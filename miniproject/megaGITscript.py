#!/usr/bin/env python3
git status
git commit -m "$name"
git push mycode HEAD

from tkinter import *
from tkinter import ttk
# launch tkinter to create a simple GROUPREF_UNI_IGNORE
# git status
# git commit -m "$name"
# git push mycode HEAD

def main():
    root = Tk()
    root.title('megaGITscript')
    root.geometry("600x500")
    def create():
        # create a GROUPREF_UNI_IGNORE
        print("create a GROUPREF_UNI_IGNORE")
    def status():
        # git status
        print("git status")
    def commit():
        # git commit -m "$name"
        print("git commit -m $name")
    def push():
        # git push mycode HEAD
        print("git push mycode HEAD")
    # create a label
    label = ttk.Label(root, text="megaGITscript", font=("Helvetica", 20))
    label.pack(pady=20)
    # create a frame
    frame = Frame(root)
    frame.pack()
    # create buttons
    create_button = ttk.Button(frame, text="Create GROUPREF_UNI_IGNORE", command=create)
    create_button.grid(row=0, column=0, padx=5, pady=5)
    status_button = ttk.Button(frame, text="git status", command=status)
    status_button.grid(row=0, column=1, padx=5, pady=5)
    commit_button = ttk.Button(frame, text="git commit -m $name", command=commit)
    commit_button.grid(row=1, column=0, padx=5, pady=5)
    push_button = ttk.Button(frame, text="git push mycode HEAD", command=push)
    push_button.grid(row=1, column=1, padx=5, pady=5)
    root.mainloop()