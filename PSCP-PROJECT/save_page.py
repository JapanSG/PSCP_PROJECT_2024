'''save_page'''
import os
import save
from tkinter import *
from customtkinter import *
from PIL import Image
from style import *
import setting

PATH = os.path.dirname(__file__)

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
        self.scroll = CTkScrollableFrame(self, fg_color=WHITE, width = 2000, height = 1000, corner_radius = 0)
        self.scroll.pack(side = "left", expand = True, fill = "x")
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
        setting.CURRPAGE = lambda app : ViewPasswordPage(app,self.key)

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
        self.box = InformationBox(self, password, num, master)
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
        setting.CURRPAGE = SavePage

class InformationBox(CTkFrame):
    '''information_box'''
    def __init__(self, master, data:dict, num: int, app):
        '''Constructor'''
        super().__init__(
            master,
            fg_color = BLUE,
            width = 490,
            height = 271,
            corner_radius = 30
        )
        self.num = num
        self.data = data
        self.pack_propagate(0)
        self.view = False
        ## fields
        self.format = CTkFrame(self,fg_color = BLUE)
        self.format.pack(side ="top", fill = "x", pady = (30,0))
        self.fields = CTkFrame(self.format, fg_color = BLUE)
        self.fields.pack(side = "left", padx = 20)
        self.copy = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/content_copy.png")), size = (20,20))

        self.globe = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/Language.png")), size = (20,20))
        self.sites = Field(self.fields, app, "Sites", self.globe, data["website"], [self.copy], [lambda : InformationBox.copy(app, data["website"])])
        self.sites.pack(side = "top")

        self.person = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/Person.png")), size = (20,20))
        self.username = Field(self.fields, app, "Username", self.person, data["username"], [self.copy], [lambda : InformationBox.copy(app, data["username"])])
        self.username.pack(side = "top", pady = (30,0))

        self.key = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/Key.png")), size = (20,20))
        self.eye = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/Remove red eye.png")), size = (20,20))
        self.password = Field(self.fields, app, "Password", self.key, "********", [self.eye, self.copy], [lambda : self.view_pass(app= app),lambda : InformationBox.copy(app, data["password"])])
        self.password.pack(side = "top", pady = (30,0))

        ## buttons
        self.buttons = CTkFrame(self.format, fg_color = BLUE)
        self.buttons.pack(side = "right", padx = (0,40))
        self.edit_btn = CTkButton(
            self.buttons,
            font = H2,
            text = "Edit",
            text_color = WHITE,
            fg_color = DARK_BLUE,
            corner_radius = 30,
            width = 104,
            height = 45,
            command = lambda : self.edit(app)
        )
        self.edit_btn.pack_propagate(0)
        self.edit_btn.pack(side = "top", pady = (20,0))

        self.delete_btn = CTkButton(
            self.buttons,
            font = H2,
            text = "Delete",
            text_color = WHITE,
            fg_color = RED,
            corner_radius = 30,
            width = 104,
            height = 45,
            command = lambda : InformationBox.delete(num,app)
        )
        self.delete_btn.pack_propagate(0)
        self.delete_btn.pack(side = "top", pady = (73,0))

    def delete(num,app):
        '''delete command'''
        save.del_pass(num)
        DelPopup(app)
        app.page.destroy()
        app.page = SavePage(app)
        app.page.pack(side = "left")
        setting.CURRPAGE = SavePage

    def copy(app, text: str):
        '''Copy to clip board'''
        app.clipboard_clear()
        app.clipboard_append(text)
        app.update()

    def view_pass(self, app):
        '''view pass'''
        if self.view:
            self.password.data.configure(text = "********")
            self.view = False
        else:
            self.password.data.configure(text = self.data["password"])
            self.view = True
        app.update()

    def edit(self, app):
        '''Edit'''
        EditPopup(app, self.data, self.num)


class Field(CTkFrame):
    '''Field for displaying information'''
    def __init__(self, master ,app, label : str, icon : CTkImage, data : str, buttons : list = [], command : list = []): #buttons = (icon1,icon2) (CTkImage,CTkImage)
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
        self.field.grid(column = 0, row = 1, sticky = "w")

        self.icon = CTkLabel(self.field, text = "", image = icon, fg_color = "transparent", width = 20, height = 20)
        self.icon.pack(side = "left", padx = (20,10))

        self.data = CTkLabel(self.field, text = data, font = P_BOLD, text_color = DARK_BLUE, fg_color = "transparent")
        self.data.pack(side = "left", padx = 10)

        length = len(buttons)
        for i in range(length):
            pad = 0
            if not i:
                pad = 10
            button = CTkButton(
                self.field,
                text = "",
                image = buttons[i],
                fg_color = "transparent",
                width = 10,
                height = 20,
                command = command[i]
            )
            button.pack(side = "right", padx = (0,pad))

