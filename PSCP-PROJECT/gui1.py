from customtkinter import *
app = CTk()
app.title("Cartoon")
app.geometry("500x400")
app._set_appearance_mode("system")

frame = CTkFrame(master=app, fg_color="#27496D",border_color="#00A8CC",border_width=2)
frame.pack(expand=True)

label = CTkLabel(master=frame, text="Check Passwaord 🔎" ,text_color="#F0FFFF")
label.pack(anchor="s", expand=True,pady=10, padx=50)

def check() :
    txt = entry.get()
    if txt.isalpha() :
        if len(txt) >= 8 :
            label3 = CTkLabel(master=frame, text="☺ Pass ☺" ,text_color="#CCFFCC")
            label3.pack(anchor="s", expand=True,pady=10, padx=50)
        else :
            label3 = CTkLabel(master=frame, text="☹ Not Pass ☹", text_color="#FFCCFF")
            label3.pack(anchor="s", expand=True,pady=10, padx=50)

entry = CTkEntry(master=frame, placeholder_text="Your Password...", show="*")
entry.pack(anchor="s", expand=True, pady=10, padx=50)

btn = CTkButton(master=frame, text="Check now")
btn.configure(command=check) #เรียกใช้ฟังก์ชั่น
btn.pack(anchor="n", expand=True, pady=20, padx=50)

app.mainloop()
