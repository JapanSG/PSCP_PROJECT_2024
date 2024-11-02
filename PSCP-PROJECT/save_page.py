'''save_page'''
import os
import save
from tkinter import *
from customtkinter import *
from PIL import Image
from style import *

PATH = os.path.dirname(os.path.dirname(__file__))

## Main Save Page
class SavePage(CTkFrame):
    '''SavePage Class'''
    def __init__(self,master):
        '''Contructor'''
        super().__init__(
            master,
            fg_color = WHITE,
            corner_radius = 0
        )
        self.scroll = CTkScrollableFrame(self, fg_color=WHITE, width = 1000, height = 1000, corner_radius = 0)
        self.scroll.pack(side = "left", expand = True)
        self.label = CTkLabel(self.scroll, text = "Password Viewer", text_color = DARK_BLUE, font = H1_BOLD)
        self.label.pack(side = "top",pady = (40,15))
        self.list = CTkFrame(self.scroll, fg_color = BLUE, corner_radius=30, width = 421, height = 1000)
        self.list.pack(side = "top", pady = (0,10), ipadx = 10, ipady = 20)
        passwords = save.read_file()
        if not passwords:
            error = CTkLabel(self.list,text = "There is no Password", width = 365, font = H1_BOLD, text_color = WHITE)
            error.pack_propagate(0)
            error.pack(side = "top", pady = (20,0))
            return
        for key in passwords:
            frame = ViewPassButton(self.list, passwords[key]["website"], key, master)
            frame.pack(side = "top", pady = (20,0))
            line = CTkFrame(self.list,fg_color=WHITE,width = 365, height = 2)
            line.pack_propagate(0)
            line.pack(side = "top")

class ViewPassButton(CTkFrame):
    '''View password for a specific website'''
    def __init__(self, master, site:str, key:int, app):
        '''Constructor'''
        super().__init__(
            master,
            fg_color = BLUE,
            corner_radius = 0,
            width = 401,
            height = 23
        )
        self.key = key
        self.site = site
        self.pack_propagate(0)
        arrow_img = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/Keyboard arrow right.png")), size = (20,20))
        site_label = CTkLabel(self,text = site,font = H2)
        site_label.pack(side = "left",padx = (30))
        self.arrow = CTkButton(self,image = arrow_img,text = "",width = 10, height = 10, fg_color=BLUE, command = lambda : self.view(app))
        self.arrow.pack(side ="right",padx = (10))

    def view(self, master) -> None:
        '''Button to change page to view password website and username'''
        master.page.destroy()
        master.page = ViewPasswordPage(master,self.key)
        master.page.pack(side = "left", expand = True, fill = "both")

## View Password Page
class ViewPasswordPage(CTkFrame):
    '''View Password Page'''
    def __init__(self, master, num:int) -> None:
        '''Constructor'''
        super().__init__(
            master,
            fg_color = WHITE,
            corner_radius = 0
        )
        password = save.get_pass(num)
        self.label_frame = LabelFrame(self, password["website"], master)
        self.label_frame.pack(side = "top", fill = "x", padx = (70,70),pady = (40,25))
        self.box = InformationBox(self, password)
        self.box.pack(side = "top")

class LabelFrame(CTkFrame):
    '''Label Frame'''
    def __init__(self, master, site:str, app):
        '''Constructor'''
        super().__init__(
            master,
            fg_color = WHITE,
            corner_radius = 0,
            height = 50
        )
        arrow = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/chevron_backward.png")), size = (50,50))
        self.back_button = CTkButton(self, image = arrow, text = "", width = 50, height = 50, fg_color=WHITE, command = lambda : LabelFrame.go_back(app))
        self.back_button.pack(side = "left")
        self.label = CTkLabel(self, text = f"https://{site}", font = H1_BOLD, text_color = DARK_BLUE, height = 50)
        self.label.pack(side = "left")

    def go_back(app):
        '''Go back to SavePage'''
        app.page.destroy()
        app.page = SavePage(app)
        app.page.pack(side = 'left')

class InformationBox(CTkFrame):
    '''information_box'''
    def __init__(self, master, data:dict):
        '''Constructor'''
        super().__init__(
            master,
            fg_color = BLUE,
            width = 490,
            height = 271,
            corner_radius = 30
        )
        self.pack_propagate(0)
        self.copy = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/content_copy.png")), size = (20,20))

        self.globe = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/Language.png")), size = (20,20))
        self.sites = Field(self, "Sites", self.globe, data["website"], [self.copy])
        self.sites.pack(side = "top", pady = (30,0))

        self.person = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/Person.png")), size = (20,20))
        self.username = Field(self, "Username", self.person, data["username"], [self.copy])
        self.username.pack(side = "top", pady = (30,0))

        self.key = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/Key.png")), size = (20,20))
        self.eye = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/Remove red eye.png")), size = (20,20))
        self.password = Field(self, "Password", self.key, data["password"], [self.eye, self.copy])
        self.password.pack(side = "top", pady = (30,0))

class Field(CTkFrame):
    '''Field for displaying information'''
    def __init__(self, master ,label : str, icon : CTkImage, data : str, buttons : list = []): #buttons = (icon1,icon2) (CTkImage,CTkImage)
        '''Constructor'''
        super().__init__(
            master,
            fg_color = BLUE,
            width = 272,
            height = 37
        )
        self.label = CTkLabel(self, text = label, fg_color = "transparent", font = P_BOLD, text_color = WHITE)
        self.label.grid(column = 0, row = 0, sticky = "w")

        self.field = CTkFrame(self, fg_color = WHITE, corner_radius = 30, width = 272, height = 21,)
        self.field.propagate(0)
        self.field.grid(column = 0, row = 1, sticky = "w",ipadx = 20, ipady = 1)

        self.icon = CTkLabel(self.field, text = "", image = icon, fg_color = "transparent", width = 20, height = 20)
        self.icon.pack(side = "left", padx = (20,10))

        self.data = CTkLabel(self.field, text = data, font = P_BOLD, text_color = DARK_BLUE, fg_color = "transparent")
        self.data.pack(side = "left", padx = 10)

        self.icon = [CTkButton(self.field, text = "", image = button_icon, fg_color = "transparent", width = 10, height = 20)  for button_icon in buttons]
        for i in self.icon:
            i.pack(side = "right", padx = (0,20))

def __main():
    '''Driver Code'''

if __name__ == "__main__":
    __main()
