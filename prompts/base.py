class PromptHandler:
    def __init__(self, next_handler=None):
        self.next = next_handler

    def handle(self, context):
        updated = self.process(context)
        if self.next:
            return self.next.handle(updated)
        return updated

    def process(self, context):
        raise NotImplementedError
