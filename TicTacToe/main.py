from Game import Game
from Player import Player


def main():
    print("This is TicTacToe")
    player1name = "Tarun"  # input("Enter your player1 name")
    player1symbol = "O"  # input("Choose your symbol 'O' or 'X'")

    player2name = "Computer"
    mode = "SinglePlayer"
    player2symbol = "X" if player1symbol != "X" else "O"
    if input("Do you want to play multiplayer? - y/n ") == 'y':
        player2name = input("Enter your player2 name")
        mode = "MultiPlayer"

    player1 = Player(player1name, player1symbol)
    player2 = Player(player2name, player2symbol)

    game = Game()
    if mode == "SinglePlayer":
        move = 0
        currPlayer = player1
        while move < 9:
            if currPlayer == player1:
                if game.fetchPlayerMove(currPlayer):
                    currPlayer = player2
                    move += 1

            else:
                if game.fetchComputerMove(currPlayer):
                    currPlayer = player1
                    move += 1

            if move > 4:
                winner = game.checkWinner()
                if winner:
                    print("{} wins".format(game.winner))

    else:
        pass


main()
