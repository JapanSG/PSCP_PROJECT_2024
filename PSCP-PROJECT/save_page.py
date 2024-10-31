'''save_page'''
import os
import save
from tkinter import *
from customtkinter import *
from PIL import Image
from style import *

PATH = os.path.dirname(os.path.dirname(__file__))

class ViewPass(CTkFrame):
    '''View password for a specific website'''
    def __init__(self,master,site:str):
        '''Constructor'''
        super().__init__(
            master,
            fg_color = BLUE,
            corner_radius = 0,
            width = 401,
            height = 23
        )
        self.pack_propagate(0)
        arrow_img = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/Keyboard arrow right.png")), size = (20,20))
        self.site = site
        site_label = CTkLabel(self,text = site,font = P)
        site_label.pack(side = "left",padx = (30))
        self.arrow = CTkButton(self,image = arrow_img,text = "",width = 10, height = 10,fg_color=BLUE)
        self.arrow.pack(side ="right",padx = (10))

class SavePage(CTkFrame):
    '''SavePage Class'''
    def __init__(self,master):
        '''Contructor'''
        super().__init__(
            master,
            fg_color = WHITE,
            corner_radius = 0
        )
        self.scroll = CTkScrollableFrame(self,fg_color=WHITE,width = 1000,height = 1000,corner_radius = 0)
        self.scroll.pack(side = "left", expand = True)
        self.label = CTkLabel(self.scroll,text = "Password Viewer", text_color = DARK_BLUE, font = H1_BOLD)
        self.label.pack(side = "top",pady = (40,15))
        self.list = CTkFrame(self.scroll,fg_color = BLUE,corner_radius=30,width = 421,height = 1000)
        self.list.pack(side = "top",pady = (0,10),ipadx = 10,ipady = 20)
        passwords = save.read_file()
        for key in passwords:
            frame = ViewPass(self.list,passwords[key]["website"])
            frame.pack(side = "top", pady = (20,0))
            line = CTkFrame(self.list,fg_color=WHITE,width = 365, height = 2)
            line.pack_propagate(0)
            line.pack(side = "top")

def __main():
    '''Driver Code'''

if __name__ == "__main__":
    __main()
