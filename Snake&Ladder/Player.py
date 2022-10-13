from unicodedata import name


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.position = 0

    def setPosition(self, position):
        self.position = position

    def getPosition(self):
        return self.position
