import customtkinter
import tkinter
import base64
from style import *

H1 = ("K2D", 24)

class EncodeDecodeApp:
    def __init__(self, master):
        '''Constructor that accepts a master widget'''
        self.master = master
        self.root = master
        self.text_input = tkinter.StringVar(value="")
        self.text_result = tkinter.StringVar(value="")
        self.setup_ui()

    def setup_ui(self):
        self.create_topic()
        self.create_input_box()
        self.create_result_label()
        self.create_encode_button()
        self.create_decode_button()
        self.create_copy_button()

    def create_topic(self):
        x = customtkinter.CTkLabel(
            master=self.root,
            text="Encode/Decode",
            corner_radius=60,
            font=("K2D", 30),
            fg_color= WHITE,
            text_color = DARK_BLUE,
            width=200,
            height=50
        )
        x.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    def create_input_box(self):
        input_label = customtkinter.CTkLabel(
            self.root, text="Input Message", font=H1, text_color="white"
        )
        input_label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        self.entry_input = customtkinter.CTkEntry(
            self.root, textvariable=self.text_input, width=400, height=40, corner_radius=8, fg_color="white", text_color="black"
        )
        self.entry_input.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    def create_result_label(self):
        label_result = customtkinter.CTkLabel(
            master=self.root,
            text="Result",
            font=H1,
            text_color="white"
        )
        label_result.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        self.result_output = customtkinter.CTkEntry(
            master=self.root,
            textvariable=self.text_result,
            width=400,
            height=40,
            fg_color="white",
            text_color="black",
            corner_radius=8
        )
        self.result_output.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def create_encode_button(self):
        encode_button = customtkinter.CTkButton(
            master=self.root,
            text="Encode",
            width=120,
            height=32,
            corner_radius=8,
            text_color = DARK_BLUE,
            fg_color="#34D399",
            hover_color="#059669",
            command=self.encode_message
        )
        encode_button.place(relx=0.4, rely=0.6, anchor=tkinter.CENTER)

    def create_decode_button(self):
        decode_button = customtkinter.CTkButton(
            master=self.root,
            text="Decode",
            width=120,
            height=32,
            corner_radius=8,
            text_color = DARK_BLUE,
            fg_color="#93C5FD",
            hover_color="#3B82F6",
            command=self.decode_message
        )
        decode_button.place(relx=0.6, rely=0.6, anchor=tkinter.CENTER)

    def create_copy_button(self):
        copy_button = customtkinter.CTkButton(
            master=self.root,
            text="COPY",
            width=80,
            height=32,
            fg_color="black",
            text_color="white",
            corner_radius=8,
            command=self.copy_to_clipboard
        )
        copy_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    def encode_message(self):
        message = self.text_input.get()
        if not message:
            self.text_result.set("Please enter a message to encode.")
            return
        encoded_message = base64.b64encode(message.encode()).decode()
        self.text_result.set(encoded_message)

    def decode_message(self):
        encoded_message = self.text_input.get()
        if not encoded_message:
            self.text_result.set("Please enter a message to decode.")
            return
        try:
            decoded_message = base64.b64decode(encoded_message.encode()).decode()
            self.text_result.set(decoded_message)
        except Exception as e:
            self.text_result.set(f"Decode Error: {e}")

    def copy_to_clipboard(self):
        text = self.text_result.get()
        self.root.clipboard_clear()
        self.root.clipboard_append(text)

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = EncodeDecodeApp(root)
    root.mainloop()

