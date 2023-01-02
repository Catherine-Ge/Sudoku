import pygame
import copy
from GeneratorandSolver import positionlist
from GeneratorandSolver import decidefull
from GeneratorandSolver import mixfirstrow
from GeneratorandSolver import checkvalid
from GeneratorandSolver import fill
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
    for i in range(10):
        thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                text1 = font.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))

def enterval(val):
    enter = font.render(str(val), 1, (0,0,0))
    screen.blit(enter, (x*dif+15, y*dif+15))

def error_wrong():
    warning = font.render("Wrong Answer", 1, (0,0,0))
    screen.blit(warning, (10, 520))

def error_invalid():
    warning = font.render("Invalid", 1, (0,0,0))
    screen.blit(warning, (10, 520))

def finish_message():
    warning = font.render("Done", 1, (0,0,0))
    screen.blit(warning, (10, 520))
                
while True:
    screen.fill((255,255,255))
    drawgrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            postogrid(pos)
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
            else:
                error_invalid()
        if val != 0:
            enterval(val)
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
            








































