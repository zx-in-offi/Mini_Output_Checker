from fastapi import FastAPI
from app.models import InputText
from app.checker import run_checks

app = FastAPI(
    title="Mini Output Checker",
    description="Checks AI-generated text for suspicious patterns.",
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