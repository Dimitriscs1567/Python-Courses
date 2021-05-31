from models.dealer import Dealer
from models.player import Player


def dealCards(player: Player, dealer: Dealer, deck: list) -> None:
    player.cards.append(deck[0])
    player.cards.append(deck[2])
    dealer.cards.append(deck[1])
    dealer.cards.append(deck[3])


def playerTurn(player: Player, deck: list, deckIndex: int) -> int:
    moreCards = True

    while moreCards:
        choice = input("Do you want another card (y-n)? ")
        if choice.lower() == "y":
            player.cards.append(deck[deckIndex])
            deckIndex += 1
        elif choice.lower() == "n":
            moreCards = False
