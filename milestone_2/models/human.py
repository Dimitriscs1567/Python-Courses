from player import Player

class Human(Player):
    def __init__(self):
        Player.__init__(self)        

    def __str__(self):
        return "Player:\n" + super().__str__() + "\n"