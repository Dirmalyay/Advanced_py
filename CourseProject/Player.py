import abc
from Deck import Deck



class AbstractPlayer(abc.ABC):
    def __init__(self, position):
        self.cards = []
        self.position = None


    def ask_card(self, deck):
        card = deck.get_card()
        self.cards.append(card)
        return True


class Player(AbstractPlayer):
    pass


class Dealer(AbstractPlayer):
    pass

# Todo: is in needed
#class Bot(AbstractPlayer):
 #   pass