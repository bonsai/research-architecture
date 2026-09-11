import json
import subprocess
import sys

from afw import AFW, DEFAULT_ROLES, DEFAULT_TRANSITIONS


def test_architecture_experiment_branch():
    runtime = AFW(DEFAULT_ROLES, DEFAULT_TRANSITIONS)
    runtime.run([
        ("professor", {"intent": "architecture research"}),
        ("researcher", {"rq": "Can a building corpus be made comparable?"}),
        ("engineer", {"experiment": "architecture corpus prototype"}),
        ("analyst", {"evidence": "comparable records"}),
        ("analyst", {"reflection": "reproducible observation"}),
        ("professor", {"next_rq": "Which representation changes the result?"}),
        ("professor", {"rq": "Which representation changes the result?"}),
    ])
    assert runtime.state.history == [
        "intent", "rq", "task", "experiment", "evidence",
        "reflection", "next_rq", "rq",
    ]


def test_invalid_transition_is_rejected():
    runtime = AFW(DEFAULT_ROLES, DEFAULT_TRANSITIONS)
    try:
        runtime.step("engineer")
    except ValueError as exc:
        assert "invalid transition" in str(exc)
    else:
        raise AssertionError("invalid transition was accepted")


def test_start_state_cli_reaches_next_question():
    result = subprocess.run(
        [sys.executable, "afw.py", "experiment"],
        cwd="runtime",
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout)
    assert payload["history"] == [
        "experiment", "evidence", "reflection", "next_rq", "rq",
    ]
    assert payload["state"] == "rq"


def test_all_supported_start_states_are_executable():
    for state in ["intent", "rq", "task", "experiment", "investigation", "evidence", "reflection", "next_rq"]:
        result = subprocess.run(
            [sys.executable, "afw.py", state],
            cwd="runtime",
            check=True,
            capture_output=True,
            text=True,
        )
        assert json.loads(result.stdout)["history"][0] == state
