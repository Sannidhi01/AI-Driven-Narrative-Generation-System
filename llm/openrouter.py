import os
import requests
from llm.base import LLMStrategy
from common.constants import OPENROUTER_API_KEY, OPENROUTER_URL

class OpenRouterLLMStrategy(LLMStrategy):
    def __init__(self, model="gpt-4o-mini", temperature=0.3):
        self.model = model
        self.temperature = temperature

        self.api_key = os.getenv(OPENROUTER_API_KEY)
        if not self.api_key:
            raise RuntimeError(
                "OPENROUTER_API_KEY not set. "
                "Please export it as an environment variable."
            )

    def generate(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "messages": [
                {"role": "user",
                 "content": prompt}
            ],
            "temperature": self.temperature
        }
        response = requests.post(
            os.getenv(OPENROUTER_URL),
            headers=headers,
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
