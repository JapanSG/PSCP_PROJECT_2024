import customtkinter as ctk
import time

def generate_password():
    start_time = time.time()

    end_time = time.time()

    time_label.configure(text=f"{end_time - start_time:.10f}s")

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.title("Password Generator")


app.geometry("1024x768")


generate_button = ctk.CTkButton(app, text="Generate",command=generate_password,height=51, width=154,corner_radius=30,font=("K2D",24))
generate_button.pack(anchor="center", side="top",expand=True)


time_label = ctk.CTkLabel(app, text="",font=("K2D",14),text_color="#878787")
time_label.pack(anchor="center",expand=True)

app.mainloop()