def check_contradictions(text: str):

    contradiction_pairs = [
        ("always", "never"),
        ("required", "optional"),
        ("yes", "no"),
        ("increase", "decrease")
    ]

    lower_text = text.lower()

    found_pairs = []

    for a, b in contradiction_pairs:
        if a in lower_text and b in lower_text:
            found_pairs.append((a, b))

    fired = len(found_pairs) > 0

    return {
        "name": "internal_contradiction",
        "fired": fired,
        "reason": (
            f"Potential contradiction detected: {found_pairs}"
            if fired else
            "No contradiction patterns detected."
        ),
        "score": 40 if fired else 0
    }