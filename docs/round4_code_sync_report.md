# Round 4 Code Sync Report

## 1. Execution time

- Completed: 2026-06-27 22:42:32 +08:00 (Asia/Shanghai)

## 2. REPO_ROOT confirmation

- `REPO_ROOT`: `H:\Project\SoftwareX\DistTrace-DN`
- `git rev-parse --show-toplevel`: `H:/Project/SoftwareX/DistTrace-DN`
- Required paths confirmed: `README.md`, `REPRODUCTION.md`, `CHECKSUMS.md5`, `main.py`, `configs/`, and `core/`.

## 3. PAPER_ROOT

- Report-copy destination only: `H:\Project\baitu_f8_project\doc-20260417\paper2_reproducible_platform`
- No LaTeX manuscript, submission PDF, or source archive was modified or generated.

## 4. Git startup state

- Branch: `main`
- Remote: `origin https://github.com/hqhighboy/DistTrace-DN.git` (fetch and push)
- Status: branch was up to date with `origin/main`; the worktree already contained 17 changed tracked paths before this round.

Startup changes recorded before editing:

```text
M  CHECKSUMS.md5
M  CITATION.cff
M  MANIFEST.txt
M  README.md
M  REPRODUCTION.md
M  core/economics.py
D  docs/project_analysis_v7.md
M  docs/reproducibility_metrics.md
M  docs/runtime_repair_log_v7.md
M  docs/v7_engineering_summary.md
M  main.py
D  outputs/demo_v7/analysis_summary.json
M  outputs/demo_v7/logs/run.log
M  outputs/demo_v7/run_manifest.json
D  outputs/final_verification/analysis_summary.json
M  outputs/final_verification/run_manifest.json
M  requirements.txt
```

Those pre-existing core, documentation, output, and dependency changes were not reverted or overwritten wholesale.

## 5. YAML field check

- `configs/ieee33_benchmark.yaml`: no `data_boundary` field.
- `configs/engineering_feeder_anon.yaml`: no `data_boundary` field.
- Actual top-level schema sections are `study`, `feeder`, `loads`, `transformers`, `simulation`, and `economics`.

## 6. Documentation handling of protected data

No configuration field was invented or added. `REPRODUCTION.md` instead states that protected field data must be excluded from GitHub/Zenodo staging directories and that confidential fields should be documented in comments or metadata rather than included in open artifacts.

## 7. REPRODUCTION.md changes

- Unified the release version to `v1.1.1`.
- Changed the primary command and expected artifacts from the legacy demo directory to `outputs/demo`.
- Documented the IEEE 33-bus example as a minimal benchmark-style reproducibility configuration, not a complete standard AC power-flow validation case.
- Documented `dummy_power_flow` as deterministic artifact generation, not a validated AC power-flow solver.
- Added the requested new-benchmark/case-study adaptation section using fields that match the inspected YAML schema.
- Removed the earlier unverified `PASS` narrative tied to the v7 engineering run.

## 8. README.md changes

- Unified release version to `v1.1.1` and DOI to `10.5281/zenodo.20408661`.
- Changed the primary CLI command, structure, artifact path, and log path to `outputs/demo`.
- Reframed the package as reproducibility-oriented/lightweight artifact traceability, execution traceability, and artifact organization and verification.
- Added explicit IEEE 33-bus and `dummy_power_flow` scope limitations.
- Removed cross-platform validation claims and retained only runtime requirements.
- Clarified that deterministic JSON/CSV artifacts and timestamped run logs have different reproducibility roles.

`CITATION.cff` was minimally synchronized to the same version, DOI, and artifact/execution-traceability wording because it already had uncommitted release edits and otherwise contradicted README.

## 9. Benchmark command and result

Command:

```text
python main.py --config configs/ieee33_benchmark.yaml --output-dir outputs/demo
```

Result: success (exit code 0). No code repair or algorithm refactor was needed.

## 10. Actual outputs/demo file list

