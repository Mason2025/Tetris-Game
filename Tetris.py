import pygame
import random

# defining the window in pygame
win = pygame.display.set_mode((480, 800))
# captioning the window
pygame.display.set_caption('Tetris')

# fonts for the words printed to the screen
pygame.font.init()

# creating the list of pieces that won't move
frozenPieces = []

# list of the blocks comprising the pieces that won't move
blockList = []

# the current piece with its coordiantes
currentPiece = []

# variable all pieces use
stack = False


class Block():


    def __init__(self, win, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    

    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, 20, 20))

    


# pieces that won't move        
class GamePiece():
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    x3 = 0
    y3 = 0
    x4 = 0
    y4 = 0


    # constructor
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4, win, color, i, j):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.win = win
        self.color = color

        self.blocksInPiece = []
        
        self.blocksInPiece.append(Block(win, color, x1, y1))

        self.blocksInPiece.append(Block(win, color, x2, y2))

        self.blocksInPiece.append(Block(win, color, x3, y3))

        self.blocksInPiece.append(Block(win, color, x4, y4))

    

    

    

    # creates an instance of Block
    def createBlocks(self):
        

        for b in range(len(self.blocksInPiece)):
            blockList.append(self.blocksInPiece[b])

    def deleteBlock(self, y):
        tbc = []

        for a in range(len(self.blocksInPiece)):
            if(self.blocksInPiece[a].y == y):
                tbc.append(self.blocksInPiece[a])
        
        for b in range(len(tbc)):
            self.blocksInPiece.remove(tbc[b])
            


# defining and drawing the grid
def grid(win):
            

    drawnBlocks = []

    global blockList
    
    # drawing all pieces that won't move
    for b in range(len(blockList)):
        blockList[b].draw()
        drawnBlocks.append(blockList[b])

    blockList = []

    for db in range(len(drawnBlocks)):
        blockList.append(drawnBlocks[db])
    
    
    # creating rows
    i = 0
    j = 0
    while(i < 20):
        pygame.draw.line(win, (128,128,128), (100, 220 + j), (300, 220 + j))        
        i += 1
        j += 20

    # creating columns
    i = 0
    j = 0
    while(i < 10):
        pygame.draw.line(win, (128,128,128), (100 + j, 200), (100 + j, 600))        
        i += 1
        j += 20
    # border for the grid
    pygame.draw.rect(win, (255, 255, 255), (100, 200, 200, 400), 2)

    # block that obscures next pieces
    pygame.draw.rect(win, (0, 0, 0), (100, 0, 200, 200), 0)

# pieces can stack
def contactV(win, px1, py1, px2, py2, px3, py3, px4, py4, color):

    for block in range(len(blockList)):
        if(blockList[block].x == px1 and blockList[block].y == py1 + 20):
            return True
        if(blockList[block].x == px2 and blockList[block].y == py2 + 20):
            return True
        if(blockList[block].x == px3 and blockList[block].y == py3 + 20):
            return True
        if(blockList[block].x == px4 and blockList[block].y == py4 + 20):
            return True

    return False


# stops pieces from moving sidways into eachother
def contactS(win, px1, py1, px2, py2, px3, py3, px4, py4):

    for block in range(len(blockList)):
        if(blockList[block].x == px1 + 20 and blockList[block].y == py1):
            return 2
        if(blockList[block].x == px2 + 20 and blockList[block].y == py2):
            return 2
        if(blockList[block].x == px3 + 20 and blockList[block].y == py3):
            return 2
        if(blockList[block].x == px4 + 20 and blockList[block].y == py4):
            return 2


        if(blockList[block].x == px1 - 20 and blockList[block].y == py1):
            return 3
        if(blockList[block].x == px2 - 20 and blockList[block].y == py2):
            return 3
        if(blockList[block].x == px3 - 20 and blockList[block].y == py3):
            return 3
        if(blockList[block].x == px4 - 20 and blockList[block].y == py4):
            return 3
    return 1

# checks if the space is already housing a block
#currentPiece = [x1, y1, x2, y2, x3, y3, x4, y4]
def isFilled(currentPiece):

    for block in range(len(blockList)):
        if(blockList[block].x == currentPiece[0] and blockList[block].y == currentPiece[1]):
            return True
        if(blockList[block].x == currentPiece[2] and blockList[block].y == currentPiece[3]):
            return True
        if(blockList[block].x == currentPiece[4] and blockList[block].y == currentPiece[5]):
            return True
        if(blockList[block].x == currentPiece[6] and blockList[block].y == currentPiece[7]):
            return True
    
    return False



