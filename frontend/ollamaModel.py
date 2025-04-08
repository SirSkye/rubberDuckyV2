import ollama

class ollamaModel():
    def __init__(self):
        self.client = ollama.Client()