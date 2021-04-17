# Team: 8-bit
# Members: Mason, David, Casey, Logan

# importing Tkinter's methods and variables
from tkinter import *
# importing pygame
import pygame
# importing random
import random
=======
from random import *



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

# section of code devoted to input from buttons
        

# classes for different shapes
class TwoBlock():

    def __init__(self):
        Block.__init__(self)


#create window
window = Tk()
window.title("Tetris")
window.grid(row=20, column=10)

window.mainloop()