# the L Piece
def LPiece(win, i, j, r, c):

    border = 150

    global currentPiece

    if(r == 1 and j < border):
        border = LPieceR(win, i, j, r, c)
    elif(r == 2 and j < border + 20):
        border = LPieceR2(win, i, j, r, c)
    elif(r == 3 and j < border):
        border = LPieceR3(win, i, j, r, c)
        
    
    else:
        x = 100 + j
        y = 200 + i
        color = (25, 255, 255)
        

        # piece specifications
        if (x < 500):
            x1 = x  
            y1 = y
            pygame.draw.rect(win, color, (x, y, 20, 20))
            y += 20
            x2 = x
            y2 = y
            pygame.draw.rect(win, color, (x, y , 20, 20))
            y += 20
            x3 = x
            y3 = y
            pygame.draw.rect(win, color, (x , y , 20, 20))
            x += 20
            x4 = x
            y4 = y
            pygame.draw.rect(win, color, (x , y , 20, 20))

            # checking to see if the piece has touched anything#
            currentPiece = [x1, y1, x2, y2, x3, y3, x4, y4]
            if (c == 1):
                return isFilled(currentPiece)
            stack = contactV(win, x1, y1, x2, y2, x3, y3, x4, y4, color)
            contactedSide = contactS(win, x1, y1, x2, y2, x3, y3, x4, y4)

        
        # adding the piece to the frozen pieces
        if (stack or i == 340):
            if (isFilled(currentPiece)):
                y1 -= 20
                y2 -= 20
                y3 -= 20
                y4 -= 20
            frozenPieces.append(GamePiece(x1, y1, x2, y2, x3, y3, x4, y4, win, color, i, j))
            frozenPieces[len(frozenPieces) - 1].createBlocks()
            return [0]
        results = [border, contactedSide]

        return results

    return border

def LPieceR(win, i, j, r, c):

    x = 100 + j
    y = 200 + i
    color = (25, 255, 255)
    border = 130

    global currentPiece
    

    # piece specifications
    if (x < 500):
        y += 40
        x1 = x  
        y1 = y 
        pygame.draw.rect(win, color, (x, y, 20, 20))
        y -= 20
        x2 = x
        y2 = y
        pygame.draw.rect(win, color, (x, y , 20, 20))
        x += 20
        x3 = x
        y3 = y
        pygame.draw.rect(win, color, (x, y , 20, 20))
        x += 20
        x4 = x
        y4 = y
        pygame.draw.rect(win, color, (x , y , 20, 20))
        
        currentPiece = [x1, y1, x2, y2, x3, y3, x4, y4]
        if (c == 1):
            return isFilled(currentPiece)
        stack = contactV(win, x1, y1, x2, y2, x3, y3, x4, y4, color)
        contactedSide = contactS(win, x1, y1, x2, y2, x3, y3, x4, y4)

    
        if (stack or i == 340):
            if (isFilled(currentPiece)):
                y1 -= 20
                y2 -= 20
                y3 -= 20
                y4 -= 20
            frozenPieces.append(GamePiece(x1, y1, x2, y2, x3, y3, x4, y4, win, color, i, j))
            frozenPieces[len(frozenPieces) - 1].createBlocks()
            return [0]

    results = [border, contactedSide]

    return results

def LPieceR2(win, i, j, r, c):

    x = 100 + j
    y = 200 + i
    color = (25, 255, 255)
    border = 150

    global currentPiece
    
    # piece specifications
    if (x < 500):
        x1 = x  
        y1 = y 
        pygame.draw.rect(win, color, (x, y, 20, 20))
        x += 20
        x2 = x
        y2 = y
        pygame.draw.rect(win, color, (x, y , 20, 20))
        y += 20
        x3 = x
        y3 = y
        pygame.draw.rect(win, color, (x, y , 20, 20))
        y += 20
        x4 = x
        y4 = y
        pygame.draw.rect(win, color, (x , y , 20, 20))
        
        currentPiece = [x1, y1, x2, y2, x3, y3, x4, y4]
        if (c == 1):
            return isFilled(currentPiece)
        stack = contactV(win, x1, y1, x2, y2, x3, y3, x4, y4, color)
        contactedSide = contactS(win, x1, y1, x2, y2, x3, y3, x4, y4)

    
        if (stack or i == 340):
            if (isFilled(currentPiece)):
                y1 -= 20
                y2 -= 20
                y3 -= 20
                y4 -= 20
            frozenPieces.append(GamePiece(x1, y1, x2, y2, x3, y3, x4, y4, win, color, i, j))
            frozenPieces[len(frozenPieces) - 1].createBlocks()
            return [0]

    results = [border, contactedSide]

    return results

def LPieceR3(win, i, j, r, c):

    x = 100 + j
    y = 200 + i
    color = (25, 255, 255)
    border = 130

    global currentPiece
    
    # piece specifications
    if (x < 500):
        y += 40
        x1 = x  
        y1 = y 
        pygame.draw.rect(win, color, (x, y, 20, 20))
        x += 20
        x2 = x
        y2 = y
        pygame.draw.rect(win, color, (x, y , 20, 20))
        x += 20
        x3 = x
        y3 = y
        pygame.draw.rect(win, color, (x, y , 20, 20))
        y -= 20
        x4 = x
        y4 = y
        pygame.draw.rect(win, color, (x , y , 20, 20))
        
        currentPiece = [x1, y1, x2, y2, x3, y3, x4, y4]
        if (c == 1):
            return isFilled(currentPiece)
        stack = contactV(win, x1, y1, x2, y2, x3, y3, x4, y4, color)
        contactedSide = contactS(win, x1, y1, x2, y2, x3, y3, x4, y4)


    
        if (stack or i == 340):
            if (isFilled(currentPiece)):
                y1 -= 20
                y2 -= 20
                y3 -= 20
                y4 -= 20
            frozenPieces.append(GamePiece(x1, y1, x2, y2, x3, y3, x4, y4, win, color, i, j))
            frozenPieces[len(frozenPieces) - 1].createBlocks()
            return [0]

    results = [border, contactedSide]

    return results

