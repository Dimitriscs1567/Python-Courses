from generic_player import GenericPlayer


class Player(GenericPlayer):
    def __init__(self) -> None:
        GenericPlayer.__init__(self)

    def __str__(self) -> str:
        return "Player: \n" + super().__str__() + "\n"