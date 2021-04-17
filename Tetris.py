# Team: 8-bit
# Members: Mason, David, Casey, Logan

# inheritance from Tkinter
from tkinter import *

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

# classes for the blocks

# Block super class
class Block():

    blockColors = ["red","green","yellow","orange","blue","purple"]

    def __init__(self):

# classes for different shapes
class TwoBlock(Block):

    def __init__(self):
        Block.__init__(self)


#create window
window = Tk()
window.title("Tetris")
window.grid(row=20, column=10)
