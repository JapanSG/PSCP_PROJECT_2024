'''app'''
from tkinter import *
from customtkinter import *
from PIL import Image
H1 = ("K2D",24)
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
        title_frame.pack(side = "top",fill = "y",pady = (0,10))

        generate_icon = CTkImage(light_image=Image.open("Assets/Create.png"),size = (20,20))
        generate_btn = NavButton(self,"Generate",generate_icon)
        generate_btn.pack(side = "top",fill = "x", pady = (10,10))

        view_icon = CTkImage(light_image=Image.open("Assets/Remove red eye.png"),size = (20,20))
        view_btn = NavButton(self,"View",view_icon)
        view_btn.pack(side = "top",fill = "x", pady = (10,10))

        encrypt_icon = CTkImage(light_image=Image.open("Assets/Lock.png"),size = (20,20))
        encrypt_btn = NavButton(self,"Encrypt/Decrypt",encrypt_icon)
        encrypt_btn.pack(side = "top",fill = "x", pady = (10,10))
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
            font = H1,
            width = 310,
            height = 10,
            fg_color = WHITE,
            corner_radius = 10
        )
        title_label.pack(side = "left", padx = (10,0))

        line = CTkFrame(self, height = 2, width = 258, fg_color = LIGHT_BLUE)
        line.pack(side = "top",fill = "both",pady = (10,0))

class NavButton(CTkFrame):
    '''NavButton Class'''

    class MenuButton(CTkButton):
        '''MenuButton Class'''

        def __init__(self,master:CTkFrame,text:str = "CTkButton") -> None:
            '''Constructor'''
            super().__init__(
                master,
                width = 230,
                height = 40,
                text = text,
                font = H1,
                text_color = DARK_BLUE,
                bg_color = WHITE,
                fg_color = WHITE,
                hover = True,
                corner_radius = 0,
                border_color = WHITE,
                border_width = 0
            )

    def __init__(self, master:CTk, text:str, icon:CTkImage):
        '''Constructor'''
        super().__init__(
            master,
            width = 280,
            height = 40,
            bg_color = 'transparent',
            fg_color = 'transparent'
        )
        self.pack_propagate(0)

        btn = self.MenuButton(self,text = text)
        btn.pack(side = "left")
        
        img_frame = CTkFrame(self,
                       width = 50,
                       height = 40,
                       corner_radius = 30,
                       fg_color = WHITE,
                       border_color = WHITE,
                       border_width = 0,
                       background_corner_colors = (WHITE,BLUE,BLUE,WHITE)
        )
        img_frame.pack(side = "left")
        img_frame.pack_propagate(0)
        icon_label = CTkLabel(img_frame, image = icon,text = "")
        icon_label.pack(side = "left",expand = True)

def run():
    '''Driver Code'''
    global H1
    app = App()
    app.mainloop()
if __name__ == "__main__":
    run()
