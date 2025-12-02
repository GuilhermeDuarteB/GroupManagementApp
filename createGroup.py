from tkinter import *
import json
import os
from tkinter import messagebox

# Memory functions

def load_memory():
    if not os.path.exists("memory.json"):
        with open("memory.json", "w", encoding="utf-8") as f:
            json.dump([], f)
    try:
        with open("memory.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_memory(mem):
    with open("memory.json", "w", encoding="utf-8") as f:
        json.dump(mem, f, indent=4, ensure_ascii=False)

#create group def

def create_group(parent):
    createGroup = Toplevel(parent)
    createGroup.title("Create Group")
    createGroup.geometry("400x300")
    createGroup.resizable(False, False)
    createGroup.iconbitmap("group.ico")
    
    Label(createGroup, text="Group Name:", font=("Arial", 12)).pack(pady=10)
    entry_name = Entry(createGroup, font=("Arial", 12))
    entry_name.pack(pady=5)

    Label(createGroup, text="Number of Members:", font=("Arial", 12)).pack(pady=10)
    entry_members = Entry(createGroup, font=("Arial", 12))
    entry_members.pack(pady=5)

    Label(createGroup, text="Description (optional):", font=("Arial", 12)).pack(pady=10)
    entry_desc = Entry(createGroup, font=("Arial", 12))
    entry_desc.pack(pady=5)

    #save btn

    def save():
        name = entry_name.get().strip()
        membersNr = entry_members.get().strip()
        desc = entry_desc.get().strip()

        if name == "":
            messagebox.showerror("Error", "The group name is required!")
            return
        
        if membersNr == "":
            messagebox.showerror("Error", "Members quantity is required!")
            return
        
        if not membersNr.isnumeric():
            messagebox.showerror("Error", "The group quantity needs to be in numbers!")
            return
        memory = load_memory()

        #group verify

        for g in memory:
            if g["GroupName"].lower() == name.lower():
                messagebox.showerror("Error", "This group already exist!")
                return

        new_group = {
            "GroupName": name,
            "quantity": membersNr,
            "description": desc,
            "members": ""}

        memory.append(new_group)
        save_memory(memory)

        messagebox.showinfo("Success!", "Group created!")
        createGroup.destroy()

    Button(createGroup, text="Save", font=("Arial", 12), command=save).pack(pady=20)