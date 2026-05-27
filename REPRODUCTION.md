# Reproduction Guide

This guide reproduces the IEEE33 benchmark evidence bundled with DistTrace-DN release `v1.1.0`.

## Environment setup

Use Python 3.10 or later. The verified local run used:

```text
C:\Python314\python.exe
Python 3.14.0
```

Create and activate a virtual environment if desired, then install dependencies:

```bash
pip install -r requirements.txt
```

`main.py` includes a fallback parser for the bundled YAML configuration files, so the CLI can still run in minimal reviewer environments where PyYAML is unavailable.

## Execution command

From the repository root:

```bash
python main.py --config configs/ieee33_benchmark.yaml --output-dir outputs/demo_v7
```

## Expected outputs

The run should create or refresh:

```text
outputs/demo_v7/network_model.json
outputs/demo_v7/simulation_results.json
outputs/demo_v7/analysis.json
outputs/demo_v7/analysis_summary.json
outputs/demo_v7/economics_summary.json
outputs/demo_v7/voltage_profile.csv
outputs/demo_v7/run_manifest.json
outputs/demo_v7/logs/run.log
```

## Artifact interpretation

- `network_model.json` records the constructed benchmark network container.
- `simulation_results.json` records deterministic voltage and loss outputs.
- `analysis.json` records benchmark summary metrics.
- `economics_summary.json` records deterministic economic post-processing outputs.
- `voltage_profile.csv` provides the bus-level voltage profile used for the publication figure.
- `run_manifest.json` links workflow stage names to generated files.
- `logs/run.log` provides execution-level evidence.

## Rerun verification

A rerun is considered consistent when the JSON and CSV artifacts match the bundled reference outputs. The v7 engineering run compared the following artifacts and obtained status `PASS`:

```text
network_model.json
simulation_results.json
analysis.json
analysis_summary.json
economics_summary.json
voltage_profile.csv
```

For checksum-based verification, inspect `CHECKSUMS.md5`.
