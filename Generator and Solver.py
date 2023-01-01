import random

board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

#returns True if the board is full
def decidefull(board):
    for i in range(len(board)):
         for j in range(len(board[0])):
             if board[i][j] == 0:
                 return (i, j)
    return True
        
#returns a board with a mix first row
#without this function, the first row of our solved board can only be [0--9]
def mixfirstrow(board):
    random.shuffle(board[0])
    return board

#returns True if it is valid to place number at coordinates
def checkvalid(board, number, coordinates):
    for x in range(len(board[0])):
        if number == board[coordinates[0]][x] and coordinates[1] != x:
            return False
    for y in range(len(board)):
        if number == board[y][coordinates[1]] and coordinates[0] != y:
            return False
    boxx = coordinates[1]//3
    boxy = coordinates[0]//3
    for i in range(boxy*3, boxy*3+3):
        for j in range(boxx*3, boxx*3+3):
            if board[i][j] == number and (i,j) != coordinates:
                return False
    return True

#returns a valid soduko solution
#the first row is [0-9]
def fill(board):
    find = decidefull(board)
    if find == True:
        return True
    else:
        i, j = find
    for n in range(1,10):
        if checkvalid(board, n, find):
            board[i][j] = n
            if fill(board):
                return board
            board[i][j] = 0
    return False

#returns a valid soduko solution
#the first row is not [0--9]
def solvedboard(board):
    board[0] = [1,2,3,4,5,6,7,8,9]
    mixfirstrow(board)
    fill(board)
    return board

#returns a list of possible positions of the board
def positionlist():
    position=[]
    i = 0
    j = 0
    while i < 9:
        while j < 9:
            position.append([i,j])
            j = j + 1
        i = i + 1
        j = 0
    return position

#returns a soduko board with empty positions for the user to fill
def userboard(board):
    position = positionlist()
    wtf = random.randrange(75)
    while wtf > 0:
        zeroposition = random.choice(position)
        board[zeroposition[0]][zeroposition[1]] = 0
        wtf = wtf - 1
    return board

























