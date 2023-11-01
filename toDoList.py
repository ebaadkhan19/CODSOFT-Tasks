import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

app = tk.Tk()
app.title("To-Do List")

frame = tk.Frame(app)
frame.pack(pady=10)

entry = tk.Entry(frame, font=("Helvetica", 16))
entry.pack(side=tk.LEFT)

add_button = tk.Button(frame, text="Add Task", command=add_task, font=("Helvetica", 16))
add_button.pack(side=tk.LEFT)

remove_button = tk.Button(frame, text="Remove Task", command=remove_task, font=("Helvetica", 16))
remove_button.pack(side=tk.LEFT)

task_list = tk.Listbox(app, font=("Helvetica", 16))
entry.focus_set()
task_list.pack(pady=10)

app.mainloop()
