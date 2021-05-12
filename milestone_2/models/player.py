class Player():
    def __init__(self):
        self.cards = []

    def __str__(self):
        return "    ".join(list(map(lambda card: str(card), self.cards)))

    def play(self):
        raise NotImplementedError("Function play must be implemented")

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