# the J Piece
def JPiece(win, i, j, r, c):

    border = 150

    global currentPiece

    if(r == 1 and j < border):
        border = JPieceR(win, i, j, r, c)
    elif(r == 2 and j < border):
        border = JPieceR2(win, i, j, r, c)
    elif(r == 3 and j < border):
        border = JPieceR3(win, i, j, r, c)
    
    else:
        x = 100 + j
        y = 200 + i
        color = (0, 50, 255)
        

        # piece specifications
        if (x < 500):
            y += 40
            x1 = x  
            y1 = y
            pygame.draw.rect(win, color, (x, y, 20, 20))
            x += 20
            x2 = x
            y2 = y
            pygame.draw.rect(win, color, (x, y , 20, 20))
            y -= 20
            x3 = x
            y3 = y
            pygame.draw.rect(win, color, (x , y , 20, 20))
            y -= 20
            x4 = x
            y4 = y
            pygame.draw.rect(win, color, (x , y , 20, 20))

            currentPiece = [x1, y1, x2, y2, x3, y3, x4, y4]
            if (c == 1):
                return isFilled(currentPiece)
            # checking to see if the piece has touched anything#
            stack = contactV(win, x1, y1, x2, y2, x3, y3, x4, y4, color)
            contactedSide = contactS(win, x1, y1, x2, y2, x3, y3, x4, y4)

        
            # adding the piece to the frozen pieces
        if (stack or i == 340):
            if (isFilled(currentPiece)):
                y1 -= 20
                y2 -= 20
                y3 -= 20
                y4 -= 20
            frozenPieces.append(GamePiece(x1, y1, x2, y2, x3, y3, x4, y4, win, color, i, j))
            frozenPieces[len(frozenPieces) - 1].createBlocks()
            return [0]
        results = [border, contactedSide]

        return results

    return border

def JPieceR(win, i, j, r, c):

    x = 100 + j
    y = 200 + i
    color = (0, 50, 255)
    border = 130

    global currentPiece
    

    # piece specifications
    if (x < 500):
        y += 20
        x1 = x  
        y1 = y 
        pygame.draw.rect(win, color, (x, y, 20, 20))
        y += 20
        x2 = x
        y2 = y
        pygame.draw.rect(win, color, (x, y , 20, 20))
        x += 20
        x3 = x
        y3 = y
        pygame.draw.rect(win, color, (x, y , 20, 20))
        x += 20
        x4 = x
        y4 = y
        pygame.draw.rect(win, color, (x , y , 20, 20))
        
        currentPiece = [x1, y1, x2, y2, x3, y3, x4, y4]
        if (c == 1):
            return isFilled(currentPiece)
        stack = contactV(win, x1, y1, x2, y2, x3, y3, x4, y4, color)
        contactedSide = contactS(win, x1, y1, x2, y2, x3, y3, x4, y4)

    
        if (stack or i == 340):
            if (isFilled(currentPiece)):
                y1 -= 20
                y2 -= 20
                y3 -= 20
                y4 -= 20
            frozenPieces.append(GamePiece(x1, y1, x2, y2, x3, y3, x4, y4, win, color, i, j))
            frozenPieces[len(frozenPieces) - 1].createBlocks()
            return [0]

    results = [border, contactedSide]

    return results

def JPieceR2(win, i, j, r, c):

    x = 100 + j
    y = 200 + i
    color = (0, 50, 255)
    border = 130

    global currentPiece
    
    # piece specifications
    if (x < 500):
        y += 40
        x1 = x  
        y1 = y 
        pygame.draw.rect(win, color, (x, y, 20, 20))
        y -= 20
        x2 = x
        y2 = y
        pygame.draw.rect(win, color, (x, y , 20, 20))
        y -= 20
        x3 = x
        y3 = y
        pygame.draw.rect(win, color, (x, y , 20, 20))
        x += 20
        x4 = x
        y4 = y
        pygame.draw.rect(win, color, (x , y , 20, 20))
        
        currentPiece = [x1, y1, x2, y2, x3, y3, x4, y4]
        if (c == 1):
            return isFilled(currentPiece)
        stack = contactV(win, x1, y1, x2, y2, x3, y3, x4, y4, color)
        contactedSide = contactS(win, x1, y1, x2, y2, x3, y3, x4, y4)

    
        if (stack or i == 340):
            if (isFilled(currentPiece)):
                y1 -= 20
                y2 -= 20
                y3 -= 20
                y4 -= 20
            frozenPieces.append(GamePiece(x1, y1, x2, y2, x3, y3, x4, y4, win, color, i, j))
            frozenPieces[len(frozenPieces) - 1].createBlocks()
            return [0]

    results = [border, contactedSide]

    return results

