#Simple GUIs - busFare

from tkinter import *

counter = 5

def fare():
    global counter
    if int(disp.get()) <= 18:
        Label(window, text = "Your fare is $3.00").grid(row = counter, column = 0)
        counter += 1
    elif int(disp.get()) <= 65:
        Label(window, text = "Your fare is $5.00").grid(row = counter, column = 0)
        counter += 1
    else:
        Label(window, text = "Your fare is $2.50").grid(row = counter, column = 0)
        counter += 1

window = Tk()
window.title("BusFare")

Label(window, text = "Enter age then press Return").grid(row = 0, column = 0)
disp = Entry(window, width = 10)
disp.grid(row = 0, column = 1)
disp.focus()
Button(window, text = "Return", command = fare).grid(row = 0, column = 2)



window.mainloop()
