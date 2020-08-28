class Board:
    def __init__(self):
        self.listBoard = [[" "," "," "],[" "," "," "],[" "," "," "]] ## create empty board
        self.player = ""

        ## link object together
        self.printer = Printer(self)
        self.textInputor = TextInput(self)

    def startGame(self):
        self.round = 1
        print("Start Game : Tic-Tac-Toe!")

        try:
            while (self.round < 10):
                if self.player == "" or self.player == "O":
                    ## Player 1 Turn
                    self.player = "X"
                    pos = int(input("\nPlayer 1 turn \nEnter your position 'X': "))

                else :
                    ## Player 2 Turn
                    self.player = "O"
                    pos = int(input("\nPlayer 2 turn \nEnter your position 'O': "))

                self.textInputor.placeMarker(self.player, pos)  ## place marker in position that user entered

                self.printer.drawBoard()  ## display board

                if not(self.winCheck(self.player)):
                    ## no one win
                    self.round += 1

                else:
                    ## when have the winner
                    print("\n!!! End Game !!!")
                    break

            else:
                print("\nNo player win :( \n!!! Game Over !!!")

        except ValueError:
            ## case when entered wrong value, wrong type
            print("\nYou entered wrong value....Game will start again")
            self.clearBoard()
            self.player = ""
            self.startGame()


    def setBoard(self, player, position):
        # place marker X,O at position that user entered

        if position <= 3 and self.listBoard[0][position-1] == " ":
            self.listBoard[0][position-1] = self.player

        elif 3 < position <= 6 and self.listBoard[1][position-4] == " ":
            self.listBoard[1][position-4] = self.player

        elif 6 < position <= 9 and self.listBoard[2][position-7] == " ":
            self.listBoard[2][position-7] = self.player

        else:
            return False

    def retrieveValue(self, position): ## get value form listBoard
        if position <= 3 :
            return self.listBoard[0][position-1]

        elif 3 < position <= 6 :
            return self.listBoard[1][position-4]

        elif 6 < position <= 9 :
            return self.listBoard[2][position-7]

    def winCheck(self, player):
        # check winner
        # return True when has winner

        for i in range(len(self.listBoard)):
            if (self.listBoard[0][0] == self.listBoard[1][1] == self.listBoard[2][2] != " ") or \
            (self.listBoard[0][2] == self.listBoard[1][1] == self.listBoard[2][0] != " ") or \
            (self.listBoard[i][0] == self.listBoard[i][1] == self.listBoard[i][2] != " ") or \
            (self.listBoard[0][i] == self.listBoard[1][i] == self.listBoard[2][i] != " "):

                if player == "X":
                    playerTurn = 1
                else:
                    playerTurn = 2

                print("\n------ Player {} ({}) is winner!------".format(playerTurn, player))
                return True

        ## No player has win
        return False

    def clearBoard(self):
        self.board = [[" "," "," "],[" "," "," "],[" "," "," "]]
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
game1.startGame()#start game