def JPieceR3(win, i, j, r, c):

    x = 100 + j
    y = 200 + i
    color = (0, 50, 255)
    border = 130

    global currentPiece
    
    # piece specifications
    if (x < 500):
        y += 20
        x1 = x  
        y1 = y 
        pygame.draw.rect(win, color, (x, y, 20, 20))
        x += 20
        x2 = x
        y2 = y
        pygame.draw.rect(win, color, (x, y , 20, 20))
        x += 20
        x3 = x
        y3 = y
        pygame.draw.rect(win, color, (x, y , 20, 20))
        y += 20
        x4 = x
        y4 = y
        pygame.draw.rect(win, color, (x , y , 20, 20))
        
        currentPiece = [x1, y1, x2, y2, x3, y3, x4, y4]
        if (c == 1):
            return isFilled(currentPiece)
        stack = contactV(win, x1, y1, x2, y2, x3, y3, x4, y4, color)
        contactedSide = contactS(win, x1, y1, x2, y2, x3, y3, x4, y4)

    
        if (stack or i == 340):
            if (isFilled(currentPiece)):
                y1 -= 20
                y2 -= 20
                y3 -= 20
                y4 -= 20
            frozenPieces.append(GamePiece(x1, y1, x2, y2, x3, y3, x4, y4, win, color, i, j))
            frozenPieces[len(frozenPieces) - 1].createBlocks()
            return [0]

    results = [border, contactedSide]

    return results

# the O piece
def OPiece(win, i, j, r, c):

    border = 150

    x = 100 + j
    y = 200 + i
    color = (0, 0, 0)

    global currentPiece

    # piece specifications 
    if (x < 500):
        y += 20
        x1 = x
        y1 = y
        pygame.draw.rect(win, (0, 255, 0), (x, y, 20, 20))
        y += 20
        x2 = x
        y2 = y
        pygame.draw.rect(win, (0, 255, 0), (x, y , 20, 20))
        x += 20
        x3 = x
        y3 = y
        pygame.draw.rect(win, (0, 255, 0), (x , y , 20, 20))
        y -= 20
        x4 = x
        y4 = y
        pygame.draw.rect(win, (0, 255, 0), (x , y , 20, 20))
        x -= 20
        y -= 40

        currentPiece = [x1, y1, x2, y2, x3, y3, x4, y4]
        if (c == 1):
            return isFilled(currentPiece)
        stack = contactV(win, x1, y1, x2, y2, x3, y3, x4, y4, color)
        contactedSide = contactS(win, x1, y1, x2, y2, x3, y3, x4, y4)

        c = 0

    if (contactedSide == 1 and i != 340 and stack == False):
        y1 = y + c
        pygame.draw.rect(win, color, (x, y, 20, 20))
        y2 = y + c
        pygame.draw.rect(win, color, (x, y , 20, 20))
        y3 = y + c
        pygame.draw.rect(win, color, (x , y , 20, 20))
        y4 = y + c
        pygame.draw.rect(win, color, (x , y , 20, 20))
        c += 20

        stack = contactV(win, x1, y1, x2, y2, x3, y3, x4, y4, color)
        contactedSide = contactS(win, x1, y1, x2, y2, x3, y3, x4, y4)

    # adding the piece to the frozen pieces
    if (stack or i == 340):
        if (isFilled(currentPiece)):
                y1 -= 20
                y2 -= 20
                y3 -= 20
                y4 -= 20
        frozenPieces.append(GamePiece(x1, y1, x2, y2, x3, y3, x4, y4, win, (0, 255, 0), i, j))
        frozenPieces[len(frozenPieces) - 1].createBlocks()
        return [0]

    results = [border, contactedSide]
    return results
    

# the T piece
def TPiece(win, i, j, r, c):

    border = 130

    global currentPiece
    
    if(r == 1 and j < border + 40):
        border = TPieceR(win, i, j, r, c)
    elif(r == 2 and j < border + 40):
        border = TPieceR2(win, i, j, r, c)
    elif(r == 3 and j < border + 40):
        border = TPieceR3(win, i, j, r, c)

    else:
        x = 100 + j
        y = 200 + i
        color = (255, 0, 255)
        

        # piece specifications
        if (x < 500):
            y += 40
            x1 = x  
            y1 = y
            pygame.draw.rect(win, color, (x, y, 20, 20))
            y -= 20
            x += 20
            x2 = x
            y2 = y
            pygame.draw.rect(win, color, (x, y , 20, 20))
            y += 20
            x3 = x
            y3 = y
            pygame.draw.rect(win, color, (x , y , 20, 20))
            x += 20
            x4 = x
            y4 = y
            pygame.draw.rect(win, color, (x , y , 20, 20))

            currentPiece = [x1, y1, x2, y2, x3, y3, x4, y4]
            if (c == 1):
                return isFilled(currentPiece)
            # checking to see if the piece has touched anything#
            stack = contactV(win, x1, y1, x2, y2, x3, y3, x4, y4, color)
            contactedSide = contactS(win, x1, y1, x2, y2, x3, y3, x4, y4)

        
            # adding the piece to the frozen pieces
        if (stack or i == 340):
            if (isFilled(currentPiece)):
                y1 -= 20
                y2 -= 20
                y3 -= 20
                y4 -= 20
            frozenPieces.append(GamePiece(x1, y1, x2, y2, x3, y3, x4, y4, win, color, i, j))
            frozenPieces[len(frozenPieces) - 1].createBlocks()
            return [0]
        results = [border, contactedSide]

        return results

    return border

