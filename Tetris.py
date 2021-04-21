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

# rotating shapes
def rotateShape(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]
 
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))
 
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
 
    return positions


# display the given message (Used for game over)
def message(text, size, color, surface):
    font = pygame.font.SysFont('timesnewroman', size, bold=True)
    label = font.render(text, 1, color)
 
    surface.blit(label, (upperLeftX + gridWidth/2 - (label.get_width() / 2), upperLeftY + gridHeight/2 - label.get_height()/2))

# start screen that awaits input to begin the game
def titleScreen(text, size, color, surface):
    font = pygame.font.SysFont('timesnewroman', size)
    label = font.render(text, 1, color)
 
    surface.blit(label, (upperLeftX + gridWidth/2 - (label.get_width() / 2), upperLeftY + gridHeight/2 - label.get_height()/2))

# displaying the title screen
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

# highscore and current score initialization
highscore = 0
currentScore = 0

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

# define the window
def createWindow(surface):
    surface.fill("black")
    # Tetris Title
    font = pygame.font.SysFont('timesnewroman', 60)
    label = font.render('TETRIS', 1, "red")
 
    surface.blit(label, (upperLeftX + gridWidth / 2 - (label.get_width() / 2), 30))
 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (upperLeftX + j* 30, upperLeftY + i * 30, 30, 30), 0)
 
    # create grid
    showGrid(surface, 20, 10)
    pygame.draw.rect(surface, "white", (upperLeftX, upperLeftY, gridWidth, gridHeight), 5)


# section of code devoted to input from buttons
        

#create window
window = Tk()
window.title("Tetris")



window.mainloop()
