import tkinter as tk
from tkinter import messagebox

class TodoAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App")

        self.tasks = []
        self.task_entry = tk.Entry(self.root)
        self.task_entry.pack()

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_list = tk.Listbox(self.root)
        self.task_list.pack()

        self.mark_done_button = tk.Button(self.root, text="Mark as Done", command=self.mark_done)
        self.mark_done_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "done": False})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task["done"] else "Not Done"
            self.task_list.insert(tk.END, f"{task['task']} - {status}")

    def mark_done(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["done"] = True
            self.update_task_list()

def main():
    root = tk.Tk()
    app = TodoAppGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
