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
        self.create_rectangle(20, 20, 200, 400, outline = "blue", fill = "")
        
    

# section of code devoted to input from buttons
        

# classes for different shapes


#create window
window = Tk()
window.title("Tetris")

# opening the game
s = GridSystem(window)
# creating the grid
s.plotGrid()


window.mainloop()
