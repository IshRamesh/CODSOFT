
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

tasks = []

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete!")

def update_task():
    try:
        selected = listbox.curselection()[0]
        new_task = entry.get()
        if new_task:
            tasks[selected] = new_task
            update_listbox()
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter a new task!")
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to update!")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add any Task", command=add_task)
add_button.pack()

update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=20)


root.mainloop()
