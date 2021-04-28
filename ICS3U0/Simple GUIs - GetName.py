#Simple GUIs - getName

from tkinter import *

counter = 5

def greeting(event):
    global counter
    Label(window, text = "Hello "+ disp.get() + ". How are you?").grid(row = counter, column = 0)
    counter += 1

window = Tk()
window.title("Get Name")

Label(window, text = "Enter first name then press Return").grid(row = 0, column = 0)
disp = Entry(window, width = 40)
disp.grid(row = 1, column = 0)
disp.focus()
disp.bind("<Return>", greeting)

window.mainloop()