## delete popup
class DelPopup(CTkToplevel):
    '''Delete popup window'''
    def __init__(self,master):
        '''Constructor'''
        super().__init__(master, fg_color = WHITE)

        self.wait_visibility()

        x = master.winfo_x() + master.winfo_width()//2 - self.winfo_width()//2
        y = master.winfo_y() + master.winfo_height()//2 - self.winfo_height()//2
        self.geometry(f"+{x}+{y}")
        self.title("Deleted")
        self.resizable(width =False, height = False)

        self.label = CTkLabel(
            self,
            fg_color = WHITE,
            font = H2,
            text = "Your password have been deleted",
            text_color = DARK_BLUE
        )
        self.label.pack(side = "top", pady = 30, padx = 20)

        self.button = CTkButton(
            self,
            fg_color = BLUE,
            font = H2,
            text = "OK",
            text_color = WHITE,
            command = self.destroy
        )
        self.button.pack(side = "top", pady = (0,30))
        self.attributes("-topmost", True)
        self.lift()

##Edit Poppup
class EditPopup(CTkToplevel):
    '''EditPage Class'''
    def __init__(self, master, data:dict, num:int):
        '''Constructor'''
        super().__init__(master, fg_color = BLUE)

        self.wait_visibility()
        
        self.view = False

        x = master.winfo_x() + master.winfo_width()//2 - self.winfo_width()//2
        y = master.winfo_y() + master.winfo_height()//2 - self.winfo_height()//2
        self.geometry(f"+{x}+{y}")
        self.title("Edit")
        self.resizable(width =False, height = False)
        self.data = data
        self.num = num

        self.label_frame = CTkFrame(self, fg_color= BLUE)
        self.label_frame.pack(side = "top", fill = "x")
        CTkLabel(self.label_frame, text="Edit", font=H1, text_color = WHITE).pack(side = "left", pady=(10, 30), padx = 25)

        self.globe_img = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/Language.png")), size = (20,20))
        self.sites = EditEntry(self, "Site", data["website"], self.globe_img)
        self.sites.pack(side = "top", padx = 25)

        self.person_img = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/Person.png")), size = (20,20))
        self.username = EditEntry(self, "Username", data["username"], self.person_img)
        self.username.pack(side = "top", pady = (30,0), padx = 25)

        self.key_img = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/Key.png")), size = (20,20))
        self.eye = CTkImage(light_image = Image.open(os.path.join(PATH,"Assets/Remove red eye.png")), size = (20,20))
        self.password = EditEntry(self, "Password", "*****", self.key_img)
        self.eye_btn = CTkButton(
            self.password.field,
            text = "",
            image = self.eye,
            fg_color = WHITE,
            width = 20,
            height = 20,
            command = lambda : self.show(master)
        )
        self.eye_btn.pack(side = "left", padx = (0,10))
        self.password.pack(side = "top", pady = (30,0), padx = 25)

        self.buttons = CTkFrame(self, fg_color = BLUE)
        self.buttons.pack(side = "top", pady = (50,35))
        self.cancel = CTkButton(self.buttons, fg_color = WHITE, text = "Cancel", text_color = DARK_BLUE, font = P_BOLD, corner_radius = 30, command = self.destroy)
        self.cancel.pack(side = "left", padx = 5)
        self.confirm_btn = CTkButton(self.buttons, fg_color = WHITE, text = "Confirm", text_color = DARK_BLUE, font = P_BOLD, corner_radius = 30, command = lambda : self.confirm(master))
        self.confirm_btn.pack(side = "right", padx = 5)

        self.attributes("-topmost", True)
        self.lift()

    def confirm(self, app):
        '''Confirm edit'''
        website = self.sites.get()
        if not website:
            website = self.data["website"]
        username = self.username.get()
        if not username:
            username = self.data["username"]
        password = self.password.get()
        if not password:
            password = self.data["password"]
        save.edit(self.num, website, username, password)
        app.page.destroy()
        app.page = SavePage(app)
        app.page.pack(side = "left")
        setting.CURRPAGE = SavePage
        self.destroy()
    
    def show(self, app):
        '''Show password in entry'''
        if self.view:
            self.password.entry.configure(placeholder_text = "*****")
            self.view = False
        else:
            self.password.entry.configure(placeholder_text = self.data["password"])
            self.view = True
        app.update()
        app.focus()

class EditEntry(CTkFrame):
    '''Edit Entry Field'''
    def __init__(self, master, label:str, data:str, icon:CTkImage):
        '''Constructor'''
        super().__init__(master, fg_color = BLUE)

        self.label = CTkLabel(
            self,
            text = label,
            font = P_BOLD,
            text_color = WHITE,
            fg_color = BLUE
        )
        self.label.grid(column = 0, row = 0, sticky = "w")

        self.field = CTkFrame(
            self,
            fg_color = WHITE,
            corner_radius = 30,
            width = 272,
            height = 21,
        )
        self.field.pack_propagate(0)
        self.field.grid(column = 0, row = 1)

        self.img = CTkLabel(
            self.field,
            text = "",
            image = icon,
            width = 20,
            height = 20
        )
        self.img.pack(side = "left", padx = (10,0))

        self.entry = CTkEntry(
            self.field,
            font = P_BOLD,
            placeholder_text = data,
            placeholder_text_color = DARK_BLUE,
            text_color = DARK_BLUE,
            fg_color = WHITE,
            border_color = WHITE,
            width = 185,
            height = 20,
            corner_radius = 30
        )
        self.entry.pack(side = "left",padx = (10,0))
    def get(self):
        '''Get str in entry'''
        return self.entry.get()

def __main():
    '''Driver Code'''

if __name__ == "__main__":
    __main()
