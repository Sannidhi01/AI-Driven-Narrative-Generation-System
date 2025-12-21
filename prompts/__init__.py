from prompts.understand_story import StoryUnderstandingPrompt
from prompts.align_expectation import ExpectationAlignmentPrompt
from prompts.generate_prompt import PromptGeneration

def build_prompt():
    return StoryUnderstandingPrompt(
        ExpectationAlignmentPrompt(
            PromptGeneration()
        )
    )
