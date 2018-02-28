# -*- coding:utf-8 -*-
import Tkinter as tk


class Todo(tk.Tk, object):
    def __init__(self, tasks=None):
        super(Todo, self).__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.title("want---Do")
        self.geometry("300x400")

        todo1 = tk.Label(self, text="待完成事项", bg="lightgrey", fg="black", pady=10)

        self.tasks.append(todo1)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        self.task_create = tk.Text(self, height=3, bg="white", fg="black")

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        self.bind("<Return>", self.add_task)

        self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]

        self.add_button()

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0,tk.END).strip()

        if len(task_text) > 0:
            new_task = tk.Label(self, text=task_text, pady=10)

            _, task_style_choice = divmod(len(self.tasks), 2)

            my_scheme_choice = self.colour_schemes[task_style_choice]

            new_task.configure(bg=my_scheme_choice["bg"])
            new_task.configure(fg=my_scheme_choice["fg"])

            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)

        self.task_create.delete(1.0, tk.END)


    def add_button(self):
        m1 = tk.PanedWindow()
        m1.pack(fill=tk.BOTH,side=tk.BOTTOM)
        left = tk.Button(m1, text="添加", )
        mid = tk.Button(m1, text="保存")
        right = tk.Button(m1, text="删除")
        m1.add(left)
        m1.add(mid)
        m1.add(right)