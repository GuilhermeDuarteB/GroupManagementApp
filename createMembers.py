from tkinter import *
import json
import tkinter as tk
from tkinter import ttk
import os
from tkinter import messagebox

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

def vef_member(name):
    memory = load_memory()

    for group in memory:
        member = group.get("members", [])

        if isinstance(member, str):
            member = [] if member.strip() == "" else [member]

        for m in member:
            if isinstance(m, str) and m.lower() == name.lower():
                return True, group.get("GroupName", "Unknown")
    return False, None

#create member func app
def create_member(parent):
    createMember = Toplevel(parent)
    createMember.title("Create Member")
    createMember.geometry("400x300")
    createMember.resizable(False, False)
    createMember.iconbitmap("group.ico")

    Label(createMember, text="Member Name:", font=("Arial", 12)).pack(pady=10)
    entryMemberName = Entry(createMember, font=("Arial", 12))
    entryMemberName.pack(pady=5)

    groupData = load_memory()
    groups = [item["GroupName"] for item in groupData if "GroupName" in item]

    Label(createMember, text="Group:", font=("Arial", 12)).pack(pady=10)
    if not groups:
        combo = ttk.Combobox(createMember, values=["No Groups"], state="disabled")
        combo.set("No Groups")
    else:
        combo = ttk.Combobox(createMember, values=groups, state="readonly")
        combo.set("")
    combo.pack(padx=20, pady=20)

    #save btn

    def save():
        memberName = entryMemberName.get().strip()
        selectedGroup = combo.get().strip()

        if memberName == "":
            messagebox.showerror("Error", "Insert the member name.")
            return
        
        # verify if the member already exists in a group
        exists, group_found = vef_member(memberName)
        if exists:
            messagebox.showerror("Error", f"The member already exists in the group '{group_found}'!")
            return

        if selectedGroup == "" or selectedGroup == "No Groups":
            messagebox.showerror("Error", "Please select a valid group.")
            return
        
        memory = load_memory()
        group = None
        for g in memory:
            if g.get("GroupName", "").lower() == selectedGroup.lower():
                group = g
                break

        if group is None:
            messagebox.showerror("Error", "Selected group not found!")
            return

        qty_raw = group.get("quantity", 0)
        try:
            max_quantity = int(qty_raw)
        except:
            messagebox.showerror("Error", f"Invalid group quantity: {qty_raw}")
            return
        
        # normalize members
        members_field = group.get("members", "")
        if isinstance(members_field, list):
            members = members_field
        else:
            members = [] if isinstance(members_field, str) and members_field.strip() == "" else []

        # verify if member already exists in THIS group
        for m in members:
            if isinstance(m, str) and m.lower() == memberName.lower():
                messagebox.showerror("Error", "The member already exists in this group.")
                return

        # group full
        if len(members) >= max_quantity:
            messagebox.showerror("Error", "This group is full.")
            return
        
        # add member
        members.append(memberName)
        group["members"] = members

        save_memory(memory)

        messagebox.showinfo("Success!", f"Member '{memberName}' added to group '{selectedGroup}'")
        createMember.destroy()

    Button(createMember, text="Save",font=("Arial", 12), command=save).pack(pady=20)