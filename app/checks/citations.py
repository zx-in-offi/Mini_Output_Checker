import re

def check_citations(text: str):

    suspicious_phrases = [
        "studies show",
        "experts say",
        "research proves",
        "scientists confirmed",
        "harvard study",
        "mit research"
    ]

    citation_patterns = [
        r"\[\d+\]",
        r"\(.*\d{4}.*\)",
        r"https?://\S+"
    ]

    lower_text = text.lower()

    vague_claim = any(
        phrase in lower_text
        for phrase in suspicious_phrases
    )

    has_real_citation = any(
        re.search(pattern, text)
        for pattern in citation_patterns
    )

    fired = vague_claim and not has_real_citation

    return {
        "name": "suspicious_citation",
        "fired": fired,
        "reason": (
            "Contains vague authority claims without verifiable citation."
            if fired else
            "No suspicious citation patterns detected."
        ),
        "score": 35 if fired else 0
    }