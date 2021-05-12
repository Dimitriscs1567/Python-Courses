from player import Player

class Human(Player):
    def __init__(self):
        Player.__init__(self)

    def play():
        pass

    def __str__(self) -> str:
        return "Player:\n" + super().__str__() + "\n"