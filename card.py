class Card:
    def __init__(self, card_name, card_description, key_words = []):
        self.card_name = card_name
        self.card_description = card_description
        self.key_words = key_words

    def __str__(self):
        return f"""{self.card_name}:\n{self.card_description}\nKey Words: {self.key_words}"""

    def __repr__(self):
        return f"""self.card_name = {self.card_name} : 
        self.card_description = {self.card_description} : 
        self.key_words = {self.key_words}"""