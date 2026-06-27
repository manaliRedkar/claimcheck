from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl
from services import VerificationService

verification_service = VerificationService()

app = FastAPI(
    title="ClaimCheck API",
    description="AI-powered social media claim verification platform",
    version="0.1.0",
)


class VerifyRequest(BaseModel):
    input: str = Field(..., min_length=5)
    source_url: Optional[HttpUrl] = None


class Source(BaseModel):
    title: str
    publisher: str
    url: HttpUrl
    relevance_score: float


class VerifyResponse(BaseModel):
    original_input: str
    extracted_claim: str
    verdict: str
    confidence: float
    summary: str
    supporting_sources: List[Source]
    contradicting_sources: List[Source]


@app.get("/")
def root():
    return {"message": "Welcome to ClaimCheck"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/verify", response_model=VerifyResponse)
def verify_claim(request: VerifyRequest):
    result = verification_service.verify(request.input)
    return VerifyResponse(**result)