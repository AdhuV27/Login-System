import sqlite3 as sql
from tkinter import *
import subprocess

# screen stuff
screen = Tk()


# sql stuff
conn = sql.connect(
    "C:\\Users\\ADYAN\\OneDrive\\Desktop\\Adyant\\sqlitedbs\\randompythonthing.db")

cr = conn.cursor()



def check_login(name, passw):

    cr.execute(
        "SELECT * FROM info WHERE USERNAME = ? AND PASSWORD = ?", (name, passw))
    final_result = cr.fetchone()

    if final_result:

        label_login = Label(screen, text=f"Logged in as {name}")
        label_login.grid(row=2, column=0, columnspan=2)
    else:

        label_login = Label(
            screen, text="Please check login credentials(failed to login)")
        label_login.grid(row=0, column=0, columnspan=2, rowspan=3)

    button_enter.destroy()
    label_user.destroy()
    label_pass.destroy()
    entry_pass.destroy()
    entry_user.destroy()


entry_user = Entry(screen)
label_user = Label(screen, text="Enter Username here: ")
entry_pass = Entry(screen)
label_pass = Label(screen, text="Enter Password here")
button_enter = Button(
    screen, text="Click to enter details", command=lambda: check_login(entry_user.get(), entry_pass.get()))

label_user.grid(row=0, column=0)
entry_user.grid(row=0, column=1)
label_pass.grid(row=1, column=0)
entry_pass.grid(row=1, column=1)
button_enter.grid(row=2, column=0)


# the end (i hope)
screen.mainloop()
conn.close()