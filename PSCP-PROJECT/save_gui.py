'''save_gui'''
import tkinter as tk
from tkinter import *
from save import *

## buttons method
def save_password():
    '''Save password to a file(not finished)'''
    global username_field, password_field
    username = username_field.get()
    password = password_field.get() 
    add_password(username,password)
    popup_message = "Password have been saved"
    button_message = "OK"
    popup(popup_message,button_message)

def delete_password():
    '''delete all password'''
    message = "Are you sure you want to delete all saved password?"
    yesno_popup(clear_destroy,popup_message = message)

def clear_destroy(popup):
    '''delete all password and close popup'''
    clear_file()
    popup.destroy()

def show_page2():
    '''show page 2'''
    label22.config(text = read_file())
    page2.tkraise()

def popup(popup_message = "This is a popup", button_message = "close"):
    '''Create a popup window'''
    popup = Toplevel(name="confirmation")
    popup.geometry("300x200")
    label = Label(
        popup,
        text = popup_message
        )
    label.pack(pady = 30)

    button = Button(
        popup,
        text = button_message,
        command = popup.destroy,
        width = 20
        )
    button.pack(pady = 30)

def yesno_popup(func,popup_message = "This is a popup"):
    popup = Toplevel(name="confirmation")
    popup.geometry("300x200")
    button_frame = Frame(popup)
    button_frame.pack()

    label = Label(
        popup,
        text = popup_message
        )
    label.pack(pady = 30)

    yes_button = Button(
        button_frame,
        text = "Yes",
        command = lambda: func(popup)
        )
    yes_button.pack(side = "left",padx = 15,pady = 20)

    no_button = Button(
        button_frame,
        text = "No",
        command = popup.destroy
        )
    no_button.pack(side = "left",padx = 15,pady = 20)

## Main window
master = tk.Tk(className="Password-saver")
master.geometry("500x500")
Grid.rowconfigure(master, 0, weight=1)
Grid.columnconfigure(master, 0, weight=1)
page1 = Frame(master,bg="AntiqueWhite2")
page2 = Frame(master,bg="AntiqueWhite2")
page1.grid(row = 0 , column = 0,sticky = "nsew")
page2.grid(row = 0 , column = 0,sticky = "nsew")
page_button_frame = Frame(master)
page_button_frame.grid(row = 1,column =0)

username_title = Label(
    page1,
    text = "username",
    font = ("Arial",10)
    )

password_title = Label(
    page1,
    text = "password",
    font = ("Arial",10)
    )

username_field = Entry(
    page1,
    text = "username",
    font = ("Arial",10),
    width = 20
    )

password_field = Entry(
    page1,
    text = "password",
    font = ("Arial",10),
    width = 20,
    show="*"
    )

save_button = Button(
    page1,
    text = "save",
    command = save_password
    )

deleteal_button = Button(
    page1,
    text = "Clear All",
    command = delete_password
    )

first = Button(
    page_button_frame,
    text = "1",
    width = 10,
    command = page1.tkraise
)

second = Button(
    page_button_frame,
    text = "2",
    width = 10,
    command = show_page2
)

label2 = Label(
    page2,
    text = "View Password",
    font = ("Arial",10)
)

label22 = Label(
    page2,
    text = read_file(),
    font = ("Arial",10)
)

first.grid(row = 2,column = 0,)
second.grid(row = 2,column = 1)
label2.grid(row = 0, column = 0)
label22.grid(row = 1,column = 0)
username_title.grid(row = 0, column = 0, pady = 10)
username_field.grid(row = 0, column = 1, pady = 10)
password_title.grid(row = 1, column = 0, pady = 10)
password_field.grid(row = 1, column = 1, pady = 10)
save_button.grid(row = 2, column = 1, sticky = 'E',pady = 10)
deleteal_button.grid(row=3)

def main():
    '''Driver Code'''
    global master
    master.mainloop()

if __name__ == "__main__":
    main()