def TPieceR(win, i, j, r, c):

    x = 100 + j
    y = 200 + i
    color = (255, 0, 255)
    border = 150

    global currentPiece
    

    # piece specifications
    if (x < 500):
        y += 40
        x1 = x  
        y1 = y 
        pygame.draw.rect(win, color, (x, y, 20, 20))
        y -= 20
        x2 = x
        y2 = y
        pygame.draw.rect(win, color, (x, y , 20, 20))
        y -= 20
        x3 = x
        y3 = y
        pygame.draw.rect(win, color, (x, y , 20, 20))
        y += 20
        x += 20
        x4 = x
        y4 = y
        pygame.draw.rect(win, color, (x , y , 20, 20))
        
        currentPiece = [x1, y1, x2, y2, x3, y3, x4, y4]
        if (c == 1):
            return isFilled(currentPiece)
        stack = contactV(win, x1, y1, x2, y2, x3, y3, x4, y4, color)
        contactedSide = contactS(win, x1, y1, x2, y2, x3, y3, x4, y4)

    
        if (stack or i == 340):
            if (isFilled(currentPiece)):
                y1 -= 20
                y2 -= 20
                y3 -= 20
                y4 -= 20
            frozenPieces.append(GamePiece(x1, y1, x2, y2, x3, y3, x4, y4, win, color, i, j))
            frozenPieces[len(frozenPieces) - 1].createBlocks()
            return [0]

    results = [border, contactedSide]

    return results

def TPieceR2(win, i, j, r, c):

    x = 100 + j
    y = 200 + i
    color = (255, 0, 255)
    border = 130

    global currentPiece
    
    # piece specifications
    if (x < 500):
        y += 20
        x1 = x  
        y1 = y 
        pygame.draw.rect(win, color, (x, y, 20, 20))
        x += 20
        x2 = x
        y2 = y
        pygame.draw.rect(win, color, (x, y , 20, 20))
        y += 20
        x3 = x
        y3 = y
        pygame.draw.rect(win, color, (x, y , 20, 20))
        y -= 20
        x += 20
        x4 = x
        y4 = y
        pygame.draw.rect(win, color, (x , y , 20, 20))
        
        currentPiece = [x1, y1, x2, y2, x3, y3, x4, y4]
        if (c == 1):
            return isFilled(currentPiece)
        stack = contactV(win, x1, y1, x2, y2, x3, y3, x4, y4, color)
        contactedSide = contactS(win, x1, y1, x2, y2, x3, y3, x4, y4)

    
        if (stack or i == 340):
            if (isFilled(currentPiece)):
                y1 -= 20
                y2 -= 20
                y3 -= 20
                y4 -= 20
            frozenPieces.append(GamePiece(x1, y1, x2, y2, x3, y3, x4, y4, win, color, i, j))
            frozenPieces[len(frozenPieces) - 1].createBlocks()
            return [0]

    results = [border, contactedSide]

    return results

def TPieceR3(win, i, j, r, c):

    x = 100 + j
    y = 200 + i
    color = (255, 0, 255)
    border = 150

    global currentPiece
    
    # piece specifications
    if (x < 500):
        y += 20
        x1 = x  
        y1 = y 
        pygame.draw.rect(win, color, (x, y, 20, 20))
        x += 20
        x2 = x
        y2 = y
        pygame.draw.rect(win, color, (x, y , 20, 20))
        y += 20
        x3 = x
        y3 = y
        pygame.draw.rect(win, color, (x, y , 20, 20))
        y -= 40
        x4 = x
        y4 = y
        pygame.draw.rect(win, color, (x , y , 20, 20))
        
        currentPiece = [x1, y1, x2, y2, x3, y3, x4, y4]
        if (c == 1):
            return isFilled(currentPiece)
        stack = contactV(win, x1, y1, x2, y2, x3, y3, x4, y4, color)
        contactedSide = contactS(win, x1, y1, x2, y2, x3, y3, x4, y4)

    
        if (stack or i == 340):
            if (isFilled(currentPiece)):
                y1 -= 20
                y2 -= 20
                y3 -= 20
                y4 -= 20
            frozenPieces.append(GamePiece(x1, y1, x2, y2, x3, y3, x4, y4, win, color, i, j))
            frozenPieces[len(frozenPieces) - 1].createBlocks()
            return [0]

    results = [border, contactedSide]

    return results
        
