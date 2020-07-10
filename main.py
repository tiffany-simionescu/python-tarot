# Import classes
from client import Client
from card import Card
from card_position import CardPosition
from spread import Spread
import random
from card_spreads import one_card_spread, three_card_spread, celtic_cross_spread
from major_arcana import tarot_card_names

# Commands for Tarot Spreads
tarot_spreads = ['one', 'three', 'celtic']

# Beginning Program
print("Welcome to the Tabby Tarot!")

# Get Client's name and question
client_name_input = input("What's your name? ")
client_question_input = input("What is your question? ")
client = Client(client_name_input, client_question_input)

# Welcome Client
print(client)
print("I want you to clear your mind. Only focus on your question...")

# Client Instructions
print("The current spreads avaliable are the following: one card, three card, celtic cross")

while True:
  # Client Input
  card_spread_choice = input("Which spread whould you like to use? ").lower().split(" ")

  # Exit Program
  if card_spread_choice[0] == "q" or card_spread_choice[0] == "quit":
      print(f"Have a wonderful day {client.name}!")
      break

  # Client Input Error Handling
  elif len(card_spread_choice) > 2 or len(card_spread_choice) <= 1:
      print("Invalid entry. Please try again.")
      print("The current spreads avaliable are the following: one card, three card, celtic cross")

  # Conditionals for Tarot Spreads
  elif len(card_spread_choice) == 2:
      if card_spread_choice[0] in tarot_spreads:

        # One Card Spread
        if card_spread_choice[0] == 'one' and card_spread_choice[1] == "card":
            print(f"""You chose the One Card Spread. 
            This spread includes the following positions:\n{one_card_spread.card_position_description[0]}""")
            my_card = random.choice(tarot_card_names)
            print(my_card)

        # Three Card Spread
        elif card_spread_choice[0] == 'three' and card_spread_choice[1] == "cards":
            print(f"""You chose the Three Card Spread.""")

            i = 0
            cards = []
            while i < 3:
                card = key, val = random.choice(tuple(tarot_card_names.items()))

                if card not in cards:
                    cards.append(card)
                    print(three_card_spread.card_position_description[i])
                    print(card)
                    i += 1
                # Bug - Fix Output Format

        # Celtic Cross
        elif card_spread_choice[0] == 'celtic' and card_spread_choice[1] == "cross":
            print(f"""You chose the Celtic Cross Spread.""") 

            i = 0
            cards = []
            while i < 10:
                card = key, val = random.choice(tuple(tarot_card_names.items()))

                if card not in cards:
                    cards.append(card)
                    print(celtic_cross_spread.card_position_description[i])
                    print(card)
                    i += 1
                # Bug - Will print duplicate cards. Can only print a card once during a read
                # Bug - Fix Output Format

        # Error Handling
        else:
            print("That spread doesn't exist. Please try again.")