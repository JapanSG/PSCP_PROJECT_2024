import customtkinter, tkinter
from tkinter import *
import string
import random
a = customtkinter.CTk()
a.title("TEST")
a.geometry("500x500")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
def check():
    charlist = ''
    if check_upper.get() == 'on':
        charlist+=string.ascii_uppercase
    if check_lower.get() == 'on':
        charlist+=string.ascii_lowercase
    if check_digits.get() == 'on':
        charlist+=string.digits
    if check_punctuation.get() == 'on':
        charlist+=string.punctuation
    return charlist

def showed():
    charlist = check()
    password = []
    for i in range(5):
        randoms = random.choice(charlist)
        password.append(randoms)
    text_result.set(''.join(password))
    
check_upper = customtkinter.StringVar(value="off")
check_lower = customtkinter.StringVar(value="off")
check_digits = customtkinter.StringVar(value="off")
check_punctuation = customtkinter.StringVar(value="off")
upper = customtkinter.CTkCheckBox(a,text="Uppercase",command=check,variable=check_upper,onvalue="on",offvalue="off")
lower = customtkinter.CTkCheckBox(a,text="Lowercase",command=check,variable=check_lower,onvalue="on",offvalue="off")
digits = customtkinter.CTkCheckBox(a,text="Digits",command=check,variable=check_digits,onvalue="on",offvalue="off")
punctuation = customtkinter.CTkCheckBox(a,text="Punctuation",command=check,variable=check_punctuation,onvalue="on",offvalue="off")
upper.place(relx=0.55,rely=0.4,anchor=tkinter.CENTER)
lower.place(relx=0.55,rely=0.5,anchor=tkinter.CENTER)
digits.place(relx=0.55,rely=0.6,anchor=tkinter.CENTER)
punctuation.place(relx=0.55,rely=0.7,anchor=tkinter.CENTER)
#ลองsystem
button = customtkinter.CTkButton(master=a,width=120,height=32,border_width=0,corner_radius=8,text="print",command=showed)
button.place(relx=0.5,rely=0.8,anchor=tkinter.CENTER)
text_result = tkinter.StringVar(value="")
label_result = customtkinter.CTkLabel(master=a,textvariable=text_result,
                                        width=220,height=60,text_color="black",font=("Arial",25),fg_color=("blue"))
label_result.place(relx=0.55,rely=0.9,anchor=tkinter.CENTER)
#ลองสร้างปิด/เปิดตา
def check():
    if check_test.get() == 'on':
        entry.config(show='')
    else:
        entry.config(show='*')
check_test = customtkinter.StringVar(value='off')
entry = Entry(a,show='*')
entry.place(relx=0.55,rely=0.1)
check_pass = customtkinter.CTkCheckBox(a,text="show",command=check,variable=check_test,onvalue='on',offvalue='off')
check_pass.place(relx=0.55,rely=0.2)

a.mainloop()