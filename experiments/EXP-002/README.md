# EXP-002 — Static vs Temporal Architecture

## Goal
RQ-009を検証し、建築アニメーションが静的表現では捉えにくい時間・身体・光・視点の関係を追加的に観察可能にするか評価する。

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
