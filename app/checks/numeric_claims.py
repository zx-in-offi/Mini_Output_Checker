import re

def check_numeric_claims(text: str):
    pattern = r"\b\d+(\.\d+)?%|\b\d{4}\b|\b\d{1,3}(,\d{3})+\b"

    matches = re.findall(pattern, text)

    attribution_words = [
        "according to",
        "source",
        "study",
        "report",
        "research"
    ]

    has_attribution = any(
        word in text.lower() for word in attribution_words
    )

    fired = len(matches) > 0 and not has_attribution

    return {
        "name": "unsupported_numeric_claim",
        "fired": fired,
        "reason": (
            "Contains numerical/statistical claims without attribution."
            if fired else
            "No suspicious unsupported numeric claims detected."
        ),
        "score": 25 if fired else 0
    }