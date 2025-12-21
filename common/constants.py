from enum import Enum

OPENROUTER_URL = "OPENROUTER_URL"
OPENROUTER_API_KEY = "OPENROUTER_API_KEY"

class LLMStrategyType(str, Enum):
    OPENROUTER = "openrouter"
