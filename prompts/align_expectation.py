from prompts.base import PromptHandler

class ExpectationAlignmentPrompt(PromptHandler):
    def process(self, context):
        context["aligned_goal"] = (
             "Translate the original conflict into a modern setting where intelligent systems shape outcomes"
              "The focus should remain on ethical responsibility, unanticipated consequences and how people react when decisions feel unfair"
            "or unchallengeable, rather than on myth or symbolism."
        )
        return context
