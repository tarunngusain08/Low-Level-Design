class Board:
    def __init__(self) -> None:
        self.board = [-1]*101
        self.ladders = None
        self.snakes = None

    def getPlayer(self, position):
        return self.board[position]

    def updateBoard(self, player, move):
        position = player.getPosition()+move
        if position != 0 and self.board[position] != -1:
            return self.board[position]

        player.setPosition(position)
        self.board[position] = player
        return player

    def setLadders(self, ladders):
        self.ladders = ladders

    def setSnakes(self, snakes):
        self.snakes = snakes
