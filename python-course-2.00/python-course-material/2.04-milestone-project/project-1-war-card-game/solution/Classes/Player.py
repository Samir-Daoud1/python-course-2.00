class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.won_cards = []

    def add_cards(self, cards):
        self.cards.extend(cards)

    def draw_card(self):
        return self.cards.pop()

    def total_cards(self):
        return len(self.cards) + len(self.won_cards)

    def __str__(self):
        return self.name