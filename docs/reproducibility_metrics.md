# Reproducibility Metrics

Evidence source: real CLI execution in `versions/v7`.

## Execution

- Command: `python main.py --config configs/ieee33_benchmark.yaml --output-dir outputs/demo_v7`
- Runtime: 0.084 seconds
- Return status: success
- Config load status: success (`configs/ieee33_benchmark.yaml`)
- Output directory: `outputs/demo_v7`

## Artifact Metrics

- Artifact count: 8 files
- Manifest size: 370 bytes
- Generated file types: .csv, .json, .log
- Required evidence files present: analysis.json, run_manifest.json, voltage_profile.csv, logs/run.log

## Run Results Extracted from Real Artifacts

- Network: ieee33_benchmark
- Bus count: 33
- Min voltage: 0.92 p.u.
- Max voltage: 1.0 p.u.
- Mean voltage: 0.96 p.u.
- Voltage violation count: 12
- Line losses: 44.58 kW
- Placeholder total cost: 53572.08 USD

## Rerun Consistency

- Status: PASS
- Compared artifacts: network_model.json, simulation_results.json, analysis.json, analysis_summary.json, economics_summary.json, voltage_profile.csv
- Deterministic artifact hashes matched: True

## Python Environment

- Python executable: `C:\Python314\python.exe`
- Python version: `3.14.0`
- Platform: `Windows-10-10.0.19045-SP0`
- Matplotlib version used for figures: `3.10.8`

## Repair Record

See `docs/runtime_repair_log_v7.md` for the dependency/import and artifact-path repairs made during real execution.
