'''app'''
from tkinter import *
from customtkinter import *
from PIL import Image
APP_FONT = ("K2D",24)
WHITE = "#E3F1FB"
BLUE = "#1650CC"
DARK_BLUE = "#17377D"
LIGHT_BLUE = "#8AA7E6"

class App(CTk):
    '''App Class'''
    def __init__(self):
        '''Contructor'''
        super().__init__(fg_color = WHITE)

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
            fg_color = BLUE,
            width = 310,
            corner_radius = 0
        )

        CTkFrame( #Padding
            self,
            fg_color = BLUE,
            width = 310,
            height= 40,
            corner_radius = 0
        ).pack(side = "top")

        title_frame = TitleFrame(self)
        title_frame.pack(side = "top",fill = "y")

class TitleFrame(CTkFrame):
    '''Menu Title Frame Class'''
    def __init__(self,master):
        super().__init__(
            master,
            fg_color = BLUE,
            width = 270,
            height = 59,
            corner_radius = 0
        )
        self.pack_propagate(0)

        titlemenu = CTkFrame(self, fg_color = BLUE)
        titlemenu.pack(side = "top")

        menu_image = CTkImage(light_image=Image.open("Assets/Menu.png"),size = (40,40))
        menu_label = CTkLabel(titlemenu, image = menu_image,text = "")
        menu_label.pack(side = "left")

        title_label =  CTkLabel(
            titlemenu,
            text = "ENCRYPT|MINDS",
            text_color = DARK_BLUE,
            font = APP_FONT,
            width = 310,
            height = 10,
            fg_color = WHITE,
            corner_radius = 10
        )
        title_label.pack(side = "left", padx = (10,0))

        line = CTkFrame(self, height = 2, width = 258, fg_color = LIGHT_BLUE)
        line.pack(side = "top",fill = "both",pady = (10,0))

def run():
    '''Driver Code'''
    global APP_FONT
    app = App()
    app.mainloop()
if __name__ == "__main__":
    run()
