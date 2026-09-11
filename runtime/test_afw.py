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
