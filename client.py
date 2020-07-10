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

    # def save_reading(self, reading):
        # save the reading from spread.py for client to access later
        # Will include the question, the spread, and the cards
    def reading(self, card_name):
        # super().__init__(card_name, card_description, key_words)
        # return f"{card_name}:\n{card_description}\n{key_words}"
        pass