def printboard(board):
    for i in range(len(board)):
        if i%3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j%3 == 0 and j!= 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def decidefull(board):
    for i in range(len(board)):
         for j in range(len(board[0])):
             if board[i][j] == 0:
                 return (i, j)
    return True

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
#refactoring, rewrite the code, requirements =, improve (efficiency, readable)
#secondary checker, local, break checker into three
#design pattern, forms: data structure, etc, common solutions to common problems, rather fixed, standard terms
#aritechure patters: large design patterns
#certain charateristsic -> fit well in a pattern
#anti-patterns: not to do for certain problems, solutions don't work (incorrect, inefficiency)
#adapt patterns, combine
#Book: "Design Patterns" by Gamma, Helm, Johnson, Vlissides.
#obersever: through changes, other parts need to be notified
#opendata, inspirations

def solve(board):
    find = decidefull(board)
    if find == True:
        return True
    else:
        i, j = find
    for n in range(1,10):
        board[i][j]=n
        #print(printboard(board))
        if checkvalid(board, n, find):
            board[i][j] = n
            if solve(board):
                return board
            board[i][j] = 0
    return False
        


print(printboard(solve(board)))

*helper 