# Reproduction Guide

This guide reproduces the IEEE33 benchmark evidence bundled with DistTrace-DN release `v1.1.1`.

## Environment setup

Use Python 3.10+.

Create and activate a virtual environment if desired, then install dependencies:

```bash
pip install -r requirements.txt
```

`main.py` includes a fallback parser for the bundled YAML configuration files, so the CLI can still run in minimal reviewer environments where PyYAML is unavailable.

## Execution command

From the repository root:

```bash
python main.py --config configs/ieee33_benchmark.yaml --output-dir outputs/demo
```

The IEEE 33-bus example is a minimal benchmark-style configuration for reproducibility demonstration. It is not a complete standard IEEE 33-bus AC power-flow validation case. The `dummy_power_flow` routine is used for deterministic artifact generation and is not presented as a validated AC power-flow solver.

## Expected outputs

The run should create or refresh:

```text
outputs/demo/network_model.json
outputs/demo/simulation_results.json
outputs/demo/analysis.json
outputs/demo/economics_summary.json
outputs/demo/voltage_profile.csv
outputs/demo/run_manifest.json
outputs/demo/logs/run.log
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

A rerun is considered consistent when the deterministic JSON and CSV artifacts match the bundled reference outputs:

```text
network_model.json
simulation_results.json
analysis.json
economics_summary.json
voltage_profile.csv
```

For checksum-based verification, inspect `CHECKSUMS.md5`.

## Adapting DistTrace-DN to a new benchmark or case study

To run DistTrace-DN with a new distribution-network benchmark or anonymized feeder configuration, follow these steps:

### Step 1: Create a new configuration file

Copy an existing configuration as a starting point:

```
copy configs\ieee33_benchmark.yaml configs\my_new_case.yaml
```

On Linux/macOS, the equivalent command is:

```
cp configs/ieee33_benchmark.yaml configs/my_new_case.yaml
```

Edit the new file to reflect your case. Key fields to update should match the actual YAML schema used in this repository. Inspect `configs/ieee33_benchmark.yaml` before editing. Typical fields may include the case name, network scale, voltage level, load summary, simulation settings, and output label.

Protected field data should be excluded from any directory staged for GitHub release or Zenodo archiving. Confidential fields should be documented in comments or metadata rather than included in open artifacts.

### Step 2: Run the workflow

```
python main.py --config configs/my_new_case.yaml --output-dir outputs/my_new_case
```

### Step 3: Verify the generated artifacts

```
type outputs\my_new_case\run_manifest.json
type CHECKSUMS.md5
```

On Linux/macOS, use:

```
cat outputs/my_new_case/run_manifest.json
cat CHECKSUMS.md5
```

The manifest lists generated files. Compare the MD5 checksums in `CHECKSUMS.md5` against local outputs to verify artifact integrity.

### Step 4: Archive the evidence package

Follow the GitHub release and Zenodo archiving steps described in the main reproduction workflow to create a citable, long-term archive of the case results.

### Notes

* The `dummy_power_flow` routine used in the IEEE 33-bus example produces deterministic outputs for artifact-traceability demonstration. To connect DistTrace-DN to a real power-flow solver such as pandapower or OpenDSS, replace the simulation execution call with a solver interface and ensure outputs are written to the configured output directory.
* Protected field data should never be placed in the outputs directory that is staged for GitHub release or Zenodo archiving.
