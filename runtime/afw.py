"""Minimal AFW runtime for architecture research.

Role layer: Subject -> Role -> Responsibility
State layer: State -> Transition -> Loop
"""

from dataclasses import dataclass, field
import argparse
import json
from typing import Any


@dataclass(frozen=True)
class Role:
    name: str
    responsibility: str


@dataclass(frozen=True)
class Transition:
    source: str
    target: str
    actor: str


@dataclass
class ResearchState:
    state: str = "intent"
    payload: dict[str, Any] = field(default_factory=dict)
    history: list[str] = field(default_factory=lambda: ["intent"])


class AFW:
    def __init__(self, roles: list[Role], transitions: list[Transition], start_state: str = "intent"):
        valid_states = {t.source for t in transitions} | {t.target for t in transitions}
        if start_state not in valid_states:
            raise ValueError(f"invalid start state: {start_state!r}")
        self.roles = {role.name: role for role in roles}
        self.transitions = transitions
        self.state = ResearchState(start_state, history=[start_state])

    def available(self) -> list[Transition]:
        return [t for t in self.transitions if t.source == self.state.state]

    def step(self, actor: str, output: dict[str, Any] | None = None) -> ResearchState:
        if actor not in self.roles:
            raise ValueError(f"unknown role: {actor!r}")
        candidates = [t for t in self.available() if t.actor == actor]
        if not candidates:
            raise ValueError(f"invalid transition: state={self.state.state!r}, actor={actor!r}")
        transition = candidates[0]
        self.state.state = transition.target
        if output:
            self.state.payload.update(output)
        self.state.history.append(transition.target)
        return self.state

    def run(self, actors: list[tuple[str, dict[str, Any] | None]]) -> ResearchState:
        for actor, output in actors:
            self.step(actor, output)
        return self.state


DEFAULT_ROLES = [
    Role("professor", "question"),
    Role("researcher", "investigate"),
    Role("engineer", "implement"),
    Role("analyst", "evaluate"),
    Role("archivist", "record"),
]

DEFAULT_TRANSITIONS = [
    Transition("intent", "rq", "professor"),
    Transition("rq", "task", "researcher"),
    Transition("task", "investigation", "researcher"),
    Transition("task", "experiment", "engineer"),
    Transition("investigation", "evidence", "analyst"),
    Transition("experiment", "evidence", "analyst"),
    Transition("evidence", "reflection", "analyst"),
    Transition("reflection", "next_rq", "professor"),
    Transition("next_rq", "rq", "professor"),
]


DEMO_PATHS: dict[str, list[tuple[str, dict[str, Any]]]] = {
    "intent": [
        ("professor", {"intent": "Can architecture data become research evidence?"}),
        ("researcher", {"rq": "Can a building corpus be made comparable?"}),
        ("engineer", {"experiment": "build architecture corpus prototype"}),
        ("analyst", {"evidence": "prototype produced comparable records"}),
        ("analyst", {"reflection": "observation is reproducible enough for RX"}),
        ("professor", {"next_rq": "Which representation changes the result?"}),
        ("professor", {"rq": "Which representation changes the result?"}),
    ],
    "rq": [
        ("researcher", {"rq": "Can a building corpus be made comparable?"}),
        ("engineer", {"experiment": "build architecture corpus prototype"}),
        ("analyst", {"evidence": "prototype produced comparable records"}),
        ("analyst", {"reflection": "observation is reproducible enough for RX"}),
        ("professor", {"next_rq": "Which representation changes the result?"}),
        ("professor", {"rq": "Which representation changes the result?"}),
    ],
    "task": [
        ("engineer", {"experiment": "build architecture corpus prototype"}),
        ("analyst", {"evidence": "prototype produced comparable records"}),
        ("analyst", {"reflection": "observation is reproducible enough for RX"}),
        ("professor", {"next_rq": "Which representation changes the result?"}),
        ("professor", {"rq": "Which representation changes the result?"}),
    ],
    "experiment": [
        ("analyst", {"evidence": "prototype produced comparable records"}),
        ("analyst", {"reflection": "observation is reproducible enough for RX"}),
        ("professor", {"next_rq": "Which representation changes the result?"}),
        ("professor", {"rq": "Which representation changes the result?"}),
    ],
    "investigation": [
        ("analyst", {"evidence": "investigation produced comparable records"}),
        ("analyst", {"reflection": "observation is reproducible enough for RX"}),
        ("professor", {"next_rq": "Which representation changes the result?"}),
        ("professor", {"rq": "Which representation changes the result?"}),
    ],
    "evidence": [
        ("analyst", {"reflection": "observation is reproducible enough for RX"}),
        ("professor", {"next_rq": "Which representation changes the result?"}),
        ("professor", {"rq": "Which representation changes the result?"}),
    ],
    "reflection": [
        ("professor", {"next_rq": "Which representation changes the result?"}),
        ("professor", {"rq": "Which representation changes the result?"}),
    ],
    "next_rq": [
        ("professor", {"rq": "Which representation changes the result?"}),
    ],
}


def run_demo(start_state: str = "intent") -> ResearchState:
    runtime = AFW(DEFAULT_ROLES, DEFAULT_TRANSITIONS, start_state)
    return runtime.run(DEMO_PATHS[start_state])


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the architecture AFW research loop.")
    parser.add_argument("start_state", nargs="?", default="intent", choices=sorted(DEMO_PATHS))
    args = parser.parse_args()
    result = run_demo(args.start_state)
    print(json.dumps({"history": result.history, "state": result.state, "payload": result.payload}, ensure_ascii=False))


if __name__ == "__main__":
    main()
