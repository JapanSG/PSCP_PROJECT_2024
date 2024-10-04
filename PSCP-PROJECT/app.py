'''app'''
from tkinter import *
from customtkinter import *

def main():
    '''Driver Code'''
    app_font = ("K2D",24)
    app = CTk()
    app.geometry("1024x768")
    app.title("Password Generator")
    bar = CTkFrame(
        app,
        fg_color = "#1650CC",
        width = 310,
        height = 768
        )

    top_padding = CTkFrame(
        bar,
        fg_color = "#1650CC",
        width = 309,
        height= 40,
    )

    label = CTkLabel(
        bar,
        text = "ENCRYPT|MINDS",
        font = app_font,
        width = 309,
        height = 10
        )

    bar.pack(side = "left",fill = "both")
    top_padding.pack(side = "top")
    label.pack(side = "top")
    app.mainloop()
if __name__ == "__main__":
    main()
