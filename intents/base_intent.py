class BaseIntent:
    def __init__(self, nlu):
        self.nlu = nlu

    def handle(self, user_input):
        raise NotImplementedError("Each intent must implement the handle method.")