from tkinter import *
from node import Node

window = Tk()
window.resizable(False, False)

def close():
    window.quit()
    window.destroy()

menubar = Menu(window)
close_menu = Menu(menubar, tearoff=0)
close_menu.add_command(label="프로그램 종료", command=close)
menubar.add_cascade(label="프로그램 조작", menu=close_menu)

window.config(menu=menubar)

window.attributes('-fullscreen', True)

frame1 = Frame(window, relief="solid", bd=1)
frame1.pack(side="left", fill="both", expand=True)

frame2 = Frame(window, relief="solid", bd=1)
frame2.pack(side="right", fill="both", expand=True)

node1 = Node(frame1, "노드1")
node1.pack()

window.mainloop()