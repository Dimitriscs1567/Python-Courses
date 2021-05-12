from player import Player

class Dealer(Player):
    def __init__(self):
        Player.__init__(self)

    def hidenPrint(self):
        result = "Dealer:\n"
        for i in range(4):
            for (index, value) in enumerate(self.cards):
                if i==0:
                    result += " ____     "
                elif i==1:
                    result += "|    |    "
                elif i==2:
                    if index == 0:
                        result += f"| NO |    "
                    else:
                        result += f"| {value.name} |    " if len(value.name) == 2 else f"|{value.name} |    "
                elif i==3:
                    result += "|____|    "

            result += "\n"

        return result   

    def __str__(self):
        return "Dealer:\n" + super().__str__() + "\n"