```text
outputs/demo/analysis.json
outputs/demo/economics_summary.json
outputs/demo/logs/run.log
outputs/demo/network_model.json
outputs/demo/run_manifest.json
outputs/demo/simulation_results.json
outputs/demo/voltage_profile.csv
```

Requested key-file check:

- Present: `analysis.json`, `voltage_profile.csv`, `run_manifest.json`.
- Not generated: `model_summary.json`.
- Actual model artifact: `network_model.json`.
- Every path listed inside `run_manifest.json` exists.

## 11. CHECKSUMS.md5 update

- Replaced the legacy demo-directory entries with all seven files under `outputs/demo`.
- Recomputed hashes for other release files already covered by the checksum list.
- Verification result: `PASS (26/26)`; every listed MD5 matches the current file.
- `logs/run.log` includes timestamps, so its hash identifies this archived run rather than a byte-identical rerun expectation.

## 12. Legacy demo-directory residuals

No legacy demo-directory reference remains in `README.md`, `REPRODUCTION.md`, `CHECKSUMS.md5`, `MANIFEST.txt`, the two checked YAML files, or `.gitignore`.

The old directory is still present because this round prohibited file deletion. Content references remain only in historical engineering records and the old output manifest:

```text
docs/reproducibility_metrics.md
docs/runtime_repair_log_v7.md
docs/v7_engineering_summary.md
outputs/demo_v7/run_manifest.json
```

`MANIFEST.txt` labels the listed v7 documents as historical engineering records and explicitly says they are not the primary reproduction path.

## 13. v1.1.0 residual check

- Repository-wide pre-report scan: no match.

## 14. Strong-claim and forbidden-expression scan

Repository-wide pre-report scan results:

- No match: `REPRODUCE.md`.
- No match: `standard IEEE 33-bus used as-is`.
- No match: `Linux Ubuntu 22.04 and Windows 11`.
- No match: `we have added unit tests`.
- No match: `representative tests have been added`.
- No match: `W3C PROV-compliant`.
- No match: `provenance system`.
- No match: `provenance layer`.
- No match: `data_boundary`.
- A broad search for the standalone word `provenance` found only `docs/v7_engineering_summary.md`, a historical engineering record.

This report necessarily repeats the searched strings as diagnostic labels; those report-only mentions are not software capability claims.

## 15. Files changed or generated by this round

```text
.gitignore
CHECKSUMS.md5
CITATION.cff
MANIFEST.txt
README.md
REPRODUCTION.md
outputs/demo/analysis.json
outputs/demo/economics_summary.json
outputs/demo/logs/run.log
outputs/demo/network_model.json
outputs/demo/run_manifest.json
outputs/demo/simulation_results.json
outputs/demo/voltage_profile.csv
docs/round4_code_sync_report.md
```

A second copy of this report was requested at `H:\Project\baitu_f8_project\doc-20260417\paper2_reproducible_platform\round4_code_sync_report.md`.

No configuration, core algorithm, LaTeX, PDF, or source-archive file was changed by this round.

## 16. Push recommendation

Do not push the entire current worktree directly. First review the pre-existing unrelated modifications/deletions, inspect the generated demo artifacts, and stage only the intended release synchronization files. After that review, a scoped commit and push are appropriate. No push was performed in this round.

## 17. Manual confirmations still needed

1. Decide whether the old `outputs/demo_v7` directory and v7 engineering records should remain as historical material in the release; this round intentionally did not delete them.
2. Review ownership and intent of the 17 tracked changes that predated this round, especially `main.py`, `core/economics.py`, `requirements.txt`, and the deleted files.
3. Confirm the supplied Zenodo DOI `10.5281/zenodo.20408661` against the public deposit before release.
4. `CITATION.cff` still points `repository-code` and `url` to `hqhighboy/reproducible-distribution-network`, while Git remote `origin` is `hqhighboy/DistTrace-DN`; confirm which repository URL is canonical.
