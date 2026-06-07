def check_contradictions(text: str):

    contradiction_patterns = [
        ("required", "optional"),
        ("always", "never"),
        ("can", "cannot"),
        ("is", "is not")
    ]

    sentences = [
        sentence.strip().lower()
        for sentence in text.split(".")
        if sentence.strip()
    ]

    found = []

    for sentence in sentences:
        for a, b in contradiction_patterns:
            if a in sentence and b in sentence:
                found.append((a, b))

    fired = len(found) > 0

    return {
        "name": "internal_contradiction",
        "fired": fired,
        "reason": (
            f"Potential contradiction patterns detected: {found}"
            if fired else
            "No contradiction patterns detected."
        ),
        "score": 40 if fired else 0
    }