'''app'''
from tkinter import *
from customtkinter import *
from PIL import Image
from Chisanupong import PasswordGeneratorApp
H1 = ("K2D",24)
WHITE = "#E3F1FB"
BLUE = "#1650CC"
DARK_BLUE = "#17377D"
LIGHT_BLUE = "#8AA7E6"

class page1(CTkFrame):
    '''Page 1'''
    def __init__(self,master):
        '''Constructor'''
        super().__init__(master,fg_color=BLUE,corner_radius =50,border_color=WHITE,border_width=30)
        self.password_app = PasswordGeneratorApp(self)
class page2(CTkFrame):
    '''Page 2'''
    def __init__(self,master):
        '''Constructor'''
        super().__init__(master,fg_color= 'blue',corner_radius = 0)

class page3(CTkFrame):
    '''Page 3'''
    def __init__(self,master):
        '''Constructor'''
        super().__init__(master,fg_color= 'red',corner_radius = 0)

curr_page = page1

class App(CTk):
    '''App Class'''
    def __init__(self):
        '''Contructor'''
        super().__init__(fg_color = WHITE)

        self.geometry("1024x768")
        self.title("Password Generator")
        self.resizable(width =False, height = False)
        self.navbar = NavBar(self)
        self.navbar.pack(side = "left",fill = "y")
        self.navbar.pack_propagate(False)
        self.page = page1(self)
        self.page.pack(side = "left", expand = True,fill = "both")

class NavBarClose(CTkFrame):
    '''Closed NavBar'''

    def __init__(self,master:CTk):
        '''Contructor'''
        super().__init__(
            master,
            fg_color = BLUE,
            width = 70,
            corner_radius = 0
        )
        self.pack_propagate(0)
        menu_image = CTkImage(light_image=Image.open("Assets/Menu.png"),size = (40,40))
        menu_btn = CTkButton(self, image = menu_image,text = "",width=0,height= 0,fg_color=BLUE,command = lambda: NavBarClose.open(master))
        menu_btn.pack(side = "left",padx = (10,0))

    def open(app:App):
        '''open Menu'''
        global curr_page
        app.navbar.destroy()
        app.navbar = NavBar(app)
        app.navbar.pack(side = "left", fill = "y")
        app.page.destroy()
        app.page = curr_page(app)
        app.page.pack(side = "left", expand = True,fill = "both")

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

        title_frame = TitleFrame(self,master)
        title_frame.pack(side = "top",fill = "x",pady = (40,10))

        generate_icon = CTkImage(light_image = Image.open("Assets/Create.png"), size = (20,20))
        generate_btn = NavButton(self, master, page1, "Generate", generate_icon)
        generate_btn.pack(side = "top",fill = "x", pady = (10,10))

        view_icon = CTkImage(light_image = Image.open("Assets/Remove red eye.png"), size = (20,20))
        view_btn = NavButton(self,master, page2, "View", view_icon)
        view_btn.pack(side = "top",fill = "x", pady = (10,10))

        encrypt_icon = CTkImage(light_image = Image.open("Assets/Lock.png"), size = (20,20))
        encrypt_btn = NavButton(self,master, page3, "Encrypt/Decrypt", encrypt_icon)
        encrypt_btn.pack(side = "top",fill = "x", pady = (10,10))

class TitleFrame(CTkFrame):
    '''Menu Title Frame Class'''
    def __init__(self,master,app):
        super().__init__(
            master,
            fg_color = BLUE,
            width = 310,
            height = 60,
            corner_radius = 0
        )
        self.pack_propagate(0)

        titlemenu = CTkFrame(self, fg_color = BLUE,width = 310)
        titlemenu.pack(side = "top",fill = "x")

        menu_image = CTkImage(light_image=Image.open("Assets/Menu.png"),size = (40,40))
        menu_btn = CTkButton(titlemenu, image = menu_image,text = "",width=0,height= 0,fg_color=BLUE,command = lambda: TitleFrame.close(app))
        menu_btn.pack(side = "left",padx = (10,0))

        title_label =  CTkLabel(
            titlemenu,
            text = "ENCRYPT|MINDS",
            text_color = DARK_BLUE,
            font = H1,
            width = 208,
            height = 30,
            fg_color = WHITE,
            corner_radius = 10
        )
        title_label.pack(side = "left", padx = (10,0))

        line = CTkFrame(self, height = 2, width = 270, fg_color = LIGHT_BLUE)
        line.pack(side = "top",pady = (10,0))

    def close(app:App):
        '''close menu'''
        global curr_page
        app.navbar.destroy()
        app.navbar = NavBarClose(app)
        app.navbar.pack(side = "left",fill = "y")
        app.page.destroy()
        app.page = curr_page(app)
        app.page.pack(side = "left", expand = True, fill = "both")

class NavButton(CTkFrame):
    '''NavButton Class'''

    class MenuButton(CTkButton):
        '''MenuButton Class'''

        def __init__(self, master:CTkFrame, app:App, page, text:str = "CTkButton") -> None:
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
                hover = False,
                corner_radius = 0,
                border_color = WHITE,
                border_width = 0,
                command = lambda : NavButton.MenuButton.change_page(app,page)
            )

        def change_page(app:App,page):
            '''Change page'''
            global curr_page
            app.page.destroy()
            app.page = page(app)
            app.page.pack(side ='left',expand = True, fill = "both")
            curr_page = page

    def __init__(self, master:CTk, app:App, page, text:str, icon:CTkImage):
        '''Constructor'''
        super().__init__(
            master,
            width = 280,
            height = 40,
            bg_color = 'transparent',
            fg_color = 'transparent'
        )
        self.pack_propagate(0)

        btn = self.MenuButton(self, app, page, text = text)
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
