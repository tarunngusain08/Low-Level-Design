from Game import Game
from Player import Player

if __name__ == "__main__":
    print("This is Snake&Ladder")
    n = int(input("Enter the number of players - "))
    players = []

    for i in range(n+1):
        players.append(Player(chr(97+i)))

    game = Game()
    game.setPlayers(players)
    index = 0
    player = players[index]

    while game.checkWinner(100) == -1:
        index %= n+1
        player = players[index]
        game.move(player)
        index += 1
        print("player {} is on {} position".format(index, player.getPosition()))

    print("{} wins".format(game.checkWinner(100)))
