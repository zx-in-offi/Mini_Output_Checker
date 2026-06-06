import re

def check_citations(text: str):

    suspicious_phrases = [
        "studies show",
        "experts say",
        "research proves",
        "scientists confirmed",
        "a harvard study",
        "mit research"
    ]

    malformed_url_pattern = r"https?://[^\s]+"

    has_suspicious_phrase = any(
        phrase in text.lower()
        for phrase in suspicious_phrases
    )

    urls = re.findall(malformed_url_pattern, text)

    invalid_url = any(
        "." not in url.split("//")[-1]
        for url in urls
    )

    fired = has_suspicious_phrase or invalid_url

    return {
        "name": "suspicious_citation",
        "fired": fired,
        "reason": (
            "Contains vague authority claims or malformed citations."
            if fired else
            "No suspicious citation patterns detected."
        ),
        "score": 35 if fired else 0
    }