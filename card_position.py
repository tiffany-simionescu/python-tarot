class CardPosition:
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return f"{self.description}"
    
    def __repr__(self):
        return f"self.description = {self.description}"