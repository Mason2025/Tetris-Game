# Team: 8-bit
# Members: Mason, David, Casey, Logan

# importing Tkinter's methods and variables
from tkinter import *
# importing random
import random



shapes = {"Square":[(-1,-1),(0,-1),(0,0),(-1,0)]}
shapeColor = {"Square":"blue"}


# start screen that awaits input to begin the game

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

# the layout of the grid
class GridSystem(Canvas):

    def __init__(self, master):
        Canvas.__init__(self, master)
        self.pack(expand=1, fill=BOTH)

    def plotGrid(self):
        i = 20
        y = 40
        # 1
        while (i > 0):
            # creates a block to be seen
            self.create_rectangle(20, 20, 40, y, outline = "black", fill = "")
            # registers that block in blockList
            blockList.append(Block(20, 20, 40, y))
            y += 20
            i -=1
        i = 20
        y = 40
        # 2
        while (i > 0):
            self.create_rectangle(40, 20, 60, y, outline = "black", fill = "")
            blockList.append(Block(40, 20, 60, y))
            y += 20
            i -=1
        i = 20
        y = 40
        # 3
        while (i > 0):
            self.create_rectangle(60, 20, 80, y, outline = "black", fill = "")
            blockList.append(Block(60, 20, 80, y))
            y += 20
            i -=1
        i = 20
        y = 40
        # 4
        while (i > 0):
            self.create_rectangle(80, 20, 100, y, outline = "black", fill = "")
            blockList.append(Block(80, 20, 100, y))
            y += 20
            i -=1
        i = 20
        y = 40
        # 5
        while (i > 0):
            self.create_rectangle(100, 20, 120, y, outline = "black", fill = "")
            blockList.append(Block(100, 20, 120, y))
            y += 20
            i -=1
        i = 20
        y = 40
        # 6
        while (i > 0):
            self.create_rectangle(120, 20, 140, y, outline = "black", fill = "")
            blockList.append(Block(120, 20, 140, y))
            y += 20
            i -=1
        i = 20
        y = 40
        # 7
        while (i > 0):
            self.create_rectangle(140, 20, 160, y, outline = "black", fill = "")
            blockList.append(Block(140, 20, 160, y))
            y += 20
            i -=1
        i = 20
        y = 40
        # 8
        while (i > 0):
            self.create_rectangle(160, 20, 180, y, outline = "black", fill = "")
            blockList.append(Block(160, 20, 180, y))
            y += 20
            i -=1
        i = 20
        y = 40
        # 9
        while (i > 0):
            self.create_rectangle(180, 20, 200, y, outline = "black", fill = "")
            blockList.append(Block(180, 20, 200, y))
            y += 20
            i -=1
        i = 20
        y = 40
        # 10
        while (i > 0):
            self.create_rectangle(200, 20, 220, y, outline = "black", fill = "")
            blockList.append(Block(200, 20, 220, y))
            y += 20
            i -=1
            
    # colors a block
    def colorBlock(self, x1, y1, x2, y2, color):
        blockList[1].blockColor = color
        self.create_rectangle(x1, y1, x2, y2, outline = "black", fill = color)
    

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
s.colorBlock(blockList[1].blockX1, blockList[1].blockY1,
             blockList[1].blockX2, blockList[1].blockY2 - 20, "red")


window.mainloop()
