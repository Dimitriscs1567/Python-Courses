class Player():
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