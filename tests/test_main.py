from streamlit.testing.v1 import AppTest

at = AppTest.from_file("main.py").run()


def test_session_state_datasets():
    assert "DATASETS" in at.session_state
    datasets = at.session_state["DATASETS"]
    expected_keys = {"Digenea", "Cestoda", "Chromadorea", "Enoplea"}
    assert set(datasets.keys()) == expected_keys
