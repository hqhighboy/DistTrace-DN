# DistTrace-DN

DistTrace-DN is a lightweight research-software package for executable reproducibility, provenance capture, and artifact traceability in distribution-network studies. The repository provides a documented CLI workflow, benchmark configurations, deterministic reviewer outputs, and a protected-data-aware organization pattern suitable for SoftwareX-style software publication.

## Project overview

The package exposes a compact and inspectable distribution-network workflow: configuration loading, network object construction, deterministic benchmark workflow execution, analysis, economic post-processing, manifest generation, and runtime logging. It is intended to make the research workflow inspectable and rerunnable by reviewers without requiring protected engineering data.

## Motivation

Distribution-network studies often mix public benchmark cases, locally protected feeder data, scripts, manuscript figures, and partial runtime evidence. DistTrace-DN separates those layers and preserves the evidence chain from configuration to generated artifacts. The goal is reproducible science infrastructure rather than a new optimization algorithm.

## Software architecture

- `main.py` orchestrates configuration loading, module execution, and artifact writing.
- `configs/` stores public benchmark and anonymized feeder configurations.
- `core/model.py` builds the in-memory network representation.
- `core/simulation.py` runs the deterministic benchmark workflow.
- `core/analysis.py` summarizes voltage and benchmark indicators.
- `core/economics.py` computes deterministic economic post-processing indicators.
- `outputs/demo_v7/` preserves reviewer-visible JSON, CSV, manifest, and log evidence.

## Reproducibility workflow

1. Create a clean Python environment.
2. Install dependencies from `requirements.txt`.
3. Run the documented CLI command.
4. Inspect `outputs/demo_v7/run_manifest.json`.
5. Compare generated JSON/CSV artifacts with the bundled reference outputs.
6. Use `docs/reproducibility_metrics.md` and `CHECKSUMS.md5` for verification.

## Repository structure

```text
DistTrace-DN/
  README.md
  REPRODUCTION.md
  LICENSE
  requirements.txt
  MANIFEST.txt
  CHECKSUMS.md5
  main.py
  configs/
  core/
  outputs/demo_v7/
  figures/
  docs/
```

## Quick start

### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python main.py \
  --config configs/ieee33_benchmark.yaml \
  --output-dir outputs/demo_v7
```

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

python main.py `
  --config configs/ieee33_benchmark.yaml `
  --output-dir outputs/demo_v7
```

The command writes structured artifacts to `outputs/demo_v7/` and an execution log to `outputs/demo_v7/logs/run.log`.

## Example outputs

The IEEE33 benchmark demo generates:

- `network_model.json`
- `simulation_results.json`
- `analysis.json`
- `analysis_summary.json`
- `economics_summary.json`
- `voltage_profile.csv`
- `run_manifest.json`
- `logs/run.log`

Generated figures are stored in `figures/generated_artifacts_overview.png` and `figures/voltage_profile_v7.png`.

## Artifact traceability

`run_manifest.json` links each named workflow stage to its generated file. The reviewer can start from the configuration file, follow the execution through `main.py` and `core/`, and inspect the output artifacts without relying on manuscript claims.

## Protected-data-aware workflow

The release contains public benchmark and anonymized configuration files only. Protected engineering data are not required for rerunning the demo. The repository structure is designed so private feeder data can remain outside the public archive while the software, configuration schema, and reviewer-visible evidence remain citable.

## Release and citation

This package is prepared as release `v1.1.0` for GitHub and Zenodo archival. Cite the archived release once a permanent DOI is minted.

## Zenodo archival

A permanent DOI will be attached after Zenodo archival of release `v1.1.0`.

## License

MIT License. See `LICENSE`.


## Supported environment

Validated with:

- Python 3.11
- Windows 11
- Ubuntu 22.04

The workflow intentionally uses lightweight dependencies and does not require GPU acceleration.


## Deterministic execution

The bundled IEEE33 benchmark workflow is deterministic.
Repeated execution with the same configuration yields identical reviewer-visible artifacts and checksum verification results.

## Design philosophy

DistTrace-DN intentionally adopts a lightweight and inspectable software structure.
The framework prioritizes transparency, rerunnability, and artifact traceability over large-scale infrastructure abstraction.