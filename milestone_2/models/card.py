class Card():
    def __init__(self, name):
        self.name = name
        self.value = self.getValueFromName(name)        

    def getValueFromName(self, name):
        if len(name) == 3:
            return int(name[0:1])
        else:
            try:
                self.value = int(name[0])
            except:
                if name[0] == "A":
                    return 1
                else:
                    return 10

    def hidePrint():
        return f" ____\n|    |\n| NO |\n|____|"

    def __str__(self) -> str:
        return f" ____\n|    |\n| {self.name} |\n|____|"