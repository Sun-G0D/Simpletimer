# Import Module
from tkinter import *
from datetime import timedelta
import winsound

# create root window
root = Tk()
root.title("Timer")
root.geometry('350x200')
root.resizable(True, True)
is_counting = 0

def done(message):
    def on_click(event=None):
        notif.destroy()
    notif = Toplevel(bg='black', relief=RAISED, bd=3)
    notif.overrideredirect(True)
    notif.geometry("200x50-10-50")
    notif_message = Message(notif, bg='black', fg='white', border=2, text=message)
    notif_message.pack()
    notif.bind('<1>', on_click)

def update_timer():
    global is_counting

    time_left_label.config(text=f"{str(timedelta(seconds=time_left_var.get()))}")

    if time_left_var.get() > 0 and is_counting == 2:
        time_left_var.set(time_left_var.get() - 1)
        root.after(1000, update_timer)  # Call again after 1 second
    elif is_counting != 1:
        is_counting = 0
        time_left_var.set(0)
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS | winsound.SND_ASYNC)
        done("timer done")



def start_timer():
    global is_counting
    if is_counting != 1:
        time_left_var.set(time_left_var.get() + time_var.get())
    if is_counting != 2:
        is_counting = 2
        update_timer()

def stop_timer():
    global is_counting
    is_counting = 1

def reset_timer():
    global is_counting
    time_left_var.set(0)
    is_counting = 0
    time_left_label.config(text=f"{str(timedelta(seconds=time_left_var.get()))}")

time_left_var = IntVar(root, 0)
time_var = IntVar(root, 0)
time_label = Label(root, text = 'Input Time', font=('calibre',10,'bold'))
time_entry = Entry(root, textvariable = time_var, font=('calibre',10,'normal'))
time_left_label = Label(root, text = 'Time Left', font=('calibre',10,'bold'))
start_button = Button(root, text="Start", command=start_timer)
stop_button = Button(root, text="Stop", command=stop_timer)
reset_button = Button(root, text="Reset", command=reset_timer)

time_label.grid(row=0,column=0)
time_entry.grid(row=0,column=1)
time_left_label.grid(row=1,column=1)
start_button.grid(row=2,column=1)
stop_button.grid(row=2,column=2)
reset_button.grid(row=2,column=3)

root.mainloop()