from random import random
from Board import Board
import random


class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.players = []

    def setPlayers(self, players):
        self.players = players

    def move(self, player):
        moves = self.rollDice()
        move = 0
        if moves == 6:
            move = self.rollDice()
            if move == 6:
                move += self.rollDice()
            if move == 12:
                return 1
        moves += move
        print("moves = ", moves)
        if player.getPosition() == 0 and moves < 6:
            return 1

        if player.getPosition() + moves > 100:
            return 1

        playerAtThatPosition = self.board.updateBoard(player, moves)

        if playerAtThatPosition != player:
            self.resetPosition(playerAtThatPosition)
            self.board.updateBoard(player, self.rollDice())

        return 1

    def rollDice(self):
        return random.randrange(1, 7)

    def resetPosition(self, player):
        player.setPosition(0)
        return self.board.updateBoard(player, 0)

    def checkWinner(self, position):
        return self.board.getPlayer(position)
