# EXP-002 — Static vs Temporal Architecture

## Goal
RQ-009を検証し、建築アニメーションが静的表現では捉えにくい時間・身体・光・視点の関係を追加的に観察可能にするか評価する。

## Executable implementation

```bash
cd experiments/EXP-002
python -m venv .venv
# activate the environment, then:
pip install -r requirements.txt
python run.py --duration 6 --fps 8 --seed 42
```

Outputs are written to `experiments/EXP-002/outputs/`:

- `exp-002-static.png` — static reference
- `exp-002-temporal.gif` — deterministic temporal representation
- `manifest.json` — run parameters, checksums and structured observations

PyVista supports off-screen GIF generation through `open_gif()` and `write_frame()`, which is the mechanism used here.

## Pipeline
`CAD/BIM → Geometry → Temporal Transformation → Animation → Observation → RX → Evidence → Evaluation`

## Comparison
| View | Primary information |
|---|---|
| plan | horizontal spatial relation |
| section | vertical/spatial relation |
| elevation | facade/appearance |
| static 3D | volumetric/spatial relation |
| animation | temporal, movement, viewpoint, light |

## Procedure
1. Select a small architectural geometry.
2. Produce equivalent static views.
3. Produce deterministic animation from the same geometry.
4. Record observations independently.
5. Compare newly noticed relations.
6. Search for counterexamples.
7. Evaluate whether animation adds explanatory value.
8. Update the thesis and generate the next RQ.

## Evidence rule
Visualization output is not Evidence by itself.

`render → observation/measurement → provenance → evaluation → evidence`

## Reproducibility
Record source geometry, renderer, library versions, camera, duration, fps, seed, transformation parameters, and output checksum.

## Acceptance
The experiment succeeds even if H1 is rejected, provided the failure is reproducible and produces a useful boundary condition or next research question.
