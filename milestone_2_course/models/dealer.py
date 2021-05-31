from generic_player import GenericPlayer


class Dealer(GenericPlayer):
    def __init__(self) -> None:
        GenericPlayer.__init__(self)

    def __str__(self) -> str:
        return "Dealer: \n" + super().__str__() + "\n"

    def hiddenPrint(self) -> str:
        result = ""
        for i in range(4):
            for (index, card) in enumerate(self.cards):
                if i==0:
                    result += " ____     "
                elif i==1:
                    result += "|    |    "
                elif i==2:
                    if index == 1:
                        result += "| NO |    "
                    else:
                        result += f"| {card.name} |    " if len(card.name) == 2 else f"|{card.name} |    "
                elif i==3:
                    result += "|____|    "
            
            result += "\n"
        
        result += f"Score: {self.hiddenScore()}"

        return result


    def hiddenScore(self) -> int:
        return self.cards[0].value if not self.cards[0].name.__contains__("A") else 11