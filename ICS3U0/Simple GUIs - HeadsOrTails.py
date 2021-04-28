#Simple GUIs - headsOrTails

from tkinter import *
from random import randint

counter = 5

def heads():
    global counter
    choice = randint(1,2)
    if choice == 1:
        Label(window, text = "Heads. You were correct! Try again.").grid(row = counter, column = 0, columnspan = 3)
        counter += 1
    else:
        Label(window, text = "Tails. You were incorrect! Try again.").grid(row = counter, column = 0, columnspan = 3)
        counter += 1

def tails():
    global counter
    choice = randint(1,2)
    if choice == 1:
        Label(window, text = "Tails. You were correct! Try again.").grid(row = counter, column = 0, columnspan = 3)
        counter += 1
    else:
        Label(window, text = "Heads. You were incorrect! Try again.").grid(row = counter, column = 0, columnspan = 3)
        counter += 1

window = Tk()
window.title("Guessing Game")

Label(window, text = "Heads/Tails Guessing Game", font = ("Arial", 14, "italic")).grid(row = 0, column = 0)
Label(window, text = "Will heads or tails come up next?").grid(row = 1, column = 1)
Label(window, text = "Click on one of the buttons to choose.").grid(row = 2, column = 1)

Button(window, text = "Heads", command = heads, width = 20).grid(row = 3, column = 0)
Button(window, text = "Tails", command = tails, width = 20).grid(row = 3, column = 1)

window.mainloop()
