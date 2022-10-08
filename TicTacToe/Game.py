from Board import Board
from Record import Record
from Computer import Computer
from collections import deque
from datetime import time


class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.record = Record()
        self.moves = deque()
        self.winner = None
        self.computer = Computer()
        self.timer = 15

    def move(self, value, row, col):
        return self.board.updateBoard(value, row, col)

    def fetchPlayerMove(self, player):
        self.timer = 15
        row, col = None, None
        while self.timer and (row, col) == (None, None):
            row, col = map(int, input().split())
            time.sleep(1)
            self.timer -= 1

        if (row, col) == (None, None):
            return self.fetchComputerMove(player)

        elif self.move(player.symbol, row, col):
            self.moves.append((player.name, row, col))
            return 1
        return 0

    def fetchComputerMove(self, player):
        row, col = self.computer.nextMove()
        if self.move(player.symbol, row, col):
            self.moves.append((player.name, row, col))
            return 1
        return 0

    def undoLastMove(self):
        _, row, col = self.moves.pop()
        return self.move(" ", row, col)

    def checkWinner(self):
        self.winner = self.board.checkWinner()
        if self.winner:
            self.storeRecord()
            return self.winner

    def storeRecord(self):
        return self.record.updateTable(self.winner)

    def exitGame(self):
        return self.storeRecord()
