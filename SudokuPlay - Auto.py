import pygame
import copy
from GeneratorandSolver import positionlist
from GeneratorandSolver import decidefull
from GeneratorandSolver import mixfirstrow
from GeneratorandSolver import checkvalid
from GeneratorandSolver import solvedboard
from GeneratorandSolver import positionlist
from GeneratorandSolver import userboard

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


pygame.font.init()

screen = pygame.display.set_mode((500,600))

pygame.display.set_caption("Sudoku Game")

x = 0
y = 0
dif = 500/9
val = 0
solved = solvedboard(board)
grid = userboard(copy.deepcopy(solved))

font = pygame.font.SysFont("comicsans", 35)
def postogrid(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif

def drawgrid():
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                pygame.draw.rect(screen, (173,216,230), (i * dif, j * dif, dif+1, dif+1))
                text1 = font.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))
    for i in range(10):
        if i % 3 == 0 :
            thick = 3
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)        

def enterval(val):
    enter = font.render(str(val), 1, (0,0,0))
    screen.blit(enter, (x*dif+15, y*dif+15))

def highlight():
    for i in range(2):
        pygame.draw.line(screen, (24,116,205), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 5)
        pygame.draw.line(screen, (24,116,205), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 5)

def error_wrong():
    warning = font.render("Wrong Answer", 1, (0,0,0))
    screen.blit(warning, (10, 520))

def error_invalid():
    warning = font.render("Invalid", 1, (0,0,0))
    screen.blit(warning, (10, 520))

def finish_message():
    warning = font.render("Done", 1, (0,0,0))
    screen.blit(warning, (10, 520))

def solve(board):
    if decidefull(board) == True:
        return True
    else:
        i ,j = decidefull(board)
        for n in range(1, 10):
            text = font.render(str(n), 1, (0,0,0))
            screen.blit(text, (i * dif + 15, j * dif + 15))
            pygame.display.update()
            pygame.time.delay(80)
            if checkvalid(board, n, (i, j)):
                board[i][j] = n
                if solve(board):
                    return board
                board[i][j] = 0
            pygame.draw.rect(screen, (255,255,255), (i * dif, j * dif, dif+1, dif+1))
            for n in range(10):
                if n % 3 == 0 :
                    thick = 3
                else:
                    thick = 1
                pygame.draw.line(screen, (0, 0, 0), (0, n * dif), (500, n * dif), thick)
                pygame.draw.line(screen, (0, 0, 0), (n * dif, 0), (n * dif, 500), thick)
    return False

                
while True:
    screen.fill((255,255,255))
    drawgrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            postogrid(pos)
            highlight()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                val = 1
            elif event.key == pygame.K_2:
                val = 2
            elif event.key == pygame.K_3:
                val = 3
            elif event.key == pygame.K_4:
                val = 4
            elif event.key == pygame.K_5:
                val = 5
            elif event.key == pygame.K_6:
                val = 6
            elif event.key == pygame.K_7:
                val = 7
            elif event.key == pygame.K_8:
                val = 8
            elif event.key == pygame.K_9:
                val = 9
            elif event.key == pygame.K_0:
                solve(grid)
            elif event.key == pygame.K_DELETE:
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
                solved = solvedboard(board)
                grid = userboard(copy.deepcopy(solved))
            else:
                error_invalid()
        if val != 0:
            enterval(val)
            if grid[int(x)][int(y)] == 0:
                if val == solved[int(x)][int(y)]:
                    grid[int(x)][int(y)] = val
                else:
                    grid[int(x)][int(y)] = 0
                    error_wrong()
            val = 0
        if grid == solved:
            finish_message()
        pygame.display.update()

pygame.quit()
