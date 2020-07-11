from card import Card

# Cards
the_fool = Card("0 - The Fool", 
"""Now is the time to go and take that risk into the unknown.
 Have the courage to open up and experience new areas in your life. 
 Don't let uncertainty stop you!""", 
["beginnings", "innocence", "free spirit"])

the_magician = Card("1 - The Magician", 
"""Now is the time to tap into your full potential without hesitation, and take action!
This might be in your new job, new business venture, or possibly a new love interest.
Holding back would only mean missing the opportunity of becoming the best version of yourself.
Depending on your choice, there will be change ahead, so have faith in yourself.""", 
["manifestation", "resourcefullness", "power"])

the_high_priestess = Card("2 - The High Priestess", 
"""This is a time to search within yourself. As hard as you try to find answers, 
you will not find them in the outside world. The answers you seek lie within you.
Your intuition will guide you through this one. Not intellect.""", 
["intuition", "inner voice", "higher power"])

the_empress = Card("3 - The Empress", 
"""This card is a strong indication of pregnancy and motherhood (Depending on surrounding cards).
The Empress can also represent the birth of a new idea, business or project. 
Due to the likely successful outcome, this is the time to devote yourself towards accomplishing your ideas.""", 
["fertility", "creativity", "abundance"])

the_emperor = Card("4 - The Emperor", 
"""This card symbolizes control, authority, organization and fatherhood. 
This is someone that guides with a firm hand, gives structure, creates rules and imparts knwledge.
His goals are always aligned with the greater good.""", 
["structure", "authority", "discipline"])

the_hierophant = Card("0 - The Hierophant", "This is the Hierophant's description", ["beginnings", "starts"])
the_lovers = Card("0 - The Lovers", "This is the Lover's description", ["beginnings", "starts"])
the_chariot = Card("0 - The Chariot", "This is the Chariot's description", ["beginnings", "starts"])
strength = Card("0 - Strength", "This is Strength's description", ["beginnings", "starts"])
the_hermit = Card("0 - The Hermit", "This is the Hermit's description", ["beginnings", "starts"])

tarot_card_names = {
  1: the_fool,
  2: the_magician,
  3: the_high_priestess,
  4: the_empress, 
  5: the_emperor,
  6: the_hierophant,
  7: the_lovers,
  8: the_chariot,
  9: strength,
  10: the_hermit
}