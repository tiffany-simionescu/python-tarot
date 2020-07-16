import random
from all_cards import tarot_card_names

class Spread:
    def __init__(self, spread_name, quantity, card_position_description = []):
          self.spread_name = spread_name
          self.quantity = quantity
          self.card_position_description = card_position_description

    def __str__(self):
        return f"""You choose the {self.spread_name} spread. This spread has {self.quantity} card(s)."""

    def __repr__(self):
        return f"""self.spread_name = {self.spread_name} : 
        self.quantity = {self.quantity} : 
        self.card_position_description = {self.card_position_description}"""

    def get_cards(self, spread_name, card_count):
        i = 0
        cards = []
        while i < card_count:
            card = random.choice(tarot_card_names)

            if card not in cards:
                cards.append(card)
                print(f"\n{self.card_position_description[i]}")
                print(card)
                i += 1