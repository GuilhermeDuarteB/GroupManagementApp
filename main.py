from tkinter import *
from tkinter import ttk
from createGroup import create_group
from createMembers import create_member
import json
import os

window = Tk()
window.title("Group Management App")
window.geometry("1200x750")
window.resizable(False, False)
window.iconbitmap("group.ico")

#memory funcs
def load_memory():
    if not os.path.exists("memory.json"):
        with open("memory.json", "w", encoding="utf-8") as f:
            json.dump([], f)
    try:
        with open("memory.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return[]

def save_memory(mem):
    with open("memory.json", "w", encoding="utf-8") as f:
        json.dump(mem, f, indent=4, ensure_ascii=False)


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
listbtn = Button(btnFrame, text="Create Members", **button_style, command=lambda: create_member(window))
listbtn.grid(row=0, column=1, padx=10)

#group list frame
grouplistFrame = Frame(mainFrame, bg="#c0abab")
grouplistFrame.place(relx=0.5,rely=0.2,anchor="n",relwidth=0.9,relheight=0.8)

#render groups
def render_groups():
    for widget in grouplistFrame.winfo_children():
        widget.destroy()

    groups = load_memory()

    if not groups:
        Label(grouplistFrame, text="No Groups Created", font=("Segoe UI", 14), bg="f0f0f0")
        return
    
    for groups in groups:
        name = groups.get("GroupName", "Unnamed")
        max_qnt = int(groups.get("quantity", 0))
        members = int(groups.get("members", []))

    if isinstance(members, str):
        members = [] if members.strip() == "" else [members]

    currentQnt = len(members)

    #card frame
    card = Frame(grouplistFrame, bg="white", bd=1, relief="solid")
    card.pack(fill="x", pady=10, padx=10)

#main 
window.mainloop()
