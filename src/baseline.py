"""Dependency-light baseline for keyword-based text classification."""

from __future__ import annotations

POSITIVE = {"good", "great", "excellent", "helpful", "love"}
NEGATIVE = {"bad", "poor", "broken", "hate", "slow"}


def classify(text: str) -> str:
    words = {word.strip(".,!?;:").lower() for word in text.split()}
    positive = len(words & POSITIVE)
    negative = len(words & NEGATIVE)
    if positive > negative:
        return "positive"
    if negative > positive:
        return "negative"
    return "neutral"


if __name__ == "__main__":
    print(classify(input("Text: ")))
