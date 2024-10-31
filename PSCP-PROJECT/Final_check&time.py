import customtkinter as ctk
import time
import threading

class PasswordTool:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Tool")
        self.master.geometry("1024x768")
        
        self.frame = ctk.CTkFrame(master, fg_color="transparent")
        self.frame.pack(expand=True, anchor="center")
        
        self.generate_button = ctk.CTkButton(
            self.frame, 
            text="Generate", 
            command=self.run_generate_password, 
            height=51, 
            width=154, 
            corner_radius=30, 
            font=("K2D", 24), 
            fg_color="#17377D"
        )
        self.generate_button.pack(pady=(466-150, 10))

        self.password_entry = ctk.CTkEntry(
            self.frame, 
            placeholder_text="Your Password", 
            height=37, 
            width=421, 
            corner_radius=10
        )
        self.password_entry.pack(pady=(10, 10))

        self.time_label = ctk.CTkLabel(
            self.frame, 
            text="", 
            font=("K2D", 14), 
            text_color="#878787"
        )
        self.time_label.pack(pady=(10, 10))

        self.check_button = ctk.CTkButton(
            self.frame, 
            text="Check Password Strength", 
            command=self.run_password_check, 
            height=51, 
            width=154, 
            corner_radius=30, 
            font=("K2D", 24), 
            fg_color="#17377D"
        )
        self.check_button.pack(pady=(10, 20))

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

    def on_check_button_click(self):
        password = self.password_entry.get()
        strength = self.check_password_strength(password)

        if strength == "very weak":
            self.check_button.configure(text=strength, fg_color="red")
        elif strength == "weak":
            self.check_button.configure(text=strength, fg_color="#FF8C00")
        elif strength == "good":
            self.check_button.configure(text=strength, fg_color="#DAA520")
        elif strength == "strong":
            self.check_button.configure(text=strength, fg_color="#66CC00")
        elif strength == "very strong":
            self.check_button.configure(text=strength, fg_color="green")

    def run_password_check(self):
        threading.Thread(target=self.on_check_button_click).start()

    def generate_password(self):
        start_time = time.time()
        # โค้ดสร้างรหัสของ Fait & Mark
        end_time = time.time()
        return end_time - start_time

    def run_generate_password(self):
        elapsed_time = self.generate_password()
        self.time_label.configure(text=f"{elapsed_time:.10f}s")

if __name__ == "__main__":
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    password_tool = PasswordTool(app)
    app.mainloop()
