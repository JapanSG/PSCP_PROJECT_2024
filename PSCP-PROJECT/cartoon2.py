from customtkinter import *
import time
import threading
import string
import random


H1 = ("K2D", 24)

class PasswordTool:
    def __init__(self, master):
        self.master = master

        self.frame = CTkFrame(master, fg_color="transparent")
        self.frame.pack(expand=True, anchor="center")

        self.length_label_var = StringVar(value="0")
        self.check_upper = StringVar(value="off")
        self.check_lower = StringVar(value="off")
        self.check_digits = StringVar(value="off")
        self.check_punctuation = StringVar(value="off")
        self.text_result = StringVar(value="")
        self.time_label = CTkLabel(self.frame, text="", font=("K2D", 14), text_color="#ebf2f5")

        self.create_ui()

    def create_ui(self):
        self.create_topic()
        self.create_checkboxes()
        self.create_password_length()
        self.create_difficulty_buttons()
        self.create_password_button()
        self.create_result_label()
        self.create_time_label()
        self.create_check_button()

    def create_topic(self):
        topic_frame = CTkFrame(self.frame, width=420, height=70, fg_color="#E3F1FB", corner_radius=30)
        topic_frame.grid(row=0, column=0, columnspan=2, pady=(10, 20), padx=(10, 10), sticky="nsew")
        
        topic_label = CTkLabel(
            topic_frame,
            text="Password Generator",
            font=("K2D", 36),
            text_color="#17377D"
        )
        topic_label.place(relx=0.5, rely=0.5, anchor="center")

    def create_checkboxes(self):
        upper = CTkCheckBox(self.frame, text="Uppercase", command=self.check,
                            variable=self.check_upper, onvalue="on", offvalue="off",
                            font=H1, text_color="white", border_color="white")
        lower = CTkCheckBox(self.frame, text="Lowercase", command=self.check,
                            variable=self.check_lower, onvalue="on", offvalue="off",
                            font=H1, text_color="white", border_color="white")
        digits = CTkCheckBox(self.frame, text="Digits", command=self.check,
                             variable=self.check_digits, onvalue="on", offvalue="off",
                             font=H1, text_color="white", border_color="white")
        punctuation = CTkCheckBox(self.frame, text="Punctuation", command=self.check,
                                  variable=self.check_punctuation, onvalue="on", offvalue="off",
                                  font=H1, text_color="white", border_color="white")

        upper.grid(row=1, column=0, padx=(10, 10), pady=(5, 5), sticky="w")
        lower.grid(row=2, column=0, padx=(10, 10), pady=(5, 5), sticky="w")
        digits.grid(row=1, column=1, padx=(200, 20), pady=(5, 5), sticky="w")
        punctuation.grid(row=2, column=1, padx=(200, 10), pady=(5, 5), sticky="w")

    def create_password_length(self):
        length_frame = CTkFrame(self.frame, width=83, height=40, fg_color="white", corner_radius=30)
        length_frame.grid(row=3, column=0, columnspan=2, pady=(10, 10))
        
        length_label = CTkLabel(length_frame, textvariable=self.length_label_var, font=H1, text_color="black")
        length_label.place(relx=0.5, rely=0.5, anchor="center")

        self.slider = CTkSlider(master=self.frame, from_=0, to=20, number_of_steps=20,
                                command=self.update_length_label, width=370)
        self.slider.set(0)
        self.slider.grid(row=4, column=0, columnspan=2, pady=(10, 10))

    def create_difficulty_buttons(self):
        button_frame = CTkFrame(self.frame, fg_color="transparent")
        button_frame.grid(row=5, column=0, columnspan=2, pady=(5, 5), sticky="nsew")

        e = CTkButton(button_frame, text="Easy", font=H1, command=self.boxeasy, fg_color="#E3F1FB", text_color="#17377D")
        e.pack(side=LEFT, padx=(10, 5))

        m = CTkButton(button_frame, text="Medium", font=H1, command=self.boxmedium, fg_color="#E3F1FB", text_color="#17377D")
        m.pack(side=LEFT, padx=(82, 5))

        h = CTkButton(button_frame, text="Hard", font=H1, command=self.boxhard, fg_color="#E3F1FB", text_color="#17377D")
        h.pack(side=LEFT, padx=(80, 10))


    def boxeasy(self):
        self.slider.set(4)
        self.length_label_var.set(4)
        self.check_lower.set("on")
        self.check_digits.set("on")
        self.check_upper.set("off")
        self.check_punctuation.set("off")

    def boxmedium(self):
        self.slider.set(8)
        self.length_label_var.set(8)
        self.check_lower.set("on")
        self.check_upper.set("on")
        self.check_digits.set("on")
        self.check_punctuation.set("off")

    def boxhard(self):
        self.slider.set(12)
        self.length_label_var.set(12)
        self.check_lower.set("on")
        self.check_upper.set("on")
        self.check_digits.set("on")
        self.check_punctuation.set("on")

    def create_password_button(self):
        self.generate_button = CTkButton(
            self.frame,
            text="Generate",
            command=self.run_generate_password,
            height=51,
            width=154,
            corner_radius=30,
            font=("K2D", 24),
            fg_color="#17377D"
        )
        self.generate_button.grid(row=7, column=0, columnspan=2, pady=(10, 10))

    def create_result_label(self):
        self.label_result = CTkLabel(
            self.frame,
            # textvariable=self.text_result,
            text="Your Password",
            width=324,
            height=37,
            text_color="#71797e",
            font=("K2D", 20),
            fg_color=("#E3F1FB"),
            anchor=CENTER,
            corner_radius=10
        )
        self.label_result.grid(row=8, column=0, columnspan=2, pady=(10, 10))

    def create_time_label(self):
        self.time_label.grid(row=9, column=0, columnspan=2, pady=(10, 10))

    def create_check_button(self):
        self.check_button = CTkButton(
            self.frame,
            text="Check Password Strength",
            command=self.run_password_check,
            height=51,
            width=154,
            corner_radius=30,
            font=("K2D", 24),
            fg_color="#17377D"
        )
        self.check_button.grid(row=10, column=0, columnspan=2, pady=(10, 20))

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

    def generate_password(self):
        start_time = time.time()
        charlist = self.check()
        if charlist:
            password_length = int(self.slider.get())
            password = ''.join(random.choice(charlist) for _ in range(password_length))
            self.text_result.set(password)

            self.label_result.configure(text=password)

            self.check_button.configure(text="Check Password Strength", fg_color="#17377D")
        else:
            self.text_result.set("No character set selected!")
            self.label_result.configure(text="Your Password")

        end_time = time.time()
        elapsed_time = end_time - start_time
        self.time_label.configure(text=f"{elapsed_time:.10f}s")

    def run_generate_password(self):
        threading.Thread(target=self.generate_password).start()

    def update_length_label(self, value):
        self.length_label_var.set(int(float(value)))

    def run_password_check(self):
        password = self.text_result.get()
        if password == "No character set selected!":
            self.check_button.configure(text="Check Password Strength", fg_color="#17377D")
        else:
            strength = self.check_password_strength(password)
            self.check_button.configure(text=strength, fg_color=self.get_strength_color(strength))

    def check_password_strength(self, password):
        score = 0
        countlower = 0
        countupper = 0
        countnum = 0
        countsymbol = 0
        symbols = {'`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', '|', '\\', ':', ';', '"', '\'', '<', ',', '>', '.', '?', '/'}

        if len(password) >= 8:
            score += 1
        if len(password) >= 12:
            score += 1

        for i in password:
            if i.islower():
                countlower += 1
            if i.isupper():
                countupper += 1
            if i.isnumeric():
                countnum += 1
            if i in symbols:
                countsymbol += 1

        if countlower:
            score += 1
        if countnum:
            score += 1
        if countupper:
            score += 1
        if countsymbol:
            score += 1

        if score <= 1:
            return "very weak"
        elif score == 2:
            return "weak"
        elif score == 3:
            return "good"
        elif 4 <= score <= 5:
            return "strong"
        else:
            return "very strong"

    def get_strength_color(self, strength):
        if strength == "very weak":
            return "red"
        elif strength == "weak":
            return "#FFA500"
        elif strength == "good":
            return "#dba72c"
        elif strength == "strong":
            return "#66CC00"
        else:
            return "green"


if __name__ == "__main__":
    root = CTk()
    root.geometry("1024x768")
    app = PasswordTool(root)
    root.mainloop()
