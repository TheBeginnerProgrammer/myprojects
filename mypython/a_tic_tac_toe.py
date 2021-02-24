import random

def printGameBoard():
    for i in gameBoard:
        print(*i)

def resetGameBoard():
     resetBoard = [["1","|","2","|","3"],
             ["-","+","-","+","-"],
             ["4","|","5","|","6"],
             ["-","+","-","+","-"],
             ["7","|","8","|","9"]]
     return resetBoard
    

def countNumbers():
    numbers = {"1","2","3","4","5","6","7","8","9"}
    count = 0
    for i in range(len(gameBoard)):
        for j in range(len(gameBoard)):
            if gameBoard[i][j] in numbers:
                count +=1
    return(count)


def playerTurns():
    playerInput = int(input("Enter your position : "))

    if (playerInput not in cpuChoice) and (playerInput not in playerChoice):
        playerChoice.add(playerInput)
        
        if playerInput == 1:
            gameBoard[0][0] = "X"
        if playerInput == 2:
            gameBoard[0][2] = "X"
        if playerInput == 3:
            gameBoard[0][4] ="X"
        if playerInput == 4:
            gameBoard[2][0] = "X"
        if playerInput == 5:
            gameBoard[2][2] ="X"
        if playerInput == 6:
            gameBoard[2][4] ="X"
        if playerInput == 7:
            gameBoard[4][0] = "X"
        if playerInput == 8:
            gameBoard[4][2] = "X"
        if playerInput == 9:
            gameBoard [4][4] ="X"
    else:
        print("Position taken. Enter another position...")
        playerTurns()


def cpuTurns():
    cpuInput = random.randint(1,9)
    print("CPU's position is: ",cpuInput)

    if (cpuInput not in playerChoice) and (cpuInput not in cpuChoice):
        cpuChoice.add(cpuInput)

        if cpuInput == 1:
            gameBoard[0][0] = "O"
        if cpuInput == 2:
            gameBoard[0][2] = "O"
        if cpuInput == 3:
            gameBoard[0][4] ="O"
        if cpuInput == 4:
            gameBoard[2][0] = "O"
        if cpuInput == 5:
            gameBoard[2][2] ="O"
        if cpuInput == 6:
            gameBoard[2][4] ="O"
        if cpuInput == 7:
            gameBoard[4][0] = "O"
        if cpuInput == 8:
            gameBoard[4][2] = "O"
        if cpuInput == 9:
            gameBoard [4][4] ="O"

    else:
        cpuTurns()



def checkGame():
    playerPiece = 0
    cpuPiece = 0
    h = 0
    v = 0

    while h < 5:
        for x in range(0,len(gameBoard),2):
            if gameBoard[0+h][x]== "X":
                playerPiece += 1
            elif gameBoard[0+h][x] =="O":
                cpuPiece += 1
        if playerPiece == 3:
            print("Player wins!")
            return True
        elif cpuPiece == 3:
            print("CPU Wins!")
            return True
        elif playerPiece < 3 or cpuPiece < 3:
            playerPiece = 0
            cpuPiece = 0
        h += 1


    while v < 5:
        for y in range(0,len(gameBoard),2):
            if gameBoard[y][v]== "X":
                playerPiece += 1
            elif gameBoard[y][v] =="O":
                cpuPiece += 1
        if playerPiece == 3:
            print("Player wins!")
            return True
        elif cpuPiece == 3:
            print("CPU Wins!")
            return True
        elif playerPiece < 3 or cpuPiece < 3:
            playerPiece = 0
            cpuPiece = 0
        v+= 2

    d = 0
    e = 0

    while d < 5:
        if gameBoard[d][e] == "X":
            playerPiece +=1
        elif gameBoard[d][e] == "O":
            cpuPiece += 1
        if playerPiece == 3:
            print("Player Wins!")
            return True
        elif cpuPiece == 3:
            print("CPU Wins!")
            return True
        d+= 2
        e+= 2

    playerPiece = 0
    cpuPiece = 0

    z = 4
    b = 0
    while b < 5 :
        if gameBoard[z][b] == "X":
            playerPiece +=1
        elif gameBoard[z][b] == "O":
            cpuPiece +=1
        if playerPiece == 3:
            print("Player Wins!")
            return True
        elif cpuPiece == 3:
            print("CPU Wins1")
            return True
        z -= 2
        b += 2

    if countNumbers() == 0:
        print("Draw!")
        return True


def resumeGame():
    print("Continue")
    print("Y : Continue")
    print("N : Quit game")
    while True:
        decision = input()
        if decision.upper() == "Y" :
            return True
        elif decision.upper() == "N":
            return False
        else:
            print("Invalid input. Please enter the correct key")


def playGame():
    global gameBoard
    global playerChoice
    global cpuChoice
    printGameBoard()
    

    while True:
        playerTurns()
        printGameBoard()
        if checkGame():
            gameBoard = resetGameBoard()
            playerChoice = set()
            cpuChoice = set()
            break
        cpuTurns()
        printGameBoard()
        if checkGame():
            gameBoard = resetGameBoard()
            playerChoice = set()
            cpuChoice = set()
            break
    

playerChoice = set()
cpuChoice = set()
gameBoard =     [["1","|","2","|","3"],
                 ["-","+","-","+","-"],
                 ["4","|","5","|","6"],
                 ["-","+","-","+","-"],
                 ["7","|","8","|","9"]]
print("Welcome to a game of Tic Tac Toe")


playGame()

while True:
    if resumeGame():
        playGame()
    else:
        print("Thank you for playing")
        break











            






