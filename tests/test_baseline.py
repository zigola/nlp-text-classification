from src.baseline import classify


def test_positive_text() -> None:
    assert classify("This is an excellent and helpful tool") == "positive"


def test_neutral_text() -> None:
    assert classify("The tool was released today") == "neutral"
