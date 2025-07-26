from transformers import pipeline

class NLUModel:
    def __init__(self):
        self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    def classify(self, text, labels):
        return self.classifier(text, candidate_labels=labels)['labels'][0]