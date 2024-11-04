import customtkinter as ctk

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

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.title("Password Generator")


app.geometry("1024x768")

password_entry = ctk.CTkEntry(app, placeholder_text="Your Password", height=37, width=421, corner_radius=10)
password_entry.pack(anchor="center", side="top",expand=True)

check_button = ctk.CTkButton(app, text="Check Password Strength", command=on_check_button_click,height=51, width=154,corner_radius=30,font=("K2D",24))
check_button.pack(anchor="center",expand=True)

app.mainloop()