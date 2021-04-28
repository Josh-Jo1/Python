#Simple GUIs - Weather

from tkinter import *

counter = 5

def sunny():
    global counter
    Label(window, text = "Wear sunscreen and hat", justify = "center").grid(row = counter, column = 0, columnspan = 3)
    counter += 1

def raining():
    global counter
    Label(window, text = "Wear rain boots and jacket", justify = "center").grid(row = counter, column = 0, columnspan = 3)
    counter += 1

def snowing():
    global counter
    Label(window, text = "Wear winter hat and jacket", justify = "center").grid(row = counter, column = 0, columnspan = 3)
    counter += 1

window = Tk()
window.title("Weather")

Label(window, text = "What should I wear today?").grid(row = 0, column = 1)
Label(window, text = "Click on the Button That Describes Today's Weather").grid(row = 1, column = 1)

Button(window, text = "Sunny", command = sunny, width = 20).grid(row = 2, column = 0)
Button(window, text = "Raining", command = raining, width = 20).grid(row = 2, column = 1)
Button(window, text = "Snowing", command = snowing, width = 20).grid(row = 2, column = 2)

window.mainloop()
