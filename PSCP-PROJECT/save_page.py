'''save_page'''
import os
import save
from tkinter import *
from customtkinter import *
from PIL import Image
from style import *

class SavePage(CTkFrame):
    '''SavePage Class'''
    def __init__(self,master):
        '''Contructor'''
        super().__init__(
            master,
            fg_color = WHITE,
            corner_radius = 0
        )
        self.pack_propagate(0)
        
def __main():
    '''Driver Code'''

if __name__ == "__main__":
    __main()
