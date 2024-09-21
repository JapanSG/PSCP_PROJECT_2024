import tkinter as tk
from tkinter import *

def save():
    '''Save password to a file(not finished)'''
    global username_field, password_field
    username = username_field.get()
    password = password_field.get() 
    print(username)
    print(password)

master = tk.Tk(className="Password-saver")
master.geometry("500x500")

username_title = Label(
    master,
    text = "username",
    font = ("Arial",10)
    )

password_title = Label(
    master,
    text = "password",
    font = ("Arial",10)
    )

username_field = Entry(
    master,
    text = "username",
    font = ("Arial",10),
    width = 20
    )

password_field = Entry(
    master,
    text = "password",
    font = ("Arial",10),
    width = 20,
    show="*"
    )

save_button = Button(
    master,
    text = "save",
    command = save
    )

username_title.grid(row = 0, column = 0, pady = 10)
username_field.grid(row = 0, column = 1, pady = 10)
password_title.grid(row = 1, column = 0, pady = 10)
password_field.grid(row = 1, column = 1, pady = 10)
save_button.grid(row = 2, column = 1, sticky = 'E',pady = 10)

def main():
    '''Driver Code'''
    global master
    master.mainloop()

if __name__ == "__main__":
    main()
