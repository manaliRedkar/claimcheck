import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class LLMService:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
        )
    def chat(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=500,  # Increase from 10 to allow reasonable responses
        )
        return response.choices[0].message.content

    def extract_claim(self, text: str) -> str:
        """Extract the primary factual claim from text."""
        prompt = f"""Extract the primary factual claim from the following text.
        
        Requirements:
        - Remove emojis, hashtags, mentions (@username), and URLs
        - Return ONLY the claim (no explanation or metadata)
        - If no factual claim exists, return exactly: "No factual claim found."
        
        Text:
        {text}
        """
        return self.chat(prompt)