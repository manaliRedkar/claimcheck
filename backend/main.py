from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="ClaimCheck API",
    description="AI-powered social media claim verification platform",
    version="0.1.0",
)


class VerifyRequest(BaseModel):
    input: str


@app.get("/")
def root():
    return {"message": "Welcome to ClaimCheck"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/verify")
def verify_claim(request: VerifyRequest):
    return {
        "claim": request.input,
        "verdict": "unverified",
        "confidence": 0.42,
        "summary": "ClaimCheck backend is running. Real verification coming soon.",
        "sources": [],
    }