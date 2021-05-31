class GenericPlayer():
    def __init__(self) -> None:
        self.cards = []

    def calculateScore(self) -> int:
        aces = list(filter(lambda card: card.name.__contains__("A"), self.cards))
        sum = 0

        for card in self.cards:
            sum += card.value

        if len(aces) > 0 and sum + 10 <= 21:
            sum += 10

        return sum


    def __str__(self) -> str:
        result = ""
        for i in range(4):
            for card in self.cards:
                if i==0:
                    result += " ____     "
                elif i==1:
                    result += "|    |    "
                elif i==2:
                    result += f"| {card.name} |    " if len(card.name) == 2 else f"|{card.name} |    "
                elif i==3:
                    result += "|____|    "
            
            result += "\n"
        
        result += f"Score: {self.calculateScore()}"

        return result