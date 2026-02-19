def test_event_increases_stress():
    engine = MoodEngine()
    engine.apply_event("cluster_error")
    assert engine.state.moods["stressed"].intensity > 0
