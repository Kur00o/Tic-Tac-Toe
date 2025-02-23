import math
board = [" " for i in range (9)]

move = input("Select your character 1)X or 2)O: ")
if move == "X" or move == "x":
    pmove = "X"
    bmove = "O"
elif move == "O" or move == "o":
    pmove = "O"
    bmove = "X"
else:
    print("Wrong symbol")

def printboard():
    for i in range(0,9,3):
        print(f'|{board[i]}_|_{board[i+1]}_|_{board[i+2]}|')

def boardfull():
    return " " not in board

def checkwin(player):
    conds = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for j in conds:
        if board[j[0]] == board[j[1]] == board[j[2]] == player:
            return True
    return False

def bestmove():
    bestscore = -math.inf
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = bmove
            score = minimax(False)
            board[i] = " "
            if score > bestscore:
                best_score = score
                move = i
    return move

def minimax(maxing):
    if checkwin(bmove):
        return 1
    elif checkwin(pmove):
        return -1
    elif boardfull():
        return 0

    if maxing:
        bestscore = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = bmove
                score = minimax(False)
                board[i] = " "
                bestscore = max(score, bestscore)
        return bestscore
    else:
        bestscore = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = pmove
                score = minimax(True)
                board[i] = " "
                bestscore = min(score, bestscore)
        return bestscore

def user():
    while True:    
        chal = int(input("Enter a move between (1-9)- ")) - 1
        if chal>9 or chal<0:
            print("Wrong Move")
        elif board[chal] != " ":
            print("Not an empty slot")
        else:
            board[chal] = pmove
            break

print("Your board is \n|1_|_2_|_3| \n|4_|_5_|_6| \n|7_|_8_|_9|")

while True:
    user()
    printboard()

    if checkwin(pmove):
        print("You win")
        break
    elif boardfull():
        print("It's a tie!")
        break

    print("Bot palying...")
    ai_move = bestmove()
    board[ai_move] = bmove
    printboard()

    if checkwin(bmove):
        print("Bot wins!")
        break
    elif boardfull():
        print("It's a tie!")
        break