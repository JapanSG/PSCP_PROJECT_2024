'''app'''
from tkinter import *
from customtkinter import *
from PIL import Image
APP_FONT = ("K2D",24)

class App(CTk):
    '''App Class'''
    def __init__(self):
        '''Contructor'''
        super().__init__(fg_color="#E3F1FB")

        self.geometry("1024x768")
        self.title("Password Generator")
        self.resizable(width =False, height = False)
        navbar = NavBar(self)
        navbar.pack(side = "left",fill = "y")
        navbar.pack_propagate(False)

class NavBar(CTkFrame):
    '''NavBar Class'''
    def __init__(self,master:CTk):
        '''Contructor'''
        super().__init__(
            master,
            fg_color = "#1650CC",
            width = 310,
            corner_radius = 0
        )
        
        CTkFrame( #Padding
            self,
            fg_color = "#1650CC",
            width = 310,
            height= 40,
            corner_radius = 0
        ).pack(side = "top")

        title_frame = TitleFrame(self)
        title_frame.pack(side = "top")
        menu_button = CTkImage(light_image=Image.open("Assets/Menu.png"))

class TitleFrame(CTkFrame):
    '''Menu Title Frame Class'''
    def __init__(self,master):
        super().__init__(
            master,
            fg_color = "#1600CC",
            width = 270,
            height = 50,
            corner_radius = 0
        )

def main():
    '''Driver Code'''
    global APP_FONT
    app = App()
    # bar = CTkFrame(
    #     app,
    #     fg_color = "#1650CC",
    #     width = 310,
    #     height = 768
    #     )


    # label = CTkLabel(
    #     bar,
    #     text = "ENCRYPT|MINDS",
    #     font = APP_FONT,
    #     width = 309,
    #     height = 10
    #     )

    # bar.pack(side = "left",fill = "both")
    # top_padding.pack(side = "top")
    # label.pack(side = "top")
    app.mainloop()
if __name__ == "__main__":
    main()
