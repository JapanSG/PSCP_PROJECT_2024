import customtkinter
import tkinter
import string
import random


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TEST")
        self.root.geometry("500x500")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        self.check_upper = customtkinter.StringVar(value="off")
        self.check_lower = customtkinter.StringVar(value="off")
        self.check_digits = customtkinter.StringVar(value="off")
        self.check_punctuation = customtkinter.StringVar(value="off")
        self.text_result = tkinter.StringVar(value="")
        self.length_label_var = tkinter.StringVar(value="Length: 0")

        self.setup_ui()

    def setup_ui(self):
        self.create_checkboxes()
        self.create_password_button()
        self.create_result_label()
        self.create_toggle_entry_visibility()
        self.create_slider()

    def create_checkboxes(self):
        upper = customtkinter.CTkCheckBox(self.root, text="Uppercase", command=self.check,
                                          variable=self.check_upper, onvalue="on", offvalue="off")
        lower = customtkinter.CTkCheckBox(self.root, text="Lowercase", command=self.check,
                                          variable=self.check_lower, onvalue="on", offvalue="off")
        digits = customtkinter.CTkCheckBox(self.root, text="Digits", command=self.check,
                                           variable=self.check_digits, onvalue="on", offvalue="off")
        punctuation = customtkinter.CTkCheckBox(self.root, text="Punctuation", command=self.check,
                                                variable=self.check_punctuation, onvalue="on", offvalue="off")
        upper.place(relx=0.55, rely=0.4, anchor=tkinter.CENTER)
        lower.place(relx=0.55, rely=0.5, anchor=tkinter.CENTER)
        digits.place(relx=0.55, rely=0.6, anchor=tkinter.CENTER)
        punctuation.place(relx=0.55, rely=0.7, anchor=tkinter.CENTER)

    def create_password_button(self):
        button = customtkinter.CTkButton(master=self.root, width=120, height=32, border_width=0,
                                         corner_radius=8, text="Generate", command=self.show_password)
        button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def create_result_label(self):
        label_result = customtkinter.CTkLabel(master=self.root, textvariable=self.text_result,
                                              width=220, height=60, text_color="black",
                                              font=("Arial", 25), fg_color=("blue"))
        label_result.place(relx=0.55, rely=0.9, anchor=tkinter.CENTER)

    def create_toggle_entry_visibility(self):
        self.check_test = customtkinter.StringVar(value='off')
        self.entry = tkinter.Entry(self.root, show='*')
        self.entry.place(relx=0.55, rely=0.1)

        check_pass = customtkinter.CTkCheckBox(self.root, text="Show", command=self.toggle_entry_visibility,
                                               variable=self.check_test, onvalue='on', offvalue='off')
        check_pass.place(relx=0.55, rely=0.2)

    def create_slider(self):
        length_label = customtkinter.CTkLabel(self.root, textvariable=self.length_label_var, font=("Arial", 14))
        length_label.place(relx=0.5, rely=0.78, anchor=tkinter.CENTER)

        slider_label = customtkinter.CTkLabel(self.root, text="Password Length", font=("Arial", 16))
        slider_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        self.slider = customtkinter.CTkSlider(master=self.root, from_=0, to=20, number_of_steps=16,
                                              command=self.update_length_label)
        self.slider.set(0)  # Default length
        self.slider.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

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

    def toggle_entry_visibility(self):
        if self.check_test.get() == 'on':
            self.entry.config(show='')
        else:
            self.entry.config(show='*')

    def update_length_label(self, value):
        self.length_label_var.set(f"Length: {int(float(value))}")


if __name__ == "__main__":
    root = customtkinter.CTk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
