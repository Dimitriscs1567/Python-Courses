import sys
sys.path.append('milestone_2/models')

from models.card import Card
from models.human import Human
from models.dealer import Dealer

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

human = Human()
dealer = Dealer()

print(human)