# the ZPiece
def ZPiece(win, i, j, r, c):
    
    r = r % 2

    border = 150

    global currentPiece

    if(r == 1 and j < border):
        border = ZPieceR(win, i, j, r, c)

    else:
        x = 100 + j
        y = 200 + i
        color = (255, 255, 0)

        # piece specifications 
        if (x < 500):
            x1 = x
            y1 = y
            pygame.draw.rect(win, color, (x, y, 20, 20))
            y += 20
            x2 = x
            y2 = y
            pygame.draw.rect(win, color, (x, y , 20, 20))
            x += 20
            x3 = x
            y3 = y
            pygame.draw.rect(win, color, (x , y , 20, 20))
            y += 20
            x4 = x
            y4 = y
            pygame.draw.rect(win, color, (x , y , 20, 20))
            x -= 20
            y -= 40


            currentPiece = [x1, y1, x2, y2, x3, y3, x4, y4]
            if (c == 1):
                return isFilled(currentPiece)
            stack = contactV(win, x1, y1, x2, y2, x3, y3, x4, y4, color)
            contactedSide = contactS(win, x1, y1, x2, y2, x3, y3, x4, y4)

            c = 0

        if (contactedSide == 1 and i != 340 and stack == False):
            y1 = y + c
            pygame.draw.rect(win, color, (x, y, 20, 20))
            y2 = y + c
            pygame.draw.rect(win, color, (x, y , 20, 20))
            y3 = y + c
            pygame.draw.rect(win, color, (x , y , 20, 20))
            y4 = y + c
            pygame.draw.rect(win, color, (x , y , 20, 20))
            c += 20

            stack = contactV(win, x1, y1, x2, y2, x3, y3, x4, y4, color)
            contactedSide = contactS(win, x1, y1, x2, y2, x3, y3, x4, y4)

        if (stack or i == 340):
            if (isFilled(currentPiece)):
                y1 -= 20
                y2 -= 20
                y3 -= 20
                y4 -= 20
            frozenPieces.append(GamePiece(x1, y1, x2, y2, x3, y3, x4, y4, win, color, i, j))
            frozenPieces[len(frozenPieces) - 1].createBlocks()
            return [0]

        results = [border, contactedSide]
        return results

    return border

# rotation of the ZPiece
def ZPieceR(win, i, j, r, c):

    x = 100 + j
    y = 200 + i
    color = (255, 255, 0)
    border = 130

    global currentPiece

    # piece specifications
    if (x < 500):
        y += 40
        x1 = x  
        y1 = y 
        pygame.draw.rect(win, color, (x, y, 20, 20))
        x += 20
        x2 = x
        y2 = y
        pygame.draw.rect(win, color, (x, y , 20, 20))
        y -= 20
        x3 = x
        y3 = y
        pygame.draw.rect(win, color, (x, y , 20, 20))
        x += 20
        x4 = x
        y4 = y
        pygame.draw.rect(win, color, (x , y , 20, 20))
        x -= 40
        y -= 20


        currentPiece = [x1, y1, x2, y2, x3, y3, x4, y4]
        if (c == 1):
            return isFilled(currentPiece)
        stack = contactV(win, x1, y1, x2, y2, x3, y3, x4, y4, color)
        contactedSide = contactS(win, x1, y1, x2, y2, x3, y3, x4, y4)

    
        if (stack or i == 340):
            if (isFilled(currentPiece)):
                y1 -= 20
                y2 -= 20
                y3 -= 20
                y4 -= 20
            frozenPieces.append(GamePiece(x1, y1, x2, y2, x3, y3, x4, y4, win, color, i, j))
            frozenPieces[len(frozenPieces) - 1].createBlocks()
            return [0]

    results = [border, contactedSide]

    return results

# the SPiece
def SPiece(win, i, j, r, c):
    
    r = r % 2

    border = 150

    global currentPiece

    if(r == 1 and j < border):
        border = SPieceR(win, i, j, r, c)

    else:
        x = 100 + j
        y = 200 + i
        color = (0, 0, 0)

        # piece specifications
        if (x < 500):
            x += 20
            x1 = x
            y1 = y
            pygame.draw.rect(win, (255, 255, 255), (x, y, 20, 20))
            
            y += 20
            x2 = x
            y2 = y
            pygame.draw.rect(win, (255, 255, 255), (x, y , 20, 20))
            x -= 20
            x3 = x
            y3 = y
            pygame.draw.rect(win, (255, 255, 255), (x , y , 20, 20))
            
            y += 20
            x4 = x
            y4 = y
            pygame.draw.rect(win, (255, 255, 255), (x , y , 20, 20))
            y -= 40

            currentPiece = [x1, y1, x2, y2, x3, y3, x4, y4]
            if (c == 1):
                return isFilled(currentPiece)
            stack = contactV(win, x1, y1, x2, y2, x3, y3, x4, y4, color)
            contactedSide = contactS(win, x1, y1, x2, y2, x3, y3, x4, y4)
            
            c = 0

        if (contactedSide == 1 and i != 340 and stack == False):
            y1 = y + c
            pygame.draw.rect(win, color, (x, y, 20, 20))
            y2 = y + c
            pygame.draw.rect(win, color, (x, y , 20, 20))
            y3 = y + c
            pygame.draw.rect(win, color, (x , y , 20, 20))
            y4 = y + c
            pygame.draw.rect(win, color, (x , y , 20, 20))
            c += 20

            stack = contactV(win, x1, y1, x2, y2, x3, y3, x4, y4, color)
            contactedSide = contactS(win, x1, y1, x2, y2, x3, y3, x4, y4)

        if (stack or i == 340):
            if (isFilled(currentPiece)):
                y1 -= 20
                y2 -= 20
                y3 -= 20
                y4 -= 20
            frozenPieces.append(GamePiece(x1, y1, x2, y2, x3, y3, x4, y4, win, (255, 255, 255), i, j))
            frozenPieces[len(frozenPieces) - 1].createBlocks()
            return [0]

        results = [border, contactedSide]
        return results

    return border

