"""Executable reproducibility entry point for SoftwareX review."""

from __future__ import annotations

import argparse
import csv
import json
import logging
from pathlib import Path
from typing import Any

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - exercised in minimal reviewer envs
    yaml = None

from core import analyze_results, build_network, evaluate_economics, run_power_flow

logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the minimal reproducible distribution-network workflow."
    )
    parser.add_argument(
        "--config",
        required=True,
        help="Path to a YAML configuration file.",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Directory where reproducibility artifacts will be written.",
    )
    return parser.parse_args()


def configure_logging(output_dir: Path | None = None) -> None:
    log_paths = [Path("logs") / "run.log"]
    if output_dir is not None:
        log_paths.append(output_dir / "logs" / "run.log")

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    root = logging.getLogger()
    root.handlers.clear()
    root.setLevel(logging.INFO)
    root.addHandler(console_handler)
    for log_path in log_paths:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
        file_handler.setFormatter(formatter)
        root.addHandler(file_handler)


def load_config(path: Path) -> dict[str, Any]:
    logger.info("Loading configuration from %s", path)
    with path.open("r", encoding="utf-8") as stream:
        if yaml is not None:
            config = yaml.safe_load(stream)
        else:
            config = parse_simple_yaml(stream.read())
    if not isinstance(config, dict):
        raise ValueError(f"Configuration must be a YAML mapping: {path}")
    return config


def parse_simple_yaml(text: str) -> dict[str, Any]:
    """Parse the small YAML subset used by the bundled reviewer configs."""

    raw_lines = [
        line.rstrip()
        for line in text.splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    parsed, next_index = _parse_yaml_block(raw_lines, 0, 0)
    if next_index != len(raw_lines) or not isinstance(parsed, dict):
        raise ValueError("Unsupported YAML structure in configuration file.")
    return parsed


def _parse_yaml_block(lines: list[str], start: int, indent: int) -> tuple[Any, int]:
    if start >= len(lines):
        return {}, start

    first = lines[start]
    first_indent = len(first) - len(first.lstrip(" "))
    is_list = first_indent == indent and first.lstrip().startswith("- ")
    container: Any = [] if is_list else {}
    index = start

    while index < len(lines):
        line = lines[index]
        current_indent = len(line) - len(line.lstrip(" "))
        if current_indent < indent:
            break
        if current_indent > indent:
            raise ValueError(f"Unexpected indentation: {line}")

        content = line.strip()
        if is_list:
            if not content.startswith("- "):
                break
            item_text = content[2:].strip()
            item: dict[str, Any] = {}
            if item_text:
                key, value = _split_yaml_key_value(item_text)
                item[key] = _parse_yaml_scalar(value)
            index += 1
            while index < len(lines):
                child_indent = len(lines[index]) - len(lines[index].lstrip(" "))
                if child_indent <= indent:
                    break
                key, value = _split_yaml_key_value(lines[index].strip())
                if value == "":
                    child, index = _parse_yaml_block(lines, index + 1, child_indent + 2)
                    item[key] = child
                else:
                    item[key] = _parse_yaml_scalar(value)
                    index += 1
            container.append(item)
            continue

        key, value = _split_yaml_key_value(content)
        if value == "":
            child, index = _parse_yaml_block(lines, index + 1, indent + 2)
            container[key] = child
        else:
            container[key] = _parse_yaml_scalar(value)
            index += 1

    return container, index


def _split_yaml_key_value(text: str) -> tuple[str, str]:
    if ":" not in text:
        raise ValueError(f"Expected key-value YAML entry: {text}")
    key, value = text.split(":", 1)
    return key.strip(), value.strip()


def _parse_yaml_scalar(value: str) -> Any:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    lowered = value.lower()
    if lowered in {"true", "false"}:
        return lowered == "true"
    if lowered in {"null", "none", "~"}:
        return None
    try:
        if any(marker in value for marker in [".", "e", "E"]):
            return float(value)
        return int(value)
    except ValueError:
        return value


def write_json(path: Path, data: dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as stream:
        json.dump(data, stream, indent=2, sort_keys=True)
        stream.write("\n")


def write_voltage_csv(path: Path, voltage_profile: dict[str, float]) -> None:
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(["bus_id", "voltage_pu"])
        for bus_id, voltage in voltage_profile.items():
            writer.writerow([bus_id, voltage])


def write_outputs(
    output_dir: Path,
    network: Any,
    simulation_results: dict[str, Any],
    analysis_results: dict[str, Any],
    economics_results: dict[str, Any],
) -> dict[str, str]:
    output_dir.mkdir(parents=True, exist_ok=True)

    artifacts = {
        "network_model": output_dir / "network_model.json",
        "simulation_results": output_dir / "simulation_results.json",
        "analysis": output_dir / "analysis.json",
        "analysis_summary": output_dir / "analysis_summary.json",
        "economics_summary": output_dir / "economics_summary.json",
        "voltage_profile": output_dir / "voltage_profile.csv",
        "run_manifest": output_dir / "run_manifest.json",
    }

    write_json(artifacts["network_model"], network.to_dict())
    write_json(artifacts["simulation_results"], simulation_results)
    write_json(artifacts["analysis"], analysis_results)
    write_json(artifacts["analysis_summary"], analysis_results)
    write_json(artifacts["economics_summary"], economics_results)
    write_voltage_csv(
        artifacts["voltage_profile"],
        simulation_results["voltage_profile_pu"],
    )

    manifest = {
        key: str(path.as_posix())
        for key, path in artifacts.items()
        if key != "run_manifest"
    }
    write_json(artifacts["run_manifest"], manifest)
    return manifest


def main() -> int:
    args = parse_args()
    config_path = Path(args.config)
    output_dir = Path(args.output_dir)
    configure_logging(output_dir)

    logger.info("Starting executable reproducibility workflow.")
    config = load_config(config_path)
    network = build_network(config)
    simulation_results = run_power_flow(network, config)
    analysis_results = analyze_results(network, simulation_results, config)
    economics_results = evaluate_economics(
        network,
        simulation_results,
        analysis_results,
        config,
    )
    manifest = write_outputs(
        output_dir,
        network,
        simulation_results,
        analysis_results,
        economics_results,
    )

    logger.info("Reproducible run complete. Artifact manifest: %s", manifest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
