from tkinter import *
from tkinter import ttk
from createGroup import create_group
import json
import os

window = Tk()
window.title("Group Management App")
window.geometry("1200x750")
window.resizable(False, False)
window.iconbitmap("group.ico")

# main frame
mainFrame = Frame(window, bg="#f0f0f0")
mainFrame.pack(fill="both", expand=True)

# btn frames
btnFrame = Frame(mainFrame, bg="#a39b9b", padx=10, pady=20)
btnFrame.place(relx=0.5, rely=0.05, anchor="n", relwidth=1)

# btn style
button_style = {
    "bg": "#4a90e2",
    "fg": "white",
    "activebackground": "#357ABD",
    "activeforeground": "white",
    "font": ("Segoe UI", 12, "bold"),
    "bd": 0,
    "relief": "flat",
    "height": 2,
    "width": 20
}

btnFrame.grid_columnconfigure(0, weight=1)
btnFrame.grid_columnconfigure(1, weight=1)

# create list
createbtn = Button(btnFrame, text="Create Group", **button_style, command=lambda: create_group(window))
createbtn.grid(row=0, column=0, padx=10)

# btn list
listbtn = Button(btnFrame, text="Create Members", **button_style)
listbtn.grid(row=0, column=1, padx=10)

#main 
window.mainloop()
