#!/usr/bin/env python3
import sys
from tkinter import *
from tkinter.ttk import *
# imports tkinter to create a simple graphical user interface. The wildcard imports all the classes, functions, and variables inside the tkinter module while not having to speciify whether to use the older tk or the newer ttk. It will automagically use the newer if available.

def create():
 # create a new script template by running the pytemp.py script
    print("Creating your new template...")
 #    os.system("python3 pytemp.py")
    print("Done!")

def status():
 # git status
    print("git status")

def commit():
# git commit -m "$name"
    input("Enter a commit message: ")
    print("git commit -m $name")

def push():
# git push mycode HEAD
    print("git push mycode HEAD")

def escape():
# exit the program
    print("Exiting...")
    sys.exit()  

def main():
    window = Tk()
    window.title('megaGITscript')
    window.geometry("600x500")
    # create an entry widget
    entry = Entry(window, width=30)
    entry.pack(pady=20)
    # create a label
    greeting = Label(window, text="What would you like to do?", font=("Helvetica", 20))
    greeting.pack(pady=20)
    # create a frame
    frame = Frame(window)
    frame.pack()
    # create buttons
    create_button = Button(frame, text="Create New Template", command=create)
    create_button.grid(row=0, column=0, padx=5, pady=5)
    status_button = Button(frame, text="git status", command=status)
    status_button.grid(row=0, column=1, padx=5, pady=5)
    commit_button = Button(frame, text="git commit -m $name", command=commit)
    commit_button.grid(row=1, column=0, padx=5, pady=5)
    push_button = Button(frame, text="git push mycode HEAD", command=push)
    push_button.grid(row=1, column=1, padx=5, pady=5)
    exit_button = Button(frame, text="Exit", command=escape)
    window.mainloop()