# the S piece's rotation
def SPieceR(win, i, j, r, c):

    x = 100 + j
    y = 200 + i
    color = (255, 255, 255)
    border = 130

    global currentPiece

    # piece specifications
    if (x < 500):
        y += 40
        x1 = x  
        y1 = y - 20
        pygame.draw.rect(win, color, (x, y - 20, 20, 20))
        y -= 20
        x += 20
        x2 = x
        y2 = y
        pygame.draw.rect(win, color, (x, y , 20, 20))
        y += 20
        x3 = x
        y3 = y
        pygame.draw.rect(win, color, (x , y , 20, 20))
        x += 20
        x4 = x
        y4 = y
        pygame.draw.rect(win, color, (x , y , 20, 20))

        currentPiece = [x1, y1, x2, y2, x3, y3, x4, y4]
        if (c == 1):
            return isFilled(currentPiece)
        stack = contactV(win, x1, y1, x2, y2, x3, y3, x4, y4, color)
        contactedSide = contactS(win, x1, y1, x2, y2, x3, y3, x4, y4)

    
        if (stack or i == 340):
            if (isFilled(currentPiece)):
                y1 -= 20
                y2 -= 20
                y3 -= 20
                y4 -= 20
            frozenPieces.append(GamePiece(x1, y1, x2, y2, x3, y3, x4, y4, win, color, i, j))
            frozenPieces[len(frozenPieces) - 1].createBlocks()
            return [0]

    results = [border, contactedSide]

    return results

def IPiece(win, i, j, r, c):
    r = r % 2

    border = 170

    global currentPiece

    if(r == 1 and j < border - 40):
        border = IPieceR(win, i, j, r, c)
        pass
    
    else:
        x = 100 + j
        y = 200 + i
        color = (255, 0, 150)
        

        # piece specifications
        if (x < 500):
            y += 40
            x1 = x  
            y1 = y
            pygame.draw.rect(win, color, (x, y, 20, 20))
            y -= 20
            x2 = x
            y2 = y
            pygame.draw.rect(win, color, (x, y , 20, 20))
            y -= 20
            x3 = x
            y3 = y
            pygame.draw.rect(win, color, (x , y , 20, 20))
            y -= 20
            x4 = x
            y4 = y
            pygame.draw.rect(win, color, (x , y , 20, 20))

            currentPiece = [x1, y1, x2, y2, x3, y3, x4, y4]
            if (c == 1):
                return isFilled(currentPiece)
            # checking to see if the piece has touched anything#
            stack = contactV(win, x1, y1, x2, y2, x3, y3, x4, y4, color)
            contactedSide = contactS(win, x1, y1, x2, y2, x3, y3, x4, y4)

        
            # adding the piece to the frozen pieces
        if (stack or i == 340):
            if (isFilled(currentPiece)):
                y1 -= 20
                y2 -= 20
                y3 -= 20
                y4 -= 20
            frozenPieces.append(GamePiece(x1, y1, x2, y2, x3, y3, x4, y4, win, color, i, j))
            frozenPieces[len(frozenPieces) - 1].createBlocks()
            return [0]
        results = [border, contactedSide]

        return results

    return border

def IPieceR(win, i, j, r, c):

    x = 100 + j
    y = 200 + i
    color = (255, 0, 150)
    border = 115

    global currentPiece

    # piece specifications
    if (x < 500):
        y += 40
        x1 = x  
        y1 = y 
        pygame.draw.rect(win, color, (x, y , 20, 20))
        x += 20
        x2 = x
        y2 = y
        pygame.draw.rect(win, color, (x, y , 20, 20))
        x += 20
        x3 = x
        y3 = y
        pygame.draw.rect(win, color, (x , y , 20, 20))
        x += 20
        x4 = x
        y4 = y
        pygame.draw.rect(win, color, (x , y , 20, 20))

        currentPiece = [x1, y1, x2, y2, x3, y3, x4, y4]
        if (c == 1):
            return isFilled(currentPiece)
        stack = contactV(win, x1, y1, x2, y2, x3, y3, x4, y4, color)
        contactedSide = contactS(win, x1, y1, x2, y2, x3, y3, x4, y4)

    
        if (stack or i == 340):
            if (isFilled(currentPiece)):
                y1 -= 20
                y2 -= 20
                y3 -= 20
                y4 -= 20
            frozenPieces.append(GamePiece(x1, y1, x2, y2, x3, y3, x4, y4, win, color, i, j))
            frozenPieces[len(frozenPieces) - 1].createBlocks()
            return [0]

    results = [border, contactedSide]

    return results

tbc = []

