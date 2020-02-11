class DamasChinas:
    def __init__(self,Board):
        self.Board = Board
        for i in range(9):
            self.Board.append(['']*9)
        for i in range(0,9):
            for j in range(0,9):

                if(i%2 == 0):
                    self.Board[i][j] = "⬜"
                    if(j%2 == 0):
                        self.Board[i][j] = "⬛"
                if(i%2 != 0):
                    self.Board[i][j] = "⬜"
                    if(j%2 != 0):
                        self.Board[i][j] = "⬛"

                if(i == 0 and j == 0):
                    self.Board[i][j] = "0"
                if(i == 0 and j == 1 or i == 1 and j == 0):
                    self.Board[i][j] = "1"
                if(i == 0 and j == 2 or i == 2 and j == 0):
                    self.Board[i][j] = "2"
                if(i == 0 and j == 3 or i == 3 and j == 0):
                    self.Board[i][j] = "3"
                if(i == 0 and j == 4 or i == 4 and j == 0):
                    self.Board[i][j] = "4"
                if(i == 0 and j == 5 or i == 5 and j == 0):
                    self.Board[i][j] = "5"
                if(i == 0 and j == 6 or i == 6 and j == 0):
                    self.Board[i][j] = "6"
                if(i == 0 and j == 7 or i == 7 and j == 0):
                    self.Board[i][j] = "7"
                if(i == 0 and j == 8 or i == 8 and j == 0):
                    self.Board[i][j] = "8"

    def state(self):
        for x in self.Board:
            print(x)
class PiesesWhiteBlack(DamasChinas):
    def InitialPositionForPieses(self,Pieses_White,Pieses_Black):
        self.Pieses_White = Pieses_White
        self.Pieses_Black = Pieses_Black
        for i in range(0,9):
            for j in range(0,9):
                if(i == 1 and j == 1):
                    self.Board[i][j] = self.Pieses_White
                if(i == 1 and j == 3):
                    self.Board[i][j] = self.Pieses_White
                if(i == 1 and j == 5):
                    self.Board[i][j] = self.Pieses_White
                if(i == 1 and j == 7):
                    self.Board[i][j] = self.Pieses_White
                if(i == 2 and j == 2):
                    self.Board[i][j] = self.Pieses_White
                if(i == 2 and j == 4):
                    self.Board[i][j] = self.Pieses_White
                if(i == 2 and j == 6):
                    self.Board[i][j] = self.Pieses_White
                if(i == 2 and j == 8):
                    self.Board[i][j] = self.Pieses_White
                if(i == 3 and j == 1):
                    self.Board[i][j] = self.Pieses_White
                if(i == 3 and j == 3):
                    self.Board[i][j] = self.Pieses_White
                if(i == 3 and j == 5):
                    self.Board[i][j] = self.Pieses_White
                if(i == 3 and j == 7):
                    self.Board[i][j] = self.Pieses_White
                if(i == 6 and j == 2):
                    self.Board[i][j] = self.Pieses_Black
                if(i == 6 and j == 4):
                    self.Board[i][j] = self.Pieses_Black
                if(i == 6 and j == 6):
                    self.Board[i][j] = self.Pieses_Black
                if(i == 6 and j == 8):
                    self.Board[i][j] = self.Pieses_Black
                if(i == 7 and j == 1):
                    self.Board[i][j] = self.Pieses_Black
                if(i == 7 and j == 3):
                    self.Board[i][j] = self.Pieses_Black
                if(i == 7 and j == 5):
                    self.Board[i][j] = self.Pieses_Black
                if(i == 7 and j == 7):
                    self.Board[i][j] = self.Pieses_Black
                if(i == 8 and j == 2):
                    self.Board[i][j] = self.Pieses_Black
                if(i == 8 and j == 4):
                    self.Board[i][j] = self.Pieses_Black
                if(i == 8 and j == 6):
                    self.Board[i][j] = self.Pieses_Black
                if(i == 8 and j == 8):
                    self.Board[i][j] = self.Pieses_Black
    def movement(self, Row_Postion_current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late,Player,turn):
        self.Row_Postion_current = Row_Postion_current
        self.Column_Postion_current = Column_Postion_current
        self.Row_Postion_Late = Row_Postion_Late
        self.Column_Postion_Late = Column_Postion_Late

        self.Player = Player

        if(turn):
            
            if(self.Row_Postion_Late%2 != 0 and self.Column_Postion_Late%2 == 0 or self.Row_Postion_Late%2 == 0 and self.Column_Postion_Late%2 != 0):
                self.Board[Row_Postion_Current][Column_Postion_current] = self.Pieses_White
                self.Board[Row_Postion_Late][Column_Postion_Late] = '⬜'

            else:
                if(self.Board[Row_Postion_Late][Column_Postion_Late] != ' '):
                    self.Board[Row_Postion_Current][Column_Postion_current] = ' '
                    self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_White
                else:
                    self.Board[Row_Postion_Current][Column_Postion_current] = self.Pieses_White

        else:    
            if(self.Board[Row_Postion_Late][Column_Postion_Late] != ' '):
                    self.Board[Row_Postion_Current][Column_Postion_current] = ' '
                    self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_Black
                else:
                    self.Board[Row_Postion_Current][Column_Postion_current] = self.Pieses_Black


