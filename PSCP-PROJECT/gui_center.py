import customtkinter as ctk
import time

def check_password_strength(password):
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

def on_check_button_click():
    password = password_entry.get()
    strength = check_password_strength(password)

    if strength == "very weak":
        check_button.configure(text=strength, fg_color="red")
    elif strength == "weak":
        check_button.configure(text=strength, fg_color="#FF8C00")
    elif strength == "good":
        check_button.configure(text=strength, fg_color="#DAA520")
    elif strength == "strong":
        check_button.configure(text=strength, fg_color="#66CC00")
    elif strength == "very strong":
        check_button.configure(text=strength, fg_color="green")

def generate_password():
    start_time = time.time()
    # โค้ดสร้างรหัสของ Fait & Mark
    end_time = time.time()
    time_label.configure(text=f"{end_time - start_time:.10f}s")

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Password Tool")
app.geometry("1024x768")


frame = ctk.CTkFrame(app, fg_color="transparent")
frame.pack(expand=True, anchor="center")


generate_button = ctk.CTkButton(frame, text="Generate", command=generate_password, height=51, width=154, corner_radius=30, font=("K2D", 24), fg_color="#17377D")
generate_button.pack(pady=(10, 10))


password_entry = ctk.CTkEntry(frame, placeholder_text="Your Password", height=37, width=421, corner_radius=10)
password_entry.pack(pady=(10, 10))


time_label = ctk.CTkLabel(frame, text="", font=("K2D", 14), text_color="#878787")
time_label.pack(pady=(10, 10))


check_button = ctk.CTkButton(frame, text="Check Password Strength", command=on_check_button_click, height=51, width=154, corner_radius=30, font=("K2D", 24), fg_color="#17377D")
check_button.pack(pady=(10, 20))

app.mainloop()