class RectangleChecker():

    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n

    def scan(self):
        global yourScore
        # blocks to be cleared
        tbc = []
        s = 0
        v = 0
        for b in range(len(blockList)):
            if(self.y == blockList[b].y):
                tbc.append(blockList[b])
                v += 1
            if(v == 10):
                for p in range(len(tbc)):
                    if(tbc[p] in blockList):
                        blockList.remove(tbc[p])
                        s += 1

                for nb in range(len(blockList)):
                    if(blockList[nb].y < self.y):
                        blockList[nb].y += 20
                        
                yourScore += 100
                
                return True
                

def checker(win, n):

    checkers = []
    
    i = 0
    l = 0
    x = 100
    y = 200
    
    while(l < 20):
        pygame.draw.rect(win, (0, 0, 0), (x, y + i, 200, 20))
        x1 = x
        y1 = y + i
        rectangleC = RectangleChecker(x1, y1, n)
        checkers.append(rectangleC)
        i += 20
        l += 1

    for c in range(len(checkers)):
        deleted = checkers[c].scan()
                
# the list of pieces to draw next
pieceList = [ZPiece, TPiece, SPiece, OPiece, LPiece, JPiece, IPiece]

def gameOver():

    for piece in range(len(frozenPieces)):
        if(frozenPieces[piece].y2 <= 200):
            return True

    return False

# the function that fills the screen and calls the pieces
def screen(win, i, j, n, r, c):
    
    global yourScore
    global highScore
    
    win.fill((0,0,0))

    
    checker(win, n)

    borders = pieceList[n](win, i, j, r, c)

    #if (len(borders) < 2):
    borders.append(0)

    if(borders[0] == 0):
        borders.append(1)

    # creates the grid
    grid(win)

    # Title above the grid
    font = pygame.font.SysFont('timesnewroman', 40)
    label = font.render('TETRIS', 1, (255, 0, 0))
    win.blit(label, (135, 160))

    # high score
    font = pygame.font.SysFont('timesnewroman', 20)
    label = font.render('High Score', 1, (255, 125, 0))
    win.blit(label, (340, 320))
    
    # high score #
    font = pygame.font.SysFont('timesnewroman', 15)
    label = font.render(str(highScore), 1, (255, 255, 255))
    win.blit(label, (340, 350))
    
    # your score
    font = pygame.font.SysFont('timesnewroman', 20)
    label = font.render('Your Score', 1, (255, 125, 0))
    win.blit(label, (340, 400))

    # your score #
    font = pygame.font.SysFont('timesnewroman', 15)
    label = font.render(str(yourScore), 1, (255, 255, 255))
    win.blit(label, (340, 430))


    pygame.display.update()

    if (yourScore < 500):
        pygame.time.delay(400)
    elif (yourScore < 1000):
        pygame.time.delay(200)
    else:
        pygame.time.delay(50)

    return borders

# the main game Loop
def gameLoop():
    run = True
    
    font = pygame.font.SysFont('timesnewroman', 40)
    label = font.render('Press to start', 1, (255, 0, 0))
    win.blit(label, (130, 400))
    pygame.display.update()

    for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN):
    
                    while (run == True):
                        # variable setup
                        # positioning the next block in the middle above the grid
                        i = -60
                        j = 80
                        n = random.randint(0, 6)
                        #n = 4
                        r = 0
                        c = 0

                        while(True):
                            border = screen(win, i, j, n, r, c)
                            # player input checking
                            for event in pygame.event.get():
                                if (event.type == pygame.KEYDOWN):
                                    if (event.key == pygame.K_RIGHT and j < border[0] and i < 340):
                                        if (border[1] != 2):
                                            j += 20
                                    elif (event.key == pygame.K_LEFT and j > 0  and i < 340):
                                        if (border[1] != 3 ):
                                            j -= 20
                                    elif (event.key == pygame.K_UP):
                                        if (border[1] != 0):
                                            if (n == 1 and j > 150):
                                                if(r == 1 or r == 3):
                                                    r -= 1
                                            r += 1
                                            if (r >= 4):
                                                r = 0
                                            c = 1
                                            if (pieceList[n](win, i, j, r, c)):
                                                r -= 1
                                                if (r < 0):
                                                    r = 4
                                            c = 0
                                    elif (event.key == pygame.K_DOWN):
                                        run = False
                                        pygame.display.quit()
                                        quit()

                            # stops the movement of the current piece
                            if (i == 340 or border[0] == 0):
                                    break
                            # downwards movement of each piece
                            if (i < 340 and border[len(border) - 1] != 1):
                                i += 20
                                
                                    
                        if(gameOver() == True):
                            # Game Over message
                            font = pygame.font.SysFont('timesnewroman', 40, bold=True)
                            label = font.render("Game Over", 1, (255, 118, 30))
                            win.blit(label, (100, 400))
                            pygame.display.update()
                            pygame.time.delay(1000)
                            win.fill((0,0,0))
                            run = False
highScore = 0     
game = True            
while(game == True):
    
    yourScore = 0
    
    
    # the call for the game loop
    gameLoop()
    
    if(highScore < yourScore):
        highScore = yourScore

    # clear the grid of frozen pieces
    frozenPieces = []
    blockList = []


