from player import Player

class Dealer(Player):
    def __init__(self):
        Player.__init__(self)

    def play(self):
        pass

    def hidePrint(self) -> str:
        result = ""
        for (index, value) in enumerate(self.cards):
            result += str(value) + "    " if index > 0 else value.hidePrint() + "    "
        return result   

    def __str__(self) -> str:
        return "Dealer:\n" + super().__str__() + "\n"