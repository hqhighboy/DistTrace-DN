# v7 Engineering Summary

## Completed enhancements

- Executed the IEEE33 benchmark workflow through the real `main.py` CLI.
- Added reviewer-friendly artifact evidence under `outputs/demo_v7/`.
- Generated publication-ready artifact and voltage-profile figures from real outputs.
- Added reproducibility metrics, rerun consistency evidence, and a runtime repair log.
- Prepared GitHub Release `v1.1.0` structure with source, configs, docs, figures, outputs, license, manifest, and checksums.
- Prepared Zenodo checklist and `CITATION.cff` metadata.
- Prepared SoftwareX submission support files without modifying manuscript text.

## Newly generated artifacts

- `outputs/demo_v7/analysis.json`
- `outputs/demo_v7/run_manifest.json`
- `outputs/demo_v7/voltage_profile.csv`
- `outputs/demo_v7/logs/run.log`
- `figures/generated_artifacts_overview.png`
- `figures/voltage_profile_v7.png`
- `docs/reproducibility_metrics.md`

## Figures usable for the paper

- Artifact Figure A: `figures/generated_artifacts_overview.png`
- Artifact Figure B: `figures/voltage_profile_v7.png`

Both figures are derived from the real `outputs/demo_v7/` run and can be used as engineering/reproducibility evidence figures.

## GitHub release readiness

`github_release/` is ready as a clean upload candidate for GitHub Release `v1.1.0`. It excludes `.git`, `__pycache__`, LaTeX build byproducts, duplicate output folders, and manuscript-only material.

## Zenodo readiness

Zenodo preparation is complete at the metadata/checklist level. The DOI remains a placeholder until archive upload and DOI minting.

## SoftwareX engineering standard status

The package now meets a SoftwareX-style engineering evidence threshold for reproducible execution, artifact traceability, release organization, and reviewer rerun credibility. The scientific scope remains the documented deterministic reproducibility workflow; no new algorithmic or experimental claims were added.

## Next manuscript update suggestions

- Update manuscript Table 1 from `v1.0.0` to `v1.1.0` after the GitHub/Zenodo release is finalized.
- Add the two generated artifact figures only if the manuscript needs stronger reproducibility evidence.
- Keep wording focused on workflow infrastructure, provenance, and protected-data-aware reproducibility rather than new optimization capability.

## New file paths

- `main.py`
- `README.md`
- `REPRODUCTION.md`
- `MANIFEST.txt`
- `configs/ieee33_benchmark.yaml`
- `configs/engineering_feeder_anon.yaml`
- `core/__init__.py`
- `core/model.py`
- `core/simulation.py`
- `core/analysis.py`
- `core/economics.py`
- `outputs/demo_v7/network_model.json`
- `outputs/demo_v7/simulation_results.json`
- `outputs/demo_v7/analysis.json`
- `outputs/demo_v7/analysis_summary.json`
- `outputs/demo_v7/economics_summary.json`
- `outputs/demo_v7/voltage_profile.csv`
- `outputs/demo_v7/run_manifest.json`
- `outputs/demo_v7/logs/run.log`
- `figures/generated_artifacts_overview.png`
- `figures/voltage_profile_v7.png`
- `docs/reproducibility_metrics.md`
- `docs/runtime_repair_log_v7.md`
- `docs/v7_engineering_summary.md`
- `review_package/review_package_manifest.md`
- `review_package/artifact_inventory.csv`
- `zenodo/zenodo_release_checklist.md`
- `zenodo/CITATION.cff`
- `submission/highlights.txt`
- `submission/graphical_abstract_notes.md`
- `submission/cover_letter_draft.md`
- `submission/software_metadata.md`
- `github_release/README.md`
- `github_release/REPRODUCTION.md`
- `github_release/requirements.txt`
- `github_release/LICENSE`
- `github_release/MANIFEST.txt`
- `github_release/main.py`
- `github_release/CITATION.cff`
- `github_release/CHECKSUMS.md5`

