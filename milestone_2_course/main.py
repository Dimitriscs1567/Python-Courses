from random import shuffle
from models.dealer import Dealer
from models.player import Player
from models.card import Card
from helpful_functions import dealCards


deck = [
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

player = Player()
dealer = Dealer()
playing = True

while playing:
    shuffle(deck)
    dealCards(player, dealer, deck)
    deckIndex = 4
    print(dealer.cards)
    # Player Turn
    # Dealer Turn
    # Winning Condition
    # Cheack if player wants another game
    playing = False
