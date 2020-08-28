class Board() :
    def __init__(self):
        self.listBoard = [[" "," "," "],[" "," "," "],[" "," "," " ]]
        self.player="o"   #start player

        self.text = TextInput(self)  #instance from class  to Input and drawBoard
        self.printed = Printer(self)

    def startGame(self) :
        self.round=1        #starter round
        self.printed.drawBoard()      #draw empty board
        while(self.winCheck(self.player)) :       #check if someone win

            if self.round >= 9:         #if round over 9 then stop
                print("Draw")
                break
            if self.round%2==1 :        #swap player
                self.player = "o"
            else :
                self.player = "x"
            print("Player",self.player,"Turn ")  #display turn
            try :
                position = int(input("insert position : "))
                if self.text.placeMarker(self.player, position) : #input to the board
                    self.round +=1
            except :
                print("Invalid Input : Try again")
            self.printed.drawBoard()          #draw new board

        if int(input("""Enter "1" to play  again else to stop """))==1 :
            self.clearBoard()
            self.start()

    def retrieveValue(self,position) :  #getter method
        return self.listBoard[int((position-1)/3)][(position-1)%3]

    def setBoard(self,player,position) :     #setter setBoard
        self.listBoard[int((position-1)/3)][(position-1)%3] = player

    def winCheck(self,player) :  #if someone wins return false to stop loop
        if self.listBoard[0][0] == self.listBoard[0][1] == self.listBoard[0][2] and self.listBoard[0][2] != " ":
            print("Player",player,"WINS!")
            return False
        elif self.listBoard[1][0] == self.listBoard[1][1] == self.listBoard[1][2] and self.listBoard[1][2] != " ":
            print("Player",player,"WINS!")
            return False
        elif self.listBoard[2][0] == self.listBoard[2][1] == self.listBoard[2][2] and self.listBoard[2][2] != " ":
            print("Player",player,"WINS!")
            return False
        elif self.listBoard[0][0] == self.listBoard[1][0] == self.listBoard[2][0] and self.listBoard[2][0] != " ":
            print("Player",player,"WINS!")
            return False
        elif self.listBoard[0][1] == self.listBoard[1][1] == self.listBoard[2][1] and self.listBoard[2][1] != " ":
            print("Player",player,"WINS!")
            return False
        elif self.listBoard[0][2] == self.listBoard[1][2] == self.listBoard[2][2] and self.listBoard[2][2] != " ":
            print("Player",player,"WINS!")
            return False
        elif self.listBoard[0][0] == self.listBoard[1][1] == self.listBoard[2][2] and self.listBoard[2][2] != " ":
            print("Player",player,"WINS!")
            return False
        elif self.listBoard[0][2] == self.listBoard[1][1] == self.listBoard[2][0] and self.listBoard[2][0] != " ":
            print("Player",player,"WINS!")
            return False
        else:
            return True

    def clearBoard(self) :
        self.listBoard = [[" "," "," "],[" "," "," "],[" "," "," " ]]

class TextInput() :
    def __init__(self, object) :
        self.board=object
    def placeMarker(self, player,position) :  #input
        if((position<0 or position>9)) :  #if is over bound
            print("Error Insert again")
            return False
        elif (self.board.retrieveValue(position)!=" ") :  #if it's overlap
            print("Overlap Insert again")
            return False
        else :
            self.board.setBoard(player, position)  #set to board
            return True

class Printer() :

    def __init__ (self, object) :
        self.board=object

    def drawBoard(self) :  #preview board
        print(self.board.retrieveValue(1) + " | " + self.board.retrieveValue(2) + " | " + self.board.retrieveValue(3))
        print("----------")
        print(self.board.retrieveValue(4) + " | " + self.board.retrieveValue(5) + " | " + self.board.retrieveValue(6))
        print("----------")
        print(self.board.retrieveValue(7) + " | " + self.board.retrieveValue(8) + " | " + self.board.retrieveValue(9)+"\n")

game1=Board()#instance obj from Board
game1.start()#start game
