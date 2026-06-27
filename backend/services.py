from typing import List
import re


class VerificationService:
    def verify(self, text: str):
        return {
            "original_input": text,
            "extracted_claim": self._extract_claim(text),
            "verdict": "unverified",
            "confidence": 0.42,
            "summary": "ClaimCheck backend is running. Real verification coming soon.",
            "supporting_sources": [],
            "contradicting_sources": [],
        }
    
    def _extract_claim(self, text: str) -> str:
        cleaned_text = text.strip()

        cleaned_text = re.sub(r"http\S+", "", cleaned_text)
        cleaned_text = re.sub(r"#\w+", "", cleaned_text)
        cleaned_text = re.sub(r"@\w+", "", cleaned_text)
        cleaned_text = re.sub(r"\s+", " ", cleaned_text)

        return cleaned_text.strip()