#calculator
#Joshua Johnson
#May 6, 2018

#The objective of this code was to make a basic calculator.
#I made the calculator along with added features such as the Ans button and a message box for errors.

#References:
#-Kush greatly helped me understand and format my calculator
#-Youtube video "Python Tkinter Calculator Tutorial (Part 1): User Interface" by Henry Zhu for some functions

#initialize tkinter window
from tkinter import *
from tkinter import messagebox

calc = Tk()                     #set Tk to calc
calc.title("Calculator")        #set title of calc
calc.geometry("344x529")        #set window size of calc
calc.resizable(0,0)             #set window to fixed dimensions

class Application:
#this class is for all the calculator's functions

    def __init__(self, master):
        #this function is to set up the whole calculator
        global disp
        disp = ""
        myFont = ("Comic Sans", 14)

        #calculator display
        self.input = StringVar()
        self.disp_lbl = Label(master, font = myFont, fg = "red", bg = "gold", height = 4, textvariable = self.input, justify = CENTER).grid(row = 0, columnspan = 64, sticky = E + W)

        #number widgets
        Button(calc, text = "0", font = myFont, width = 5, height = 4, fg = "red", bg = "orange", padx = 3, pady = 3, command = lambda: self.appendToDisp("0")).grid(row = 4, column = 0)
        Button(calc, text = "1", font = myFont, width = 5, height = 4, fg = "red", bg = "orange", padx = 3, pady = 3, command = lambda: self.appendToDisp("1")).grid(row = 3, column = 0)
        Button(calc, text = "2", font = myFont, width = 5, height = 4, fg = "red", bg = "orange", padx = 3, pady = 3, command = lambda: self.appendToDisp("2")).grid(row = 3, column = 1)
        Button(calc, text = "3", font = myFont, width = 5, height = 4, fg = "red", bg = "orange", padx = 3, pady = 3, command = lambda: self.appendToDisp("3")).grid(row = 3, column = 2)
        Button(calc, text = "4", font = myFont, width = 5, height = 4, fg = "red", bg = "orange", padx = 3, pady = 3, command = lambda: self.appendToDisp("4")).grid(row = 2, column = 0)
        Button(calc, text = "5", font = myFont, width = 5, height = 4, fg = "red", bg = "orange", padx = 3, pady = 3, command = lambda: self.appendToDisp("5")).grid(row = 2, column = 1)
        Button(calc, text = "6", font = myFont, width = 5, height = 4, fg = "red", bg = "orange", padx = 3, pady = 3, command = lambda: self.appendToDisp("6")).grid(row = 2, column = 2)
        Button(calc, text = "7", font = myFont, width = 5, height = 4, fg = "red", bg = "orange", padx = 3, pady = 3, command = lambda: self.appendToDisp("7")).grid(row = 1, column = 0)
        Button(calc, text = "8", font = myFont, width = 5, height = 4, fg = "red", bg = "orange", padx = 3, pady = 3, command = lambda: self.appendToDisp("8")).grid(row = 1, column = 1)
        Button(calc, text = "9", font = myFont, width = 5, height = 4, fg = "red", bg = "orange", padx = 3, pady = 3, command = lambda: self.appendToDisp("9")).grid(row = 1, column = 2)

        #operational widgets
        Button(calc, text = "CE", font = myFont, width = 5, height = 4, fg = "red", bg = "skyblue", padx = 3, pady = 3, command = lambda: self.clearButton()).grid(row = 1, column = 3)
        Button(calc, text = "(", font = myFont, width = 5, height = 4, fg = "red", bg = "skyblue", padx = 3, pady = 3, command = lambda: self.appendToDisp("(")).grid(row = 2, column = 3)
        Button(calc, text = ")", font = myFont, width = 5, height = 4, fg = "red", bg = "skyblue", padx = 3, pady = 3, command = lambda: self.appendToDisp(")")).grid(row = 3, column = 3)
        Button(calc, text = "+", font = myFont, width = 5, height = 4, fg = "red", bg = "skyblue", padx = 3, pady = 3, command = lambda: self.appendToDisp("+")).grid(row = 1, column = 4)
        Button(calc, text = "-", font = myFont, width = 5, height = 4, fg = "red", bg = "skyblue", padx = 3, pady = 3, command = lambda: self.appendToDisp("-")).grid(row = 2, column = 4)
        Button(calc, text = "*", font = myFont, width = 5, height = 4, fg = "red", bg = "skyblue", padx = 3, pady = 3, command = lambda: self.appendToDisp("*")).grid(row = 3, column = 4)
        Button(calc, text = "/", font = myFont, width = 5, height = 4, fg = "red", bg = "skyblue", padx = 3, pady = 3, command = lambda: self.appendToDisp("/")).grid(row = 4, column = 4)
        Button(calc, text = ".", font = myFont, width = 5, height = 4, fg = "red", bg = "skyblue", padx = 3, pady = 3, command = lambda: self.appendToDisp(".")).grid(row = 4, column = 1)        
        Button(calc, text = "=", font = myFont, width = 5, height = 4, fg = "red", bg = "skyblue", padx = 3, pady = 3, command = lambda: self.equalButton()).grid(row = 4, column = 2)
        Button(calc, text = "Ans", font = myFont, width = 5, height = 4, fg = "red", bg = "skyblue", padx = 3, pady = 3, command = lambda: self.ansButton()).grid(row = 4, column = 3)

    def appendToDisp(self, text):
        #this function is to add the widget or result to the display
        global disp
        disp = disp + text
        self.input.set(disp)

    def clearButton(self):
        #this function is to clear the display
        global disp
        disp = ""
        self.input.set(disp)

    def equalButton(self):
        #this function is to calculate the inputted expression
        global disp
        global result
        try:
            result = int(eval(disp))
            disp = str(result)
            self.input.set(disp)

        except SyntaxError or ValueError:
            messagebox.showinfo("ERROR", "Invalid Input")
            disp = ""

    def ansButton(self):
        #this function is to add the previous answer to the display
        global disp
        global result
        disp = disp + str(result)
        self.input.set(disp)

calculator_gui = Application(calc)  #call Application class
calc.mainloop()                     #run calc in mainloop
