from app.checks.numeric_claims import check_numeric_claims
from app.checks.citations import check_citations
from app.checks.contradictions import check_contradictions
from app.checks.confidence import check_overconfidence

def run_checks(text: str):

    checks = [
        check_numeric_claims(text),
        check_citations(text),
        check_contradictions(text),
        check_overconfidence(text)
    ]

    score = sum(check["score"] for check in checks)

    if score >= 60:
        verdict = "suspicious"
    elif score >= 25:
        verdict = "review"
    else:
        verdict = "clean"

    return {
        "verdict": verdict,
        "score": score,
        "checks": checks
    }