# Team: 8-bit
# Members: Mason, David, Casey, Logan

# importing pygame
import pygame
# importing random
import random

# fonts for the words printed to the screen
pygame.font.init()

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

X = [['.....',
      '..0..',
      '.000.',
      '..0..',
      '.....']]


# parallel list of shapes and their colors
shapes = [S, Z, I, O, J, L, T, X]
shape_colors = ["blue", "cyan", "orange", "yellow", "purple", "white", "red", "pink"]

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

# check to see if the space can be used
def openSpace(shape, grid):
    allowedPositions = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    allowedPositions = [j for sub in allowedPositions for j in sub]
    formatted = rotateShape(shape)
 
    for pos in formatted:
        if pos not in allowedPositions:
            if pos[1] > -1:
                return False
 
    return True
 
# see if the shape is missing
def shapeCheck(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

# one of the shapes and its color
def getShape():
    global shapes, shape_colors
 
    return Piece(5, 0, random.choice(shapes))

# defines the next shape to be sent
def makeNextShape(shape):
    sx = upperLeftX + gridWidth + 50
    sy = upperLeftY + gridHeight/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]
 
    for i, line in enumerate(format):
        row = list(line)

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


# defining the grid
def makeGrid(setPieces={}):
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]
 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in setPieces:
                c = setPieces[(j,i)]
                grid[i][j] = c
    return grid
 
# create the grid that was defined
def showGrid(surface, row, col):
    sx = upperLeftX
    sy = upperLeftY
    for i in range(row):
        # creates horizontal lines
        pygame.draw.line(surface, (128,128,128), (sx, sy+ i*30), (sx + gridWidth, sy + i * 30))  
        for j in range(col):
            # creates vertical lines
            pygame.draw.line(surface, (128,128,128), (sx + j * 30, sy), (sx + j * 30, sy + gridHeight))  

# remove blocks after a row is filled
def clearBlocks(grid, piecesSet, currentScore):

    score = currentScore
    counter1 = 0
    for i in range(len(grid)-1,-1,-1):
        row = grid[i]
        if (0, 0, 0) not in row:
            counter1 += 1
            # pieces get removed from setPieces
            counter2 = i
            for j in range(len(row)):
                try:
                    del piecesSet[(j, i)]
                    # incrementation to the current score
                    score += 10
                except:
                    continue

    # moves the pieces down after the row below them is cleared
    if counter1 > 0:
        for key in sorted(list(piecesSet), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < counter2:
                newKey = (x, y + counter1)
                piecesSet[newKey] = piecesSet.pop(key)
            

    return score

# define the window
def createWindow(surface, score, hScore):
    surface.fill("black")

    # Tetris Title
    font = pygame.font.SysFont('timesnewroman', 60)
    label = font.render('TETRIS', 1, "red")
    surface.blit(label, (upperLeftX + gridWidth / 2 - (label.get_width() / 2), 30))

    # the words "High Score" on screen
    font = pygame.font.SysFont('timesnewroman', 30)
    label = font.render('High Score', 1, "orange")
    surface.blit(label, (upperLeftX + gridWidth + (label.get_width() /2), 30))

    # the high score as a number on the screen
    font = pygame.font.SysFont('timesnewroman', 30)
    label = font.render(str(hScore), 1, "white")
    surface.blit(label, (upperLeftX + 370, 60))

    # the words "Your Score" on screen
    font = pygame.font.SysFont('timesnewroman', 30)
    label = font.render('Your Score', 1, "orange")
    surface.blit(label, (upperLeftX  - (label.get_width() *1.5), 30))

    # the current score as a number on the screen
    font = pygame.font.SysFont('timesnewroman', 30)
    label = font.render(str(score), 1, "white")
    surface.blit(label, (upperLeftX  - 200, 60))
 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (upperLeftX + j* 30, upperLeftY + i * 30, 30, 30), 0)
 
    # create grid
    showGrid(surface, 20, 10)
    pygame.draw.rect(surface, "white", (upperLeftX, upperLeftY, gridWidth, gridHeight), 5)

# initializing the high score
highScore = 0



# the main function which houses the game loop
def main():
    
    global grid
    global highScore

    # pieces that won't move
    setPieces = {}
    grid = makeGrid(setPieces)
 
    changePiece = False
    run = True
    movingPiece = getShape()
    newPiece = getShape()
    clock = pygame.time.Clock()
    dropTime = 0
    currentScore = 0
    
 
    while run:
        dropSpeed = 0.3
 
        grid = makeGrid(setPieces)
        dropTime += clock.get_rawtime()
        clock.tick()
 
        # falling pieces
        if dropTime/1000 >= dropSpeed:
            dropTime = 0
            movingPiece.y += 1
            if not (openSpace(movingPiece, grid)) and movingPiece.y > 0:
                movingPiece.y -= 1
                changePiece = True
        # code involving player input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movingPiece.x -= 1
                    if not openSpace(movingPiece, grid):
                        movingPiece.x += 1
 
                elif event.key == pygame.K_RIGHT:
                    movingPiece.x += 1
                    if not openSpace(movingPiece, grid):
                        movingPiece.x -= 1
                elif event.key == pygame.K_UP:
                    # rotate shape
                    movingPiece.rotation = movingPiece.rotation + 1 % len(movingPiece.shape)
                    if not openSpace(movingPiece, grid):
                        movingPiece.rotation = movingPiece.rotation - 1 % len(movingPiece.shape)

        position = rotateShape(movingPiece)

        # add the moving piece to the grid
        for i in range(len(position)):
            x, y = position[i]
            if y > -1:
                grid[y][x] = movingPiece.color
 
        # contact with bottom
        if changePiece:
            for pos in position:
                p = (pos[0], pos[1])
                setPieces[p] = movingPiece.color
            movingPiece = newPiece
            newPiece = getShape()
            changePiece = False

            # clearing of blocks called here (also updates score)
            currentScore = clearBlocks(grid, setPieces, currentScore)

        
        createWindow(win, currentScore, highScore)
        makeNextShape(newPiece)
        pygame.display.update()
 
        # Check if user lost
        if shapeCheck(setPieces):
            run = False
            
    # update the high score
    if (currentScore > highScore):
        highScore = currentScore

    # game over message
    font = pygame.font.SysFont('timesnewroman', 40, bold=True)
    label = font.render("Game Over", 1, "green")
    win.blit(label, (upperLeftX + gridWidth/2 - (label.get_width() / 2), upperLeftY + gridHeight/2 - label.get_height()/2))


    pygame.display.update()
    pygame.time.delay(2000)


win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Tetris')


startingScreen()  # start game
        
