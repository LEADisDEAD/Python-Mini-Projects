import tkinter as tk
import json

class ToDoApp:
    def __init__(self,root):
        self.root = root
        self.root.title("To do List app")
        self.root.geometry("400x400")

        self.label = tk.Label(window, text="To-Do App", font=("Roboto",15,"bold"))
        self.label.pack(pady=10)

        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)

        self.task_listbox = tk.Listbox(root,width=50)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(root,text="Add task",command = self.add_task)
        self.add_button.pack(pady=10)

        self.delete_button = tk.Button(root,text="Delete Task",command = self.delete_task)
        self.delete_button.pack()

        self.complete_button = tk.Button(root,text = "Mark as completed",command = self.mark_completed)
        self.complete_button.pack(pady=10)


        self.load_tasks()
    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_listbox.insert(tk.END,task)
            self.task_entry.delete(0,tk.END)
            self.save_tasks()

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            select = self.task_listbox.get(selected)
            self.task_listbox.delete(selected)
            self.save_tasks()

    def mark_completed(self):
        selected = self.task_listbox.curselection()
        if selected:
            select = self.task_listbox.get(selected)
            self.task_listbox.delete(selected)
            self.task_listbox.insert(selected,f"✅ {select}")
            self.save_tasks()
    def save_tasks(self):
        tasks = self.task_listbox.get(0,tk.END)
        with open("tasks.json","w") as file:
            json.dump(list(tasks),file)

    def load_tasks(self):
        try:
            with open("tasks.json") as file:
                tasks = json.load(file)
                for task in tasks:
                    self.task_listbox.insert(tk.END,task)
        except FileNotFoundError:
            pass

window = tk.Tk()
app = ToDoApp(window)
window.mainloop()