from models.human import Human
from models.dealer import Dealer
from models.card import Card

from random import randint

class Data():
    def __init__(self):
        self.human = Human()
        self.dealer = Dealer()
        self.deck = [
            Card("A*"), Card("A#"), Card("A-"), Card("A+"),
            Card("2*"), Card("2#"), Card("2-"), Card("2+"),
            Card("3*"), Card("3#"), Card("3-"), Card("3+"),
            Card("4*"), Card("4#"), Card("4-"), Card("4+"),
            Card("5*"), Card("5#"), Card("5-"), Card("5+"),
            Card("6*"), Card("6#"), Card("6-"), Card("6+"),
            Card("7*"), Card("7#"), Card("7-"), Card("7+"),
            Card("8*"), Card("8#"), Card("8-"), Card("8+"),
            Card("9*"), Card("9#"), Card("9-"), Card("9+"),
            Card("10*"), Card("10#"), Card("10-"), Card("10+"),
            Card("J*"), Card("J#"), Card("J-"), Card("J+"),
            Card("Q*"), Card("Q#"), Card("Q-"), Card("Q+"),
            Card("K*"), Card("K#"), Card("K-"), Card("K+"),
        ]

    def initDeal(self):
        self.human.dealCards(
            self.deck.pop(randint(0, len(self.deck) - 1)), 
            self.deck.pop(randint(0, len(self.deck) - 1))
        )

        self.dealer.dealCards(
            self.deck.pop(randint(0, len(self.deck) - 1)), 
            self.deck.pop(randint(0, len(self.deck) - 1))
        )

    def print(self, hidden):
        print(self.human)
        print(self.dealer.hidenPrint() if hidden else self.dealer)

    def dealCardHuman(self):
        self.human.dealCards(self.deck.pop(randint(0, len(self.deck) - 1)))

    def dealCardDealer(self):
        self.dealer.dealCards(self.deck.pop(randint(0, len(self.deck) - 1)))