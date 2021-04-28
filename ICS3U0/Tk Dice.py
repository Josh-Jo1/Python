#dice

##Code was given excluding loops

from tkinter import *   #import the tkinter library

import random   #import the random number generator
random.seed()   #seed the random number generator, for more effective randomness

CELL_WIDTH = 7  #Constant

def setDice():
    #setting the labels for the dice to roll; initially blank
    global dice1, dice2, dice3,dice4,dice5,dice6,dice7,dice8,dice9
    
    dice1 = Label(window, text = " ", bg='red', font="Courier 10")      ##inserted text
    dice1.grid(row=1,column=1, ipadx=CELL_WIDTH, ipady=CELL_WIDTH)
    dice2 = Label(window, text = " ", bg='red', font="Courier 10")
    dice2.grid(row=1,column=2, ipadx=CELL_WIDTH, ipady=CELL_WIDTH)
    dice3 = Label(window, text = " ", bg='red', font="Courier 10")
    dice3.grid(row=1,column=3, ipadx=CELL_WIDTH, ipady=CELL_WIDTH)
    dice4 = Label(window, text = " ", bg='red', font="Courier 10")
    dice4.grid(row=2,column=1, ipadx=CELL_WIDTH, ipady=CELL_WIDTH)
    dice5 = Label(window, text = " ", bg='red', font="Courier 10")
    dice5.grid(row=2,column=2, ipadx=CELL_WIDTH, ipady=CELL_WIDTH)
    dice6 = Label(window, text = " ", bg='red', font="Courier 10")
    dice6.grid(row=2,column=3, ipadx=CELL_WIDTH, ipady=CELL_WIDTH)
    dice7 = Label(window, text = " ", bg='red', font="Courier 10")
    dice7.grid(row=3,column=1, ipadx=CELL_WIDTH, ipady=CELL_WIDTH)
    dice8 = Label(window, text = " ", bg='red', font="Courier 10")
    dice8.grid(row=3,column=2, ipadx=CELL_WIDTH, ipady=CELL_WIDTH)
    dice9 = Label(window, text = " ", bg='red', font="Courier 10")
    dice9.grid(row=3,column=3, ipadx=CELL_WIDTH, ipady=CELL_WIDTH)
    
def rollDice():
    #set the face of the dice based on a random number from 1-6
    print ("Rolling Dice")
    roll = random.randint(1,6)
    print (roll)
    
    dice2.configure(text=' ')               ##Since I added text to setDice, I technically no longer need this
    dice8.configure(text=' ')
    
    if roll == 6:    #rolled a 6        ##inserted loops
        dice5.configure(text=' ')
        
        dice1.configure(text='*')
        dice3.configure(text='*')
        dice4.configure(text='*')
        dice6.configure(text='*')
        dice7.configure(text='*')
        dice9.configure(text='*')
        
    elif roll == 5:
        dice4.configure(text=' ')
        dice6.configure(text=' ')
        
        dice1.configure(text='*')
        dice3.configure(text='*')
        dice5.configure(text='*')
        dice7.configure(text='*')
        dice9.configure(text='*')
        
    elif roll == 4:
        dice4.configure(text=' ')
        dice5.configure(text=' ')
        dice6.configure(text=' ')
        
        dice1.configure(text='*')
        dice3.configure(text='*')
        dice7.configure(text='*')
        dice9.configure(text='*')
        
    elif roll == 3:
        dice3.configure(text=' ')
        dice4.configure(text=' ')
        dice6.configure(text=' ')
        dice7.configure(text=' ')
        
        dice1.configure(text='*')
        dice5.configure(text='*')
        dice9.configure(text='*')
        
    elif roll == 2:
        dice3.configure(text=' ')
        dice4.configure(text=' ')
        dice5.configure(text=' ')
        dice6.configure(text=' ')
        dice7.configure(text=' ')
        
        dice1.configure(text='*')
        dice9.configure(text='*')
        
    else:
        dice1.configure(text=' ')
        dice3.configure(text=' ')
        dice4.configure(text=' ')
        dice6.configure(text=' ')
        dice7.configure(text=' ')
        dice9.configure(text=' ')
        
        dice5.configure(text='*')
        

window = Tk()   # Set the characteristics of the window for Tkinter application
window.title("Tkinter Dice")
window.geometry('200x200')  #width * height


 
lbl = Label(window, text="Click to Roll the dice:") #Instructions for use
lbl.grid(column=0,columnspan=5, row=0)

setDice()   #initialize the dice image

txt = Button(window,width=CELL_WIDTH, text="Roll",command=rollDice) #activate and define the screen button
txt.grid(column=4,row=2)
txt.focus()
 
window.mainloop()   #activate the main application process
