# Team: 8-bit
# Members: Mason, David, Casey, Logan

# importing pygame
import pygame
# importing random
import random

# global variables
# parameters for the screen and grid
screenWidth = 800
screenHeight = 700
gridWidth = 300  
gridHeight = 600  
blockSize = 30
upperLeftX = (screenWidth - gridWidth) // 2
upperLeftY = screenHeight - gridHeight

# shapes and rotations
 
S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]
 
Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]
 
I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
 
O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
 
J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]
 
L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]
 
T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]


# parallel list of shapes and their colors
shapes = [S, Z, I, O, J, L, T]
shape_colors = ["blue", "cyan", "orange", "yellow", "purple", "white", "red"]

# the pieces in play
class Piece(object):
    # y
    rows = 20
    # x
    columns = 10  
 
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0


# start screen that awaits input to begin the game
def startingScreen():
    run = True
    while run:
        win.fill((0,0,0))
        titleScreen('Press to start!', 80, "red", win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
 
            if event.type == pygame.KEYDOWN:
                main()
    pygame.quit()

# screen that displays highscore and current score, waits for input to play again

# Class for the game

class Game(Frame):

    def __init__(self, parent):
        Frame.__init__(self,parent)

# highscore and current score initialization
highscore = 0
currentScore = 0

# tracks the locations of the blocks in the grid
blockList = []

# defining the grid
def makeGrid(setPieces={}):
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]
 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in setPieces:
                c = setPieces[(j,i)]
                grid[i][j] = c
    return grid
 
# create the grid taht was defined
def showGrid(surface, row, col):
    sx = upperLeftX
    sy = upperLeftY
    for i in range(row):
        pygame.draw.line(surface, (128,128,128), (sx, sy+ i*30), (sx + gridWidth, sy + i * 30))  # horizontal lines
        for j in range(col):
            pygame.draw.line(surface, (128,128,128), (sx + j * 30, sy), (sx + j * 30, sy + gridHeight))  # vertical lines

# section of code devoted to input from buttons
        

# classes for different shapes
class Block():

    # default block color
    blockColor = ""
    
    
    # Block constructor
    def __init__(self, x1, y1, x2, y2):
        # default block coordinates
        self.blockX1 = 0
        self.blockY1 = 0
        self.blockX2 = 0
        self.blockY2 = 0
        # new block coordinates
        self.blockX1 = x1
        self.blockY1 = y1
        self.blockX2 = x2
        self.blockY2 = y2

    # decorators for block coordinates
    @property
    def blockX1(self):
        return self._blockX1
    
    @blockX1.setter
    def blockX1(self, value):
        self._blockX1 = value

    @property
    def blockY1(self):
        return self._blockY1
    
    @blockY1.setter
    def blockY1(self, value):
        self._blockY1 = value

    @property
    def blockX2(self):
        return self._blockX2
    
    @blockX2.setter
    def blockX2(self, value):
        self._blockX2 = value

    @property
    def blockY2(self):
        return self._blockY2
    
    @blockY2.setter
    def blockY2(self, value):
        self._blockY2 = value
        
    #def moveDown(self):
        
    #def moveLeft(self):

    #def moveright(self):

    #def rotate(self):
        
#create window
window = Tk()
window.title("Tetris")

# creating the grid
s = GridSystem(window)

s.plotGrid()

# colors a block
s.colorBlock(5, blockList[5].blockX1, blockList[5].blockY1,
             blockList[5].blockX2, blockList[5].blockY2 - 20, "red")




window.mainloop()
