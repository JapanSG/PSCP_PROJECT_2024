from customtkinter import *
from PIL import Image, ImageTk  # Import Image and ImageTk to handle images

H1 = ("K2D", 24)
PATH = os.path.dirname(os.path.dirname(__file__))

class EditPopup:
    def __init__(self, master):
        # Create the popup window
        self.popup = CTkToplevel(master)
        self.popup.geometry("350x300")
        self.popup.title("Edit")
        self.popup.configure(bg_color="white")  # Change background color

        # Widgets inside the popup
        CTkLabel(self.popup, text="Sites", font=("K2D", 14)).pack(pady=(10, 0))

        # Site Entry with Icon
        self.site_icon = CTkImage(light_image=Image.open(os.path.join(PATH,"Assets/Language.png"))) # Adjust icon size as needed
        site_frame = CTkFrame(self.popup)
        site_frame.pack(pady=5)
        site_label = CTkLabel(site_frame, image=self.site_icon, text="", compound="left")  # Combine icon and text
        site_label.pack(side="left", padx = (10,10))
        self.site_entry = CTkEntry(site_frame, width=200)
        self.site_entry.insert(0, "")
        self.site_entry.pack(side="right")

        CTkLabel(self.popup, text="Username", font=("K2D", 14)).pack(pady=(10, 0))

        # Username Entry with Icon
        self.username_icon = CTkImage(light_image=Image.open(os.path.join(PATH,"Assets/Person.png"))) # Adjust icon size as needed
        username_frame = CTkFrame(self.popup)
        username_frame.pack(pady=5)
        username_label = CTkLabel(username_frame, image=self.username_icon, text="", compound="left")
        username_label.pack(side="left", padx = (10,10))
        self.username_entry = CTkEntry(username_frame, width=200)
        self.username_entry.insert(0, "")
        self.username_entry.pack(side="right")

        CTkLabel(self.popup, text="Password", font=("K2D", 14)).pack(pady=(10, 0))

        # Password Entry with Icon
        self.password_icon = CTkImage(light_image=Image.open(os.path.join(PATH,"Assets/Key.png")))  # Adjust icon size as needed
        password_frame = CTkFrame(self.popup)
        password_frame.pack(pady=5)
        password_label = CTkLabel(password_frame, image=self.password_icon, text="", compound="left")
        password_label.pack(side="left", padx = (10,10))
        self.password_entry = CTkEntry(password_frame, show="*", width=200)
        self.password_entry.insert(0, "")
        self.password_entry.pack(side="left")
        
        self.show_icon = CTkImage(light_image=Image.open(os.path.join(PATH,"Assets/visibility_off.png")))
        self.show_password_button = CTkButton(password_frame, text="",fg_color = "transparent", command=self.toggle_password_visibility, width=10,image=self.show_icon)
        self.show_password_button.pack(side="left", padx=(5, 5))
        self.password_visible = False #ตัวแปรกำหนดค่าปุ่มshow/hid
        # Buttons
        button_frame = CTkFrame(self.popup, fg_color="transparent")
        button_frame.pack(pady=15)
        
        cancel_button = CTkButton(button_frame, text="Cancel", command=self.popup.destroy, width=100)
        cancel_button.pack(side="left", padx=5)

        confirm_button = CTkButton(button_frame, text="Confirm", command=self.on_confirm, width=100)
        confirm_button.pack(side="right", padx=5)


    def on_confirm(self):
        print(f"Site: {self.site_entry.get()}")
        print(f"Username: {self.username_entry.get()}")
        print(f"Password: {self.password_entry.get()}")
        self.popup.destroy()
    
    def toggle_password_visibility(self):
        if self.password_visible:
            self.password_entry.configure(show="*") # Hide the password
        else:
            self.password_entry.configure(show="") # Show the password
        self.password_visible = not self.password_visible # Toggle the state

if __name__ == "__main__":
    app = CTk()
    app.geometry("500x500")
    open_button = CTkButton(app, text="Open Edit Popup", command=lambda: EditPopup(app))
    open_button.pack(pady=20)

    app.mainloop()
