'''app'''
import os
from tkinter import *
from customtkinter import *
from PIL import Image
from Chisanupong import PasswordGeneratorApp
H1 = ("K2D",24)
WHITE = "#E3F1FB"
BLUE = "#1650CC"
DARK_BLUE = "#17377D"
LIGHT_BLUE = "#8AA7E6"

PATH = os.path.dirname(os.path.dirname(__file__))

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

pages ={
    1 : page1,
    2 : page2,
    3 : page3
}

curr_page = pages[1]

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
        self.page = curr_page(self)
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
        menu_image = CTkImage(light_image=Image.open(os.path.join(PATH,"Assets/Menu.png")),size = (40,40))
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

        generate_icon = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/Create.png")), size = (20,20))
        generate_iconW = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/CreateW.png")), size = (20,20))
        self.generate_btn = NavButton(self, master, pages[1], "Generate", generate_icon,generate_iconW)
        self.generate_btn.pack(side = "top",fill = "x", pady = (10,10))

        view_icon = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/Remove red eye.png")), size = (20,20))
        view_iconW = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/Remove red eyeW.png")), size = (20,20))
        self.view_btn = NavButton(self,master, pages[2], "View", view_icon,view_iconW)
        self.view_btn.pack(side = "top",fill = "x", pady = (10,10))

        encrypt_icon = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/Lock.png")), size = (20,20))
        encrypt_iconW = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/LockW.png")), size = (20,20))
        self.encrypt_btn = NavButton(self,master, pages[3], "Encrypt/Decrypt", encrypt_icon, encrypt_iconW)
        self.encrypt_btn.pack(side = "top",fill = "x", pady = (10,10))

    def reset_all_btn(self):
        '''Reset all buttons in NavBar to original color and text color'''
        def reset_btn(btn:NavButton):
            '''Reset individul button'''
            btn.btn.configure(
            fg_color = WHITE,
            bg_color = WHITE,
            text_color = DARK_BLUE
            )
            btn.img_frame.configure(
            fg_color = WHITE,
            background_corner_colors = (WHITE,BLUE,BLUE,WHITE)
            )
            btn.icon_label.configure(
                image = btn.img
            )
        reset_btn(self.generate_btn)
        reset_btn(self.view_btn)
        reset_btn(self.encrypt_btn)

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

        menu_image = CTkImage(light_image=Image.open(os.path.join(PATH,"Assets/Menu.png")),size = (40,40))
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
                command = lambda : master.change_page(app,page)
            )

    def __init__(self, master:CTk, app:App, page, text:str, icon:CTkImage, iconW:CTkImage):
        '''Constructor'''
        super().__init__(
            master,
            width = 280,
            height = 40,
            bg_color = 'transparent',
            fg_color = 'transparent'
        )
        self.pack_propagate(0)

        self.btn = self.MenuButton(self, app, page, text = text)
        self.btn.pack(side = "left")
        
        self.img_frame = CTkFrame(self,
                       width = 50,
                       height = 40,
                       corner_radius = 30,
                       fg_color = WHITE,
                       border_color = WHITE,
                       border_width = 0,
                       background_corner_colors = (WHITE,BLUE,BLUE,WHITE)
        )
        self.img_frame.pack(side = "left")
        self.img_frame.pack_propagate(0)
        self.img = icon
        self.imgW = iconW
        self.icon_label = CTkLabel(self.img_frame, image = icon,text = "")
        self.icon_label.pack(side = "left",expand = True)

    def change_page(self,app:App,page:CTk):
        '''Change page'''
        global curr_page
        app.page.destroy()
        app.page = page(app)
        app.page.pack(side ='left',expand = True, fill = "both")
        app.navbar.reset_all_btn()
        self.btn.configure(
            text_color = WHITE,
            fg_color = DARK_BLUE,
            bg_color = DARK_BLUE
        )
        self.img_frame.configure(
            fg_color = DARK_BLUE,
            background_corner_colors = (DARK_BLUE,BLUE,BLUE,DARK_BLUE)
        )
        self.icon_label.configure(
            image = self.imgW
        )
        curr_page = page
        
def run():
    '''Driver Code'''
    app = App()
    app.mainloop()
if __name__ == "__main__":
    run()
