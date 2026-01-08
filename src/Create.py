import sqlite3 as sql
import tkinter as tk
import subprocess

# screen stuff
screen = tk.Tk()


# SQL stuff
conn = sql.connect(
    "C:\\Users\\ADYAN\\OneDrive\\Desktop\\Adyant\\sqlitedbs\\randompythonthing.db")

cr = conn.cursor()


cr.execute("""
CREATE TABLE IF NOT EXISTS info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    USERNAME TEXT NOT NULL UNIQUE,
    PASSWORD TEXT NOT NULL
)
""")

def show_login():
    screen.destroy()
    subprocess.Popen(["python", "login.py"])

login_button = tk.Button(screen, text="Log in", command=show_login)
login_button.grid(row=3, column=1, columnspan=2)


failure = None
def sign_up():
    username = entry_user.get()
    password = entry_pass.get()
    confpass = entry_conf.get()

    if confirm(password, confpass):
        cr.execute("INSERT INTO info (USERNAME, PASSWORD) VALUES (?, ?)", (username, password))
        print(f"Inserted: {username}, {password}")

        conn.commit()
        cr.execute("SELECT * FROM info")
        print(cr.fetchall())

    login_button.grid(row=2, column=0)

def confirm(passw = None, conf = None):
    global failure
    if conf == passw:
        success = tk.Label(screen, text = "Successfully created an account!")
        success.grid(row=0, column=0, columnspan=2, rowspan=3)
        entry_user.destroy()
        entry_pass.destroy()
        entry_conf.destroy()
        user_label.destroy()
        pass_label.destroy()
        conf_label.destroy()
        confirm_button.destroy()
        if failure:
            failure.destroy()
            failure = None
        return True
    else:
        if failure:
            failure.destroy()

        failure = tk.Label(screen, text = "Passwords do not match! Re-enter")
        confirm_button.grid(row=3, column=0, columnspan=1, rowspan=1)
        failure.grid(row=3, column=1)
        return False


entry_user = tk.Entry(screen)
user_label = tk.Label(screen, text = "Enter ur account name: ")
entry_pass = tk.Entry(screen)
pass_label = tk.Label(screen, text = "Enter ur password: ")
entry_conf = tk.Entry(screen)
conf_label = tk.Label(screen, text = "Confirm password: ")

confirm_button = tk.Button(screen, text="Sign up", command = lambda: sign_up())


user_label.grid(row=0, column=0)
entry_user.grid(row=0, column=1)
pass_label.grid(row=1, column=0)
entry_pass.grid(row=1, column=1)
conf_label.grid(row=2, column=0)
entry_conf.grid(row=2, column=1)
confirm_button.grid(row=3, column=0, columnspan=2, rowspan=3)


conn.commit()

screen.mainloop()
conn.close()