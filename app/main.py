from fastapi import FastAPI
from app.models import InputText
from app.checker import run_checks

app = FastAPI(
    title="Mini Output Checker API",
    description="""
A lightweight backend service that evaluates AI-generated text
for potentially suspicious patterns such as unsupported claims,
vague citations, contradictions, and overconfident language.
""",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Mini Output Checker API is running."
    }


@app.post("/check")
def check_text(data: InputText):
    return run_checks(data.text)

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

