# EXP-AFW-001 — Architecture AFW Runtime Proof

## Purpose

Validate the research-runtime architecture used by `research-architecture`:

- CrewAI-like role separation: Subject → Role → Responsibility
- LangGraph-like state evolution: State → Transition → Loop

## Hypothesis

Research work can preserve role responsibility independently from research state transitions, allowing the same runtime to execute different branches while returning to the next research question.

## Procedure

1. Start from an AFW state.
2. Execute only transitions allowed for the responsible role.
3. Record every state transition in `history`.
4. Produce a JSON execution record.
5. Run the same contract locally and through GitHub Actions.

Canonical loop:

`Intent → RQ → Task → AW/DEV/EXP → Evidence → RX → Next RQ → RQ`

## Acceptance

- Invalid role/state transitions are rejected.
- `intent` reaches `rq` through the research loop.
- `experiment` reaches `evidence → reflection → next_rq → rq`.
- Every supported start state is executable.
- GitHub Actions can run tests and upload execution evidence.

## Current result

The runtime and test suite are implemented. Local verification is represented by the same Python test contract used by the workflow.

GitHub Actions is configured for both `push` and manual `workflow_dispatch` execution.

## Boundary

This experiment validates research infrastructure. It does **not** claim that any architecture RQ has been answered.
