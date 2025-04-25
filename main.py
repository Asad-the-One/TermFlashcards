"""
εεε
"""

import tkinter as tk
from random import randint

# Get list of words
words = []
f = open("words.txt", "r")
for i in f:
    words.append(i.strip().split("εεε"))
f.close()

# Create window
win = tk.Tk()
win.geometry("500x200")

# State globals
term = ""
point = ""

# Main frame

def main():
    
    # Create frame
    f1 = tk.Frame(win, padx=5, pady=5)
    f1.pack()

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
    l1 = tk.Label(f1, text=term[0])
    l1.pack()

    # Create label that displays score
    l2 = tk.Label(f1,text=term[2])
    l2.pack()

    ############## Buttons

    # Create button to switch definition to answer
    def switch():
        if l1.cget("text") == term[0]:
            l1.config(text=term[1])
        else:
            l1.config(text=term[0])
    b1 = tk.Button(f1, text="Switch", command=switch)
    b1.pack()

    # Create button to input "I know this". Changes word
    def correct():
        global words
        words[words.index(term)][2] = str(int(words[words.index(term)][2]) + 1)
        getTerm()
        l1.config(text=term[0])
        l2.config(text=term[2])
    b2 = tk.Button(f1, text="Correct", command=correct)
    b2.pack()

    # Create button to input "I don't know this". Changes word
    def wrong():
        global words
        if int(words[point][2]) > 0:
            words[point][2] = str(int(words[point][2]) - 1)
        getTerm()
        l1.config(text=term[0])
        l2.config(text=term[2])
    b3 = tk.Button(f1, text="Wrong", command=wrong)
    b3.pack()

    # Create button to quit
    def byebye():
        win.destroy()
    b4 = tk.Button(f1, text="Quit", command=byebye)
    b4.pack()

main()
win.mainloop()

f = open("words.txt", "w")
for i in words:
    f.write(f"{i[0]}εεε{i[1]}εεε{i[2]}\n")