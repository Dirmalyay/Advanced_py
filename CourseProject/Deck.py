from Const import SUITS, RANKS
from random import shuffle
from itertools import product

class Card:
    def __init__(self, suit, rank, points):
        self.suit = suit
        self.rank = rank
        # self.picture = picture
        self.points = points

    def __str__(self):
        massege = "\nPoints: " + str(self.points) + str(self.suit)
        return massege



class Deck:
    def __init__(self):
        self.cards = self._generate_deck()
        shuffle(self.cards)

    def _generate_deck(self):
        cards = []
        for suit, rank in product(SUITS, RANKS):
            if rank == 'ace':
                points = 11
            elif rank.isdigit():
                points = int(rank)
            else:
                points = 10
            # picture = PRINTED.get(rank)

            c = Card(suit=suit, rank=rank, points=points)
            cards.append(c)
        return cards

    def get_card(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)
