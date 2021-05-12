class Card():
    def __init__(self, name):
        self.name = name
        self.value = self.getValueFromName(name)  

    def getValueFromName(self, name):
        if len(name) == 3:
            return 10
        else:
            try:
                return int(name[0])
            except:
                if name[0] == "A":
                    return 1
                else:
                    return 10