class Card():
    def __init__(self, name: str) -> None:
        self.name = name
        self.value = self.getValueFromName()

    def __str__(self) -> str:
        return self.name

    def getValueFromName(self) -> int:
        # name = 2*, 5*, A*, 10*, K*
        valueString = self.name[:-1]
        try:
            return int(valueString)
        except:
            # A K Q J
            return 1 if valueString == "A" else 10