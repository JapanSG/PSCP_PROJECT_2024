import customtkinter
import tkinter
import string
import random
H1 = ("K2D",24)

class PasswordGeneratorApp:
    def __init__(self, master):
        '''Constructor that accepts a master widget'''
        self.master = master
        self.root = master
        self.check_upper = customtkinter.StringVar(value="off")
        self.check_lower = customtkinter.StringVar(value="off")
        self.check_digits = customtkinter.StringVar(value="off")
        self.check_punctuation = customtkinter.StringVar(value="off")
        self.text_result = tkinter.StringVar(value="")
        self.length_label_var = tkinter.StringVar(value="0")

        self.setup_ui()

    def setup_ui(self):
        self.create_checkboxes()
        self.create_password_button()
        self.create_result_label()
        self.create_slider()
        self.create_topic()
    def create_checkboxes(self):
        upper = customtkinter.CTkCheckBox(self.root, text="Uppercase", command=self.check,
                                          variable=self.check_upper, onvalue="on", offvalue="off",font=H1,text_color="white")
        lower = customtkinter.CTkCheckBox(self.root, text="Lowercase", command=self.check,
                                          variable=self.check_lower, onvalue="on", offvalue="off",font=H1,text_color="white")
        digits = customtkinter.CTkCheckBox(self.root, text="Digits", command=self.check,
                                           variable=self.check_digits, onvalue="on", offvalue="off",font=H1,text_color="white",width=50,height=50)
        punctuation = customtkinter.CTkCheckBox(self.root, text="Punctuation", command=self.check,
                                                variable=self.check_punctuation, onvalue="on", offvalue="off",font=H1,text_color="white",width=50,height=50)
        upper.place(relx=0.2, rely=0.2, anchor=tkinter.CENTER)
        lower.place(relx=0.2, rely=0.3, anchor=tkinter.CENTER)
        digits.place(relx=0.7, rely=0.2, anchor=tkinter.CENTER)
        punctuation.place(relx=0.7, rely=0.3, anchor=tkinter.CENTER)

    def create_password_button(self):
        button = customtkinter.CTkButton(master=self.root, width=120, height=32, border_width=0,
                                         corner_radius=8, text="Generate", command=self.show_password)
        button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def create_result_label(self):
        label_result = customtkinter.CTkLabel(master=self.root, textvariable=self.text_result,
                                              width=220, height=60, text_color="black",
                                              font=H1, fg_color=("blue"))
        label_result.place(relx=0.55, rely=0.9, anchor=tkinter.CENTER)


    def create_slider(self):
        length_label = customtkinter.CTkLabel(self.root, textvariable=self.length_label_var, font=H1)
        length_label.place(relx=0.5, rely=0.37, anchor=tkinter.CENTER)

        slider_label = customtkinter.CTkLabel(self.root, text="Password Length", font=H1)
        slider_label.place(relx=0.5, rely=0.34, anchor=tkinter.CENTER)

        self.slider = customtkinter.CTkSlider(master=self.root, from_=0, to=20, number_of_steps=16,
                                              command=self.update_length_label)
        self.slider.set(0)  # Default length
        self.slider.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    def check(self):
        charlist = ''
        if self.check_upper.get() == 'on':
            charlist += string.ascii_uppercase
        if self.check_lower.get() == 'on':
            charlist += string.ascii_lowercase
        if self.check_digits.get() == 'on':
            charlist += string.digits
        if self.check_punctuation.get() == 'on':
            charlist += string.punctuation
        return charlist

    def show_password(self):
        charlist = self.check()
        if charlist:
            password_length = int(self.slider.get())
            password = ''.join(random.choice(charlist) for _ in range(password_length))
            self.text_result.set(password)
        else:
            self.text_result.set("No character set selected!")


    def update_length_label(self, value):
        self.length_label_var.set(int(float(value)))

    def create_topic(self):
        x = customtkinter.CTkLabel(
        master=self.root,
        text="Password Generator",
        corner_radius=60,
        font=("K2D", 30),
        fg_color="white",
        width=50,
        height=50
        )
        x.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        
if __name__ == "__main__":
    root = customtkinter.CTk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
