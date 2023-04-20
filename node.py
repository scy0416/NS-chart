from tkinter import *

class Node(Frame):
    def __init__(self, window, label):
        super().__init__(window, relief="solid", bd=1)

        l = Label(self, text=label)
        l.pack(side="left")

        btn = Button(self, text="편집")
        btn.pack()