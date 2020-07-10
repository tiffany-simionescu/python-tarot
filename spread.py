class Spread:
    def __init__(self, spread_name, quantity, card_position_description = []):
          # super().__init__(card_description, key_words)
          self.spread_name = spread_name
          self.quantity = quantity
          self.card_position_description = card_position_description
        #   self.reading = []

    def __str__(self):
        return f"""You choose the {self.spread_name} spread. 
                This spread has {self.quantity} card(s)."""

    def __repr__(self):
        return f"""self.spread_name = {self.spread_name} : 
        self.quantity = {self.quantity} : 
        self.card_position_description = {self.card_position_description}"""

    def get_card(self, card):
        # get a random card from card.py
        pass

    # def add_cards_to_reading(self, card):
    #     # for the quantity choosen for the spread
    #     # pick a random card from card.py (will need a random card method to put inside for loop)
    #     # place the card in the reading list
    #     if len(self.quantity) > 0:
    #         # print(f"This spread has {self.quantity} card(s)")
    #         for card in self.quantity:
    #             # pick random card, then append to reading list
    #             self.reading.append(card)
    def one_card_spread(self, card):
        pass