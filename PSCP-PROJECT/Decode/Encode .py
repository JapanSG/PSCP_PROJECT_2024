"""decode encode prototype"""
import tkinter as tk # จะเปลี่ยนไปใช้ custommer
from tkinter import messagebox
import base64

def encode_message():
    "User's encode message" 
    message = entry_message.get()
    if not message:
        messagebox.showwarning("Please enter a message to encode.")
        return
    encoded_message = base64.b64encode(message.encode()).decode()
    entry_result.delete(0, tk.END)
    entry_result.insert(0, encoded_message)

def decode_message():
    ""
    encoded_message = entry_message.get()
    if not encoded_message:
        messagebox.showwarning("Please enter a message to decode.")
        return
    try:
        decoded_message = base64.b64decode(encoded_message.encode()).decode()
    except Exception as e:
        messagebox.showerror("Decode Error", f"Failed to decode: {e}")
        return
    entry_result.delete(0, tk.END)
    entry_result.insert(0, decoded_message)

root = tk.Tk()
root.title("Encoder/Decoder")

label_message = tk.Label(root, text="Message:")
label_message.grid(row=0, column=0, padx=10, pady=10)

entry_message = tk.Entry(root, width=50)
entry_message.grid(row=0, column=1, padx=10, pady=10)

button_encode = tk.Button(root, text="Encode", command=encode_message)
button_encode.grid(row=1, column=0, padx=10, pady=10)

button_decode = tk.Button(root, text="Decode", command=decode_message)
button_decode.grid(row=1, column=1, padx=10, pady=10)

label_result = tk.Label(root, text="Result:")
label_result.grid(row=2, column=0, padx=10, pady=10)

entry_result = tk.Entry(root, width=50)
entry_result.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()

