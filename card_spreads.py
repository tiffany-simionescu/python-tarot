from card_position import CardPosition
from spread import Spread

# Card Position Descriptions
one_card_spread_1 = CardPosition("This is a one card spread. This card will hold all the answers to your question.")

three_card_spread_1 = CardPosition("Three Card Spread 1 position description")
three_card_spread_2 = CardPosition("Three Card Spread 2 position description")
three_card_spread_3 = CardPosition("Three Card Spread 3 position description")

celtic_cross_spread_1 = CardPosition("Celtic Cross Spread 1 position description")
celtic_cross_spread_2 = CardPosition("Celtic Cross Spread 2 position description")
celtic_cross_spread_3 = CardPosition("Celtic Cross Spread 3 position description")
celtic_cross_spread_4 = CardPosition("Celtic Cross Spread 4 position description")
celtic_cross_spread_5 = CardPosition("Celtic Cross Spread 5 position description")
celtic_cross_spread_6 = CardPosition("Celtic Cross Spread 6 position description")
celtic_cross_spread_7 = CardPosition("Celtic Cross Spread 7 position description")
celtic_cross_spread_8 = CardPosition("Celtic Cross Spread 8 position description")
celtic_cross_spread_9 = CardPosition("Celtic Cross Spread 9 position description")
celtic_cross_spread_10 = CardPosition("Celtic Cross Spread 10 position description")

# Spreads
one_card_spread = Spread("One Card Spread", 1, [
  one_card_spread_1.description
  ])
three_card_spread = Spread("Three Card Spread", 3, [
  three_card_spread_1.description,
  three_card_spread_2.description,
  three_card_spread_3.description
  ])
celtic_cross_spread = Spread("Celtic Cross Spread", 10, [
  celtic_cross_spread_1.description,
  celtic_cross_spread_2.description,
  celtic_cross_spread_3.description,
  celtic_cross_spread_4.description,
  celtic_cross_spread_5.description,
  celtic_cross_spread_6.description,
  celtic_cross_spread_7.description,
  celtic_cross_spread_8.description,
  celtic_cross_spread_9.description,
  celtic_cross_spread_10.description
])