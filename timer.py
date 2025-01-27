# Import Module
from tkinter import *
from datetime import timedelta

# create root window
root = Tk()
root.title("Timer")
root.geometry('350x200')
root.resizable(True, True)

def update_timer():
    if time_left_var.get() > 0:
        time_left_var.set(time_left_var.get() - 1)
        time_left_label.config(text=f"{str(timedelta(seconds=time_left_var.get()))}")
        root.after(1000, update_timer)  # Call again after 1 second

def start_timer():
    try:
        time_left_var.set(time_left_var.get() + time_var.get())
    except ValueError:
        time_left_label.config(text="Invalid Input") # Handle non-integer input

time_left_var = IntVar(root, 0)
time_var = IntVar(root, 0)
time_label = Label(root, text = 'Input Time', font=('calibre',10,'bold'))
time_entry = Entry(root, textvariable = time_var, font=('calibre',10,'normal'))
time_left_label = Label(root, text = 'Time Left', font=('calibre',10,'bold'))
start_button = Button(root, text="Start", command=start_timer)

time_label.grid(row=0,column=0)
time_entry.grid(row=0,column=1)
time_left_label.grid(row=1,column=1)
start_button.grid(row=2,column=1)

update_timer()

root.mainloop()