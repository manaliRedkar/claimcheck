from typing import List


class VerificationService:
    def verify(self, text: str):
        return {
            "original_input": text,
            "extracted_claim": text,
            "verdict": "unverified",
            "confidence": 0.42,
            "summary": "ClaimCheck backend is running. Real verification coming soon.",
            "supporting_sources": [],
            "contradicting_sources": [],
        }