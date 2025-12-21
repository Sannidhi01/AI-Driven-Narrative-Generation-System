from llm.openrouter import OpenRouterLLMStrategy
from common.constants import LLMStrategyType

def get_llm(strategy=LLMStrategyType.OPENROUTER):
    if strategy == LLMStrategyType.OPENROUTER:
        return OpenRouterLLMStrategy()
    else:
        raise ValueError(
            f"Unknown LLM strategy '{strategy}'. "
            f"Supported strategies are: '{LLMStrategyType.OPENROUTER.value}'"
        )
