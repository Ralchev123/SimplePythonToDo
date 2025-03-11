import tkinter as tk
from tkinter import *
z = 0.5 
def remove_button(new_task, button_for_delete):
    new_task.destroy()
    button_for_delete.destroy()


def submit_info():  
    global z
    task_info = add_new.get()
    new_task = tk.Label(root, text = task_info, font = ('Arial', 18))
    new_task.place(relx = 0.5, rely = z, anchor="center" )
    add_new.delete(0, "end")
    button_for_delete = tk.Button(root, text = "X", width = 1, height = 1, command=lambda: remove_button(new_task = new_task, button_for_delete= button_for_delete))
    button_for_delete.place(relx=0.90, rely = z, anchor = "center")
    z += 0.04


root = tk.Tk()
root.geometry("400x700")
root.title("To Do App")
Scrollbar = Scrollbar(root)
Scrollbar.place(relx=1.0, rely=0.0, anchor="ne", relheight=1.0)

label = tk.Label(root, text = "To Do App", font = ('Arial', 18))
label.place(relx = 0.35, rely = 0.02)


add_new = Entry(root)
add_new.place(relx = 0.3, rely = 0.1)

button = tk.Button(root, text = "Add a new Task", width = 25, command=submit_info)
button.place(relx = 0.22, rely = 0.2)



root.mainloop()


    