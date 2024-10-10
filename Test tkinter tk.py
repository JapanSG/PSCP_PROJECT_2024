import random
import string
import tkinter as tk

def generate_password():
    try:
        length = int(length_entry.get())
        chars = {
            "easy": string.ascii_lowercase + string.digits,
            "medium": string.ascii_letters + string.digits,
            "hard": string.ascii_letters + string.digits + string.punctuation,
        }[difficulty_var.get()]
        password_entry.delete(0, tk.END)
        password_entry.insert(0, ''.join(random.choice(chars) for _ in range(length)))
    except ValueError:
        password_entry.insert(0, "Invalid length")

root = tk.Tk()
root.title("Password Generator")
root.geometry("350x250")
root.configure(bg="#e6f0ff")

tk.Label(root, text="Your Password", bg="#e6f0ff").pack(pady=10)
password_entry = tk.Entry(root, justify="center", font=("Helvetica", 14))
password_entry.pack(pady=5)

difficulty_var = tk.StringVar(value="easy")
tk.Radiobutton(root, text="easy", variable=difficulty_var, value="easy", indicatoron=0, width=8).pack(side="left", padx=5, pady=10)
tk.Radiobutton(root, text="medium", variable=difficulty_var, value="medium", indicatoron=0, width=8).pack(side="left", padx=5)
tk.Radiobutton(root, text="hard", variable=difficulty_var, value="hard", indicatoron=0, width=8).pack(side="left", padx=5)

tk.Label(root, text="Length of Password:", bg="#e6f0ff").pack()
length_entry = tk.Entry(root, width=5, justify="center")
length_entry.insert(0, "8")
length_entry.pack()

tk.Button(root, text="Generate", command=generate_password).pack(pady=20)
root.mainloop()
