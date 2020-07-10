from card import Card

class Client:
    def __init__(self, name, question):
        self.name = name
        self.question = question
        self.client_readings = []

    def __str__(self):
        return f"Hello {self.name}!\nI see that the question you asked was: {self.question}"

    def __repr__(self):
        return f"self.name = {self.name} : self.question = {self.question}"