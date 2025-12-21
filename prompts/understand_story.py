from prompts.base import PromptHandler

class StoryUnderstandingPrompt(PromptHandler):
    def process(self, context):
        spec = context["spec"]
        context["story_summary"] = (
            f"This act sets the stage for a larger struggle by showing how power, rules, "
            f"and decisions begin to take shape in a world where {spec['world_description'].lower()}. "
            "It introduces groups with different values, early signs of imbalance and quiet tensions that may later grow into open conflicts"
            "At its core, the act raises a simple question: "
            "what is the right way to act when rules exist, but fairness is unclear?"
        )
        return context
