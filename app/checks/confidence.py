def check_overconfidence(text: str):

    risky_words = [
        "definitely",
        "guaranteed",
        "always",
        "never",
        "undoubtedly",
        "certainly"
    ]

    lower_text = text.lower()

    found = [
        word for word in risky_words
        if word in lower_text
    ]

    fired = len(found) > 0

    return {
        "name": "overconfident_language",
        "fired": fired,
        "reason": (
            f"Contains overconfident language: {found}"
            if fired else
            "No excessive certainty detected."
        ),
        "score": 15 if fired else 0
    }