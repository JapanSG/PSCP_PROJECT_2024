from customtkinter import *
import time
import threading
import string
import random
from PIL import Image
import os
from save import add_password
PATH = os.path.dirname(os.path.dirname(__file__))
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
        self.entry_web_value = StringVar(value="")
        self.entry_user_value = StringVar(value="")
        self.create_ui()

    def create_ui(self):
        self.create_topic()
        self.create_checkboxes()
        self.create_password_length()
        self.create_difficulty_buttons()
        self.create_password_button()
        self.create_site_entry()
        self.create_username_entry()
        self.create_result_label()
        self.create_copy_button()
        self.create_save_botton()
        self.create_time_label()
        self.create_check_button()
        self.master.bind("<Button-1>", self.hide_cursor)

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

        e = CTkButton(button_frame, text="Easy", font=H1, command=self.boxeasy, fg_color="#E3F1FB", text_color="#17377D", hover_color="#72D1D7")
        e.pack(side=LEFT, padx=(10, 5))

        m = CTkButton(button_frame, text="Medium", font=H1, command=self.boxmedium, fg_color="#E3F1FB", text_color="#17377D", hover_color="#72D1D7")
        m.pack(side=LEFT, padx=(82, 5))

        h = CTkButton(button_frame, text="Hard", font=H1, command=self.boxhard, fg_color="#E3F1FB", text_color="#17377D", hover_color="#72D1D7")
        h.pack(side=LEFT, padx=(80, 10))


    def boxeasy(self):
        self.slider.set(4)
        self.length_label_var.set(4)
        self.check_lower.set("on")
        self.check_digits.set("on")
        self.check_upper.set("off")
        self.check_punctuation.set("off")
        self.reset_placeholders()

    def boxmedium(self):
        self.slider.set(8)
        self.length_label_var.set(8)
        self.check_lower.set("on")
        self.check_upper.set("on")
        self.check_digits.set("on")
        self.check_punctuation.set("off")
        self.reset_placeholders()

    def boxhard(self):
        self.slider.set(12)
        self.length_label_var.set(12)
        self.check_lower.set("on")
        self.check_upper.set("on")
        self.check_digits.set("on")
        self.check_punctuation.set("on")
        self.reset_placeholders()

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

    def create_site_entry(self):
        self.site_entry = CTkEntry(
            self.frame,
            width=432,
            height=37,
            corner_radius=10,
            font=("K2D", 20),
            text_color="#4969AE",
            fg_color="#BDE4FF",
            border_width=0,
            textvariable=self.entry_web_value
        )
        self.site_entry.insert(0, "Enter your site")
        self.site_entry.bind("<FocusIn>", self.clear_site_placeholder)
        self.site_entry.bind("<FocusOut>", self.set_site_placeholder)
        self.site_entry.grid(row=8, column=0, columnspan=2, pady=(10, 10))

        self.frame.update()

    def clear_placeholder(self, event):
        if self.site_entry.get() == "Enter your site":
            self.site_entry.delete(0, END)

    def set_placeholder(self, event):
        if self.site_entry.get() == "":
            self.site_entry.insert(0, "Enter your site")

    def clear_site_placeholder(self, event):
        if self.site_entry.get() == "Enter your site":
            self.site_entry.delete(0, "end")
            self.site_entry.configure(fg_color="#BDE4FF")

    def set_site_placeholder(self, event):
        if self.site_entry.get() == "":
            self.site_entry.insert(0, "Enter your site")
            self.site_entry.configure(fg_color="#BDE4FF")

    def hide_cursor(self, event):
        if self.site_entry.get() == "":
            self.site_entry.insert(0, "Enter your site")
        if self.username_entry.get() == "":
            self.username_entry.insert(0, "Enter your username")

    def create_username_entry(self):

        self.username_entry = CTkEntry(
            self.frame,
            width=432,
            height=37,
            corner_radius=10,
            font=("K2D", 20),
            text_color="#4969AE",
            fg_color="#BDE4FF",
            border_width=0,
            textvariable=self.entry_user_value
        )
        self.username_entry.insert(0, "Enter your username")
        self.username_entry.bind("<FocusIn>", self.clear_username_placeholder)
        self.username_entry.bind("<FocusOut>", self.set_username_placeholder)
        self.username_entry.grid(row=9, column=0, columnspan=2, pady=(10, 10))

        self.frame.update()

    def clear_username_placeholder(self, event):
        if self.username_entry.get() == "Enter your username":
            self.username_entry.delete(0, END)

    def set_username_placeholder(self, event):
        if self.username_entry.get() == "":
            self.username_entry.insert(0, "Enter your username")


    def create_result_label(self):
        self.label_result = CTkLabel(
            self.frame,
            text="Your Password",
            width=324,
            height=37,
            text_color="#71797e",
            font=("K2D", 20),
            fg_color=("#E3F1FB"),
            anchor=CENTER,
            corner_radius=10
        )
        self.label_result.grid(row=10, column=0, columnspan=2, pady=(10, 10), sticky="w", padx=(90,10))

    def create_save_botton(self):
        self.save_button = CTkButton(
            self.frame,
            text="Save",
            command=self.save_password,
            height=37,
            width=80,
            corner_radius=30,
            font=("K2D", 20),
            fg_color="#9F2546",
            hover_color="#6F1A2B"
        )
        self.save_button.grid(row=10, column=1, padx=(150, 10), pady=(10, 10))

    def create_time_label(self):
        self.time_label.grid(row=11, column=0, columnspan=2, pady=(10, 10))

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
        self.check_button.grid(row=12, column=0, columnspan=2, pady=(10, 20))

    def create_copy_button(self):
        self.copy_image = CTkImage(light_image=Image.open(os.path.join(PATH,"Assets/content_copy.png")),size = (20,20))
        self.copy_image_hover = CTkImage(light_image=Image.open(os.path.join(PATH, "Assets/content_copyW.png")), size=(20, 20))

        result = CTkButton(
            master=self.frame,
            width=20,
            height=20,
            fg_color="#E3F1FB",
            command=self.copys,
            text="",
            image=self.copy_image,
            corner_radius=0,
            hover_color="#E3F1FB"
        )
        result.place(in_=self.label_result, relx=0.95, rely=0.5, anchor="center")

        result.bind("<Enter>", lambda event: self.on_enter(result))
        result.bind("<Leave>", lambda event: self.on_leave(result))

    def on_enter(self, button):
        button.configure(image=self.copy_image_hover)

    def on_leave(self, button):
        button.configure(image=self.copy_image)

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
        self.reset_placeholders()
        return charlist

    def copys(self):
        text = self.text_result.get()
        if text == "No character set selected!" or text == "":
            self.label_result.configure(text="Nothing to copy!")
            self.label_result.after(1000, lambda: self.label_result.configure(text="Your Password"))
        else:
            self.master.clipboard_clear()
            self.master.clipboard_append(text)
            self.reset_placeholders()
            self.show_copied_feedback()

    def show_copied_feedback(self):
        original_text = self.label_result.cget("text")
        self.label_result.configure(text="Copied!")
        self.label_result.after(1000, lambda: self.label_result.configure(text=original_text))


    def generate_password(self):
        start_time = time.time()
        charlist = self.check()
        if charlist:
            password_length = int(self.slider.get())
            password = ''.join(random.choice(charlist) for _ in range(password_length))
            self.text_result.set(password)
            self.label_result.configure(text=password)
            self.check_button.configure(text="Check Password Strength", fg_color="#17377D")

            if self.site_entry.get() == "":
                self.site_entry.insert(0, "Enter your site")
            if self.username_entry.get() == "":
                self.username_entry.insert(0, "Enter your username")
            end_time = time.time()
            elapsed_time = end_time - start_time
            self.time_label.configure(text=f"{elapsed_time:.10f}s")
        else:
            self.text_result.set("No character set selected!")
            self.label_result.configure(text="No character set selected!")
            if self.site_entry.get() == "":
                self.site_entry.insert(0, "Enter your site")
            if self.username_entry.get() == "":
                self.username_entry.insert(0, "Enter your username")

            self.time_label.configure(text="")

    def run_generate_password(self):
        if self.site_entry.get() == "Enter your site":
            self.site_entry.delete(0, "end")
        
        if self.username_entry.get() == "Enter your username":
            self.username_entry.delete(0, "end")
    
        threading.Thread(target=self.generate_password).start()

    def update_length_label(self, value):
        self.length_label_var.set(int(float(value)))
        self.reset_placeholders()

    def run_password_check(self):
        password = self.text_result.get()
        if password == "No character set selected!" or password == "" :
            self.check_button.configure(text="Check Password Strength", fg_color="#17377D")
        else:
            strength = self.check_password_strength(password)
            self.check_button.configure(text=strength, fg_color=self.get_strength_color(strength))

        if self.site_entry.get() == "":
            self.site_entry.insert(0, "Enter your site")
    
        if self.username_entry.get() == "":
            self.username_entry.insert(0, "Enter your username")


    def check_password_strength(self, password):
        score = 0
        countlower = 0
        countupper = 0
        countnum = 0
        countsymbol = 0
        symbols = {'', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', '|', '\\', ':', ';', '"', '\'', '<', ',', '>', '.', '?', '/'}

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

    def reset_placeholders(self):
        if self.site_entry.get() == "":
            self.site_entry.insert(0, "Enter your site")
        if self.username_entry.get() == "":
            self.username_entry.insert(0, "Enter your username")


    def save_password(self):
        self.reset_placeholders()
        add_password(self.entry_web_value,self.entry_user_value,self.text_result)
     


if __name__ == "__main__":
    root = CTk()
    root.geometry("1024x768")
    app = PasswordTool(root)
    root.mainloop()
