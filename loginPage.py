import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import ast

root = tk.Tk()
root.title("BB's Video Project Sign in Page")
root.geometry('1350x820')
root.configure(bg="#fff")
root.resizable(False, False)


# -------------------------- # Loop for username and password. Includes pop-up error screen, messagebox #
def signin():
    username = user.get()
    password = code.get()

    file = open('datasheet.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    print(r.keys())
    print(r.values())

    if username in r.keys() and password == r[username]:
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="#ffff9f")

        (Label(screen, text='Hello & Thank you for your time!', bg='#ffff9f', font=('Georgia Bold', 32))
         .pack(expand=True))

        screen.mainloop()

    else:
        messagebox.showerror('Invalid', 'invalid username or password')


# -------------################################################################################ -------- Sign up Page

def signup_command():
    window = Toplevel(root)
    window.title("SignUp")
    window.geometry('1355x780+280+200')
    window.configure(bg='#57a1f8')
    window.resizable(False, False)

    def signup():
        username = user.get()
        password = code.get()
        conform_password = confirm_code.get()

        if password == conform_password:
            try:
                file = open('datasheet.txt', 'r+')
                d = file.read()
                r = ast.literal_eval(d)

                dict2 = {username: password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file = open('datasheet.txt', 'w')
                w = file.write(str(r))

                messagebox.showinfo('Signup', 'Successfully sign up')
                window.destroy()

            except:
                file = open('datasheet.txt', 'w')
                pp = str({'Username': 'password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror('Invalid', "Both Password should match")

    def sign():
        window.destroy()

    img = PhotoImage(file='StockCake4_1724210224.png')
    Label(window, image=img, border=0, bg='white').place(x=25, y=25)

    frame = Frame(window, width=475, height=375, bg='#ffff9f')
    frame.place(x=777, y=100)

    heading = Label(frame, text='Sign up & Enjoy', fg="#57a1f8", bg="#ffff9f", font=('Georgia Bold', 30))
    heading.place(x=75, y=22)
    # ------------------------------------------------------------------------------------ # Username #

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        if user.get() == '':
            user.insert(0, 'Username')

    user = Entry(frame, width=25, fg='black', border=0, bg="#ffff9f", font=('Georgia', 20))
    user.place(x=100, y=90)
    user.insert(0, 'Username')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame, width=280, height=2, bg='black').place(x=100, y=122)
    # ----------------------------------------------------------------------------------- # Password #

    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        if code.get() == '':
            code.insert(0, 'Password')

    code = Entry(frame, width=25, fg='black', border=0, bg="#ffff9f", font=('Georgia', 20))
    code.place(x=100, y=140)
    code.insert(0, 'Password')
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)

    Frame(frame, width=280, height=2, bg='black').place(x=100, y=172)
    # -------------------------------------------------------------------------------- # Confirm Password #

    def on_enter(e):
        confirm_code.delete(0, 'end')

    def on_leave(e):
        if confirm_code.get() == '':
            confirm_code.insert(0, 'Confirm Password')

    confirm_code = Entry(frame, width=25, fg='black', border=0, bg="#ffff9f", font=('Georgia', 20))
    confirm_code.place(x=100, y=191)
    confirm_code.insert(0, 'Confirm Password')
    confirm_code.bind("<FocusIn>", on_enter)
    confirm_code.bind("<FocusOut>", on_leave)

    Frame(frame, width=280, height=2, bg='black').place(x=100, y=223)
    # ---------------------------------------------------------------------------------- # Sign up Button #

    Button(frame, width=16, pady=7, text='Sign up', bg='#57a1f8', fg='#ffff9f', font=('Georgia Bold', 20),
           border=0, command=signup).place(x=94, y=250)
    # --------------------------------------------------------------------------------------------------- #
    label = Label(frame, text='I have an account', fg='black', bg="#ffff9f", font=('Georgia', 18))
    label.place(x=100, y=320)

    # ---------------------------------------------------------------------------------- # Sign in Button #
    signin = Button(frame, width=6, text='Sign in', border=0, bg="#ffff9f", font=('Georgia Bold', 16),
                    cursor='hand2', fg='#57a1f8', command=sign)
    signin.place(x=300, y=317)

    window.mainloop()

# -------------################################################################################ -------- Login Page


# The size of the background image field to be displayed
canvas = tk.Canvas(root, width=1460, height=820)
canvas.pack()

bg_image = tk.PhotoImage(file=r"C:\Users\db4ba\PycharmProjects\\BB_Movie_LoginSystem\Main_login_page\StockCake_1724210366.png")
canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)
# Background image

# Text coordinates
x, y = 702, 70
text = "Welcome to BB's Video Search Engine"

# Boarder fill around text to have it pop
for dx in [-1.5, 1.5]:
    for dy in [-1.5, 1.5]:
        canvas.create_text(x + dx, y + dy, text=text, font=("Georgia Bold", 42), fill="#292200")

# Then add the text color fill in
canvas.create_text(x, y, text=text, font=('Georgia Bold', 42), fill='#6c84ff')

# Create a box for activity
frame = Frame(root, width=420, height=400, bg='#ffff9f')
frame.place(x=825, y=175)

# Sign in header
heading = Label(frame, text='Sign in', fg='#292200', bg='#ffff9f', font=('Georgia Bold', 32))
heading.place(x=125, y=15)


#  ---------------------------------------------------------------------------------------- # username #
def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


user = Entry(frame, width=30, fg='#292200', border=0, bg='#ffff9f', font=('Georgia', 20))
user.place(x=80, y=95)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=272, height=2, bg='#292200').place(x=70, y=130)


#  ------------------------------------------------------------------------------------- # password code #
def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    name = code.get()
    if name == '':
        user.insert(0, 'Password')


code = Entry(frame, width=30, fg='#292200', border=0, bg='#ffff9f', font=('Georgia', 20))
code.place(x=80, y=155)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=272, height=2, bg='#292200').place(x=70, y=190)

# --------------------------------------------------------------------------------------- # Sign in Button #
(Button(frame, width=15, pady=7, text='Sign in', bg="#6c84ff", fg='#292200', font=('Georgia Bold', 20),
        border=0, command=signin).place(x=70, y=215))

# ------------------------------------------------------------------------------------------------------- #
label = Label(frame, text="Have you been here before?", fg='#292200', bg='#ffff9f', font=('Georgia', 18))
label.place(x=58, y=300)

# --------------------------------------------------------------------------------------- # Sign up Button #
sign_up = Button(frame, width=6, text='Sign up', font=('Georgia Bold', 16), border=0, bg='#ffff9f',
                 cursor='hand2', fg='#6c84ff', command=signup_command)
sign_up.place(x=164, y=330)

root.mainloop()
