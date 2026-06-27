# DistTrace-DN

DistTrace-DN is a lightweight research-software package for reproducibility-oriented artifact traceability in distribution-network studies. The repository provides a documented CLI workflow, benchmark configurations, deterministic reviewer outputs, execution traceability, and an artifact organization and verification pattern suitable for SoftwareX-style software publication.

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
- `outputs/demo/` preserves reviewer-visible JSON, CSV, manifest, and log evidence.

## Simulation Scope and Deterministic Surrogate Model

The primary focus of this package is software workflow reproducibility and lightweight artifact traceability. The IEEE 33-bus example is a minimal benchmark-style configuration for reproducibility demonstration; it is not a complete standard IEEE 33-bus AC power-flow validation case. The `dummy_power_flow` routine generates deterministic surrogate results for artifact generation only. It is not a validated AC power-flow solver and is not presented as numerical validation of power-flow physics.

Similarly, in economic post-processing, the `annualized_equipment_cost` relies on a placeholder fixed coefficient (`4.0` USD/kVA/year) to generate a deterministic penalty for demonstration purposes. This constant is used solely to verify the correct operation of the economics aggregation module. The voltage violation penalty uses an assumed scenario parameter of 1000 USD/violation, which is also a placeholder and not a real-world tariff.

## Reproducibility workflow

1. Create a clean Python environment.
2. Install dependencies from `requirements.txt`.
3. Run the documented CLI command.
4. Inspect `outputs/demo/run_manifest.json`.
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
  outputs/demo/
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
  --output-dir outputs/demo
```

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

python main.py `
  --config configs/ieee33_benchmark.yaml `
  --output-dir outputs/demo
```

The command writes structured artifacts to `outputs/demo/` and an execution log to `outputs/demo/logs/run.log`.

## Example outputs

The IEEE33 benchmark demo generates:

- `network_model.json`
- `simulation_results.json`
- `analysis.json`
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

This package is prepared as release `v1.1.1` for GitHub and Zenodo archival. Cite the archived release at https://doi.org/10.5281/zenodo.20408661

## Zenodo archival

The permanent DOI for release `v1.1.1` is https://doi.org/10.5281/zenodo.20408661

## License

MIT License. See `LICENSE`.


## Runtime requirements

- Python 3.10+
- Dependencies listed in `requirements.txt`

The workflow intentionally uses lightweight dependencies and does not require GPU acceleration.


## Deterministic execution

The bundled IEEE33 benchmark workflow generates deterministic JSON and CSV data artifacts for the same configuration. The execution log includes timestamps and is retained as run-specific evidence.

## Design philosophy

DistTrace-DN intentionally adopts a lightweight and inspectable software structure.
The framework prioritizes transparency, rerunnability, and artifact traceability over large-scale infrastructure abstraction.
