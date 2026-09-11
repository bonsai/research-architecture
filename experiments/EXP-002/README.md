# EXP-002 — Static vs Temporal Architecture

## Goal
RQ-009「建築を時間・身体・光・視点によって変化する経験として記述できるか」を、静的表現と時間表現の比較で検証する。

## Phase
Phase 1 — Experiment / Implementation

## Research chain
`RQ-009 → EXT-009 → EXP-002 → RX → Evidence → Thesis / Next RQ`

RXはEXP-002に属する研究経験記録。独立した研究成果ではなく、観察・解釈・状態変化を記録する。

## Run

```bash
cd experiments/EXP-002
python -m venv .venv
pip install -r requirements.txt
python run.py --duration 6 --fps 8 --seed 42
```

Outputs:
- `outputs/exp-002-static.png` — static baseline
- `outputs/exp-002-temporal.gif` — deterministic temporal representation
- `outputs/manifest.json` — parameters, checksums, observations

## Research artifacts

| File | Role |
|---|---|
| `run.py` | experiment execution |
| `requirements.txt` | runtime dependencies |
| `observations.yaml` | observation schema + records |
| `evaluation.yaml` | comparison criteria + scoring |
| `README.md` | experiment definition / procedure / RX |

## Observation

`render → observe → interpret → compare → falsify → evaluate → evidence`

Record:
- observer / view / time
- spatial relation
- relation noticed
- interpretation
- confidence
- counterexample
- provenance

## RX

Research Experience records:
- what became noticeable
- what was expected / surprising
- confidence change
- interpretation change
- unresolved uncertainty
- next question

Example:

```yaml
trigger: "first temporal walkthrough"
experience: "movement made the relation between entrance and central void noticeable"
interpretation: "the relation may be temporal rather than purely geometric"
confidence_before: 0.40
confidence_after: 0.65
state_update: "temporal relation is now a candidate research variable"
next_question: "Can observers reproduce this relation without animation?"
```

## Falsification

The following conditions constrain or reject the claim:

- **Static equivalence** — the relation is already derivable from static views.
- **Attention illusion** — apparent discovery is caused by camera, editing, lighting, or motion salience.
- **Observer disagreement** — observers do not reliably identify the same relation.
- **Representation artifact** — renderer assumptions introduce the observed relation.
- **Convenience only** — the same information is obtained numerically or statically with equal or better reliability.

## Evidence rule

Visualization is not Evidence by itself.

`render → observation/measurement → provenance → evaluation → evidence`

## Reproducibility

Record source geometry, renderer/version, camera, duration, fps, seed, transformation parameters, and output checksum.

## Acceptance

H1 may be rejected. A reproducible failure is a valid result when it produces a boundary condition or next RQ.