def play(self):
        self.InitialPositionForPieses('W','B')
        self.state()
        turn = False
        while(True):
            Player = input("What player do you want to be? [White or Black]: ")
            if(Player == "white" or Player == "White"):
                print("You play with White")
                turn = True
                break
            elif(Player == "Black" or Player == "black"):
                print("You play with Black")
                turn = False
                break
            else:
                print("Error, Does not exist")

        i = 0
        if turn == False:
            i = 1

        while(True):
            print(i)

            Row_Postion_current = int(input("Introduzca Fila de piesa que quieres mover: "))
            if(Raw_current== 'A' or Raw_current== 'a'):
                Row_Postion_Current = 1
            if(Raw_current== 'B' or Raw_current== 'b'):
                Row_Postion_Current = 2
            if(Raw_current== 'C' or Raw_current== 'c'):
                Row_Postion_Current = 3
            if(Raw_current== 'D' or Raw_current== 'd'):
                Row_Postion_Current = 4
            if(Raw_current== 'E' or Raw_current== 'e'):
                Row_Postion_Current = 5
            if(Raw_current== 'F' or Raw_current== 'f'):
                Row_Postion_Current = 6
            if(Raw_current== 'G' or Raw_current== 'g'):
                Row_Postion_Current = 7
            if(Raw_current== 'H' or Raw_current== 'h'):
                Row_Postion_Current = 8
            Column_Postion_current = int(input("Introduzca Columna de pieza que quieres mover: "))
            Row_Postion_Late = int(input("Introduzca Fila de pieza donde la movera: "))
            Raw_Late = input("Enter the row of the piece where it will move: ")
            if(Raw_Late== 'A' or Raw_Late== 'a'):
                Row_Postion_Late = 1
            if(Raw_Late== 'B' or Raw_Late== 'b'):
                Row_Postion_Late = 2
            if(Raw_Late== 'C' or Raw_Late== 'c'):
                Row_Postion_Late = 3
            if(Raw_Late== 'D' or Raw_Late== 'd'):
                Row_Postion_Late = 4
            if(Raw_Late== 'E' or Raw_Late== 'e'):
                Row_Postion_Late = 5
            if(Raw_Late== 'F' or Raw_Late== 'f'):
                Row_Postion_Late = 6
            if(Raw_Late== 'G' or Raw_Late== 'g'):
                Row_Postion_Late = 7
            if(Raw_Late== 'H' or Raw_Late== 'h'):
                Row_Postion_Late = 8
            Column_Postion_Late = int(input("Introduzca Columna de pieza donde la movera: "))

            if(self.Board[Row_Postion_current][Column_Postion_current] == self.Pieses_White and turn and i%2 == 0):
                self.movement(Row_Postion_current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late,Player,turn)
                self.pre()
                turn = False
                print("shift change")
                i += 1
            else:
                print(self.Board[Row_Postion_current][Column_Postion_current] == self.Pieses_Black)
                if(self.Board[Row_Postion_current][Column_Postion_current] == self.Pieses_Black and turn == False and i%2 != 0):
                    self.movement(Row_Postion_current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late,Player,turn)
                    self.pre()
                    turn = True
                    print("shift change")
                    i += 1
                else:
                    print("Invalid Movement, try again")

    def pre(self):
        super().state()

LInitialPositionForPieses = PiesesWhiteBlack([])
LInitialPositionForPieses.play()