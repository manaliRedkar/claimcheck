from typing import List
import re

from llm_service import LLMService


class VerificationService:
    def __init__(self):
        self.llm_service = LLMService()
        
    def verify(self, text: str):
        return {
            "original_input": text,
            "extracted_claim": self.llm_service.extract_claim(text),  # Use LLM now!
            "verdict": "unverified",
            "confidence": 0.42,
            "summary": "ClaimCheck backend is running. Real verification coming soon.",
            "supporting_sources": [],
            "contradicting_sources": [],
        }