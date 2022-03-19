from tkinter import *
import os

powerOff = Tk()
powerOff.title("Shut Down App")
powerOff.geometry("500x500")
powerOff.config(bg="lightblue")

def restart():
    os.system("shutdown /r /t 1")   # 1 sec

def restart_time():
    os.system("shutdown /r /t 20")  # 20 sec

def logout():
    os.system("shutdown -l")

def shutdown():
    os.system("shutdown /s /t 1")


# restart
rs_button = Button(powerOff, text="Restart",
                   font="Arial 20 bold",
                   relief=RAISED,
                   cursor="plus",
                   command=restart)
rs_button.place(x=150, y=60, height=50, width=200)

# restart with time
rt_button = Button(powerOff, text="Restart Time",
                   font="Arial 20 bold",
                   relief=RAISED,
                   cursor="plus",
                   command=restart_time)
rt_button.place(x=150, y=160, height=50, width=200)

# logout
lo_button = Button(powerOff, text="Log Out",
                   font="Arial 20 bold",
                   relief=RAISED,
                   cursor="plus",
                   command=logout)
lo_button.place(x=150, y=260, height=50, width=200)

# shutdown
sd_button = Button(powerOff, text="Shut Down",
                   font="Arial 20 bold",
                   relief=RAISED,
                   cursor="plus",
                   command=shutdown)
sd_button.place(x=150, y=360, height=50, width=200)

powerOff.mainloop()

