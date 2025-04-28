"""
εεε

Issues:
. File not saving properly after practice
"""

import tkinter as tk
from random import randint
import os

# State globals
words = []
term = ""
point = ""

# Get list of words
def getWords(name):
    global words
    f = open(name, "r")
    for i in f:
        words.append(i.strip().split("εεε"))
    f.close()

# Update file
def updateFile(name):
    f = open(name, "w")
    for i in words:
        f.write(f"{i[0]}εεε{i[1]}εεε{i[2]}\n")
    f.close()

# Create window
win = tk.Tk()
win.geometry("500x200")

# Frame, menu

def menu():

    # Create frame
    f1 = tk.Frame(win, padx=5, pady=5)
    f1.pack()

    ############## Labels

    # Header
    l1 = tk.Label(f1, text="Filler Title")
    l1.pack()

    ############## Dropdown with packs

    # Get list of ".txt" files
    files = []
    for i in os.listdir():
        if i[-4:] == ".txt":
            files.append(i)
    
    # Stringvar with first value in list
    v = tk.StringVar(f1, files[0])

    # Create dropdown menu
    o1 = tk.OptionMenu(f1, v, *files)
    o1.pack()

    ############## Buttons

    # Button to enter flashcards
    def startFlash():
        global file
        f1.destroy()
        file = v.get()
        getWords(file)
        flashes()
    b1 = tk.Button(f1, text="Practice", command=startFlash)
    b1.pack()

    # Button to quit
    def bye():
        win.destroy()
    b3 = tk.Button(f1, text="Quit", command=bye)
    b3.pack()

# Frame with flashcards

def flashes():
    
    # Create frame
    f2 = tk.Frame(win, padx=5, pady=5)
    f2.pack()

    ############## Labels

    # Select random word, and confirm selection based on score
    def getTerm():
        global term
        global point
        while True:            
            point = randint(0,len(words))
            #index = words[point]
            term = words[point] # <-- Select
            
            if randint(0,int(term[2])+1) == 0: # <-- Confirm
                break
    print(term)
    getTerm()

    # Create label on top that has the term
    l1 = tk.Label(f2, text=term[0])
    l1.pack()

    # Create label that displays score
    l2 = tk.Label(f2,text=term[2])
    l2.pack()

    ############## Buttons

    # Create button to switch definition to answer
    def switch():
        if l1.cget("text") == term[0]:
            l1.config(text=term[1])
        else:
            l1.config(text=term[0])
    b1 = tk.Button(f2, text="Switch", command=switch)
    b1.pack()

    # Create button to input "I know this". Changes word
    def correct():
        global words
        words[words.index(term)][2] = str(int(words[words.index(term)][2]) + 1)
        getTerm()
        l1.config(text=term[0])
        l2.config(text=term[2])
    b2 = tk.Button(f2, text="Correct", command=correct)
    b2.pack()

    # Create button to input "I don't know this". Changes word
    def wrong():
        global words
        if int(words[point][2]) > 0:
            words[point][2] = str(int(words[point][2]) - 1)
        getTerm()
        l1.config(text=term[0])
        l2.config(text=term[2])
    b3 = tk.Button(f2, text="Wrong", command=wrong)
    b3.pack()

    # Create button to quit
    def byebye():
        f2.destroy()
        updateFile(file)
        menu()
    b4 = tk.Button(f2, text="Quit", command=byebye)
    b4.pack()

# Create a new pack
def newPack():
    pass


# Summon menu and loop
menu()
win.mainloop()

"""
# Importing Tkinter module
from tkinter import *
# from tkinter.ttk import *
 
# Creating master Tkinter window
master = Tk()
master.geometry("175x175")
 
# Tkinter string variable
# able to store any string value
v = StringVar(master, "1")
 
# Dictionary to create multiple buttons
values = {"RadioButton 1" : "1",
          "RadioButton 2" : "2",
          "RadioButton 3" : "3",
          "RadioButton 4" : "4",
          "RadioButton 5" : "5"}
 
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
    Radiobutton(master, text = text, variable = v, 
                value = value, indicator = 0,
                background = "light blue").pack(fill = X, ipady = 5)
 
# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())
mainloop()
"""