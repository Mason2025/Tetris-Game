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

# the layout of the grid
class GridSystem(Canvas):

    def __init__(self, master):
        Canvas.__init__(self, master)
        self.pack(expand=1, fill=BOTH)

    def plotGrid(self):
        # the size of a block V
        # self.create_rectangle(20, 20, 40, 40, outline = "blue", fill = "")
        # outline for grid V
        #self.create_rectangle(20, 20, 200, 400, outline = "blue", fill = "")
        i = 20
        y = 40
        # 1
        while (i > 0):
            self.create_rectangle(20, 20, 40, y, outline = "blue", fill = "")
            y += 20
            i -=1
        i = 20
        y = 40
        # 2
        while (i > 0):
            self.create_rectangle(40, 20, 60, y, outline = "blue", fill = "")
            y += 20
            i -=1
        i = 20
        y = 40
        # 3
        while (i > 0):
            self.create_rectangle(60, 20, 80, y, outline = "blue", fill = "")
            y += 20
            i -=1
        i = 20
        y = 40
        # 4
        while (i > 0):
            self.create_rectangle(80, 20, 100, y, outline = "blue", fill = "")
            y += 20
            i -=1
        i = 20
        y = 40
        # 5
        while (i > 0):
            self.create_rectangle(100, 20, 120, y, outline = "blue", fill = "")
            y += 20
            i -=1
        i = 20
        y = 40
        # 6
        while (i > 0):
            self.create_rectangle(120, 20, 140, y, outline = "blue", fill = "")
            y += 20
            i -=1
        i = 20
        y = 40
        # 7
        while (i > 0):
            self.create_rectangle(140, 20, 160, y, outline = "blue", fill = "")
            y += 20
            i -=1
        i = 20
        y = 40
        # 8
        while (i > 0):
            self.create_rectangle(160, 20, 180, y, outline = "blue", fill = "")
            y += 20
            i -=1
        i = 20
        y = 40
        # 9
        while (i > 0):
            self.create_rectangle(180, 20, 200, y, outline = "blue", fill = "")
            y += 20
            i -=1
        i = 20
        y = 40
        # 10
        while (i > 0):
            self.create_rectangle(200, 20, 220, y, outline = "blue", fill = "")
            y += 20
            i -=1
        
    

# section of code devoted to input from buttons
        

# classes for different shapes
class Block():

    def __init__(self):
        Block.__init__(self)


#create window
window = Tk()
window.title("Tetris")

# opening the game
s = GridSystem(window)
# creating the grid
s.plotGrid()


window.mainloop()
