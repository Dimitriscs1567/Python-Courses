class Player():
    def __init__(self):
        self.cards = []

    def calculate(self):
        score = 0
        hasAce = False
        
        for card in self.cards:
            if card.name.__contains__("A"):
                hasAce = True

            score += card.value
        
        if score + 10 < 22 and hasAce:
            score += 10

        return score

    def dealCards(self, *cards):
        for card in cards:
            self.cards.append(card)

    def __str__(self):
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
        
        result += f"Score: {self.calculate()}"

        return result