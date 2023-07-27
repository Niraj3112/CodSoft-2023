from tkinter import *

root = Tk()
root.title("ToDo List")
root.geometry("400x500")

#create a list that will store the all addes task
list = []

#create a label
heading = Label(root, text="TASKS",bg="grey", font="arial 25 bold")
heading.place(x=140, y=10)
# functions which will help to add task and delete task
def add_task():
    task_text = task.get()
    list.append(task_text)
    listbox.insert(END, task_text)
    task_entry.delete(0, END)
def delete_task():
    selected_task_index = listbox.curselection()
    index = selected_task_index[0]
    listbox.delete(index)
    list.pop(index)

#main
frame = Frame(root, width=400, height=300, bg="#F0F0F0")
frame.place(x=0, y=120)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0, textvariable=task)
task_entry.pack(pady=10)

btn1 = Button(frame, text="ADD", font="arial 20", bg="#008000", fg="white", bd=0, command=add_task)
btn1.pack(pady=10)

#box
listbox = Listbox(frame, width=35, height=10, bg="grey", font="arial 15", fg="white", selectbackground="#F0F0F0")
listbox.pack(pady=20, padx=0)

btn2 = Button(root, text="Delete", font="arial 20", bg="red", fg="white", bd=0, command=delete_task)
btn2.place(x=150, y=450)

root.mainloop()