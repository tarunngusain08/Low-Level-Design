class Board:
    def __init__(self) -> None:
        self.Board=[[" " for i in range(3)] for j in range(3)]
    
    def updateBoard(self,row,col,symbol):
        if self.Board[row][col]!=" ":
            return -1
        else:
            self.Board[row][col]=symbol
            return 1


    def checkRow(self) -> int:
        for i in range(len(self.Board)):
            if self.Board[i] ==['0']*3:
                return 1
            if self.Board[i] ==['X']*3:
                return 2
        return 0

    def checkCol(self) -> int:
        for i in range(len(self.Board)):
            if [self.Board[0][i],self.Board[1][i],self.Board[2][i]] in [['0']*3,['X']*3]:
                return 1
        return 0


    def checkDiagonal(self) -> int:
        if [self.Board[0][0],self.Board[1][1],self.Board[2][2]] in [['0']*3,['X']*3]:
            return 1
        if [self.Board[0][2],self.Board[1][1],self.Board[2][0]] in [['0']*3,['X']*3]:
            return 1
        return 0

    def checkWinner(self) -> str:
        if self.checkCol or self.checkRow or self.checkDiagonal:
            return 1
        return 0
    
    def displayBoard(self)->None:
        for i in range(3):
            for j in range(3):
                print(self.Board[i][j],end=" ")
                
       
