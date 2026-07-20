import tkinter
import os
import os.path
from PIL import Image, ImageTk
import tkinter.messagebox
import customtkinter

#Main menu 
class MenuPage(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

# planning events
class ExcelModePage(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)




#main window
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Rota Planner")
        self.geometry("1600x800")

        script_dir = os.path.dirname(__file__) 
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),script_dir, "images")#Assiagns path to image folder to the variable
        self.eventimg = customtkinter.CTkImage(Image.open(os.path.join(image_path, "addicon_w.png")), size=(130, 130))#Assiagns the size of the Image, path and image to the variable
        self.accountimg = customtkinter.CTkImage(Image.open(os.path.join(image_path, "accounticon_w.png")), size=(120, 120))
        self.excelimg = customtkinter.CTkImage(Image.open(os.path.join(image_path, "excelicon_w.png")), size=(130, 130))

        self.grid_rowconfigure(0, weight=1)#row 0 lots of space
        self.grid_columnconfigure(1, weight=1)#col 2 free space col 1 fixed

        #sidebar
        self.sidebar = customtkinter.CTkFrame(self,corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nswe")
        self.sidebar.grid_rowconfigure(4, weight=1)

        #main part of the grid
        self.main = customtkinter.CTkFrame(self, width=1200, height=700, corner_radius=0,fg_color="transparent")
        self.main.grid(row=0, column=1)

        self.event_btn = customtkinter.CTkButton(self.main, corner_radius=15, 
                                                 font=("Comic sans",30),
                                                 hover_color="#3A8FFF", 
                                                 width=250,
                                                 image=self.eventimg,
                                                 height=150, 
                                                 text="Create event",
                                                 compound="top",
                                                 anchor="s",command=self.event_page)
        self.event_btn.grid(row=2, column=0, padx=20, pady=20)
        

        self.worker_btn = customtkinter.CTkButton(self.main, corner_radius=15,
                                                 font=("Comic sans",30),
                                                 hover_color="#3A8FFF", 
                                                 width=250,
                                                 image=self.accountimg,
                                                 height=150, 
                                                 text="Add employee",
                                                 compound="top",
                                                 anchor="s",command=self.event_page)
        
        self.worker_btn.grid(row=2, column=1, padx=20, pady=20)

        self.planner_btn = customtkinter.CTkButton(self.main, corner_radius=15, 
                                                 font=("Comic sans",30),
                                                 hover_color="#3A8FFF", 
                                                 width=250,
                                                 image=self.excelimg,
                                                 height=150, 
                                                 text="Planner",
                                                 compound="top",
                                                 anchor="s",command=self.event_page)
        self.planner_btn.grid(row=2, column=2, padx=20, pady=20)


    def event_page(self):
        print("cool")





if __name__ == "__main__":
    app = App()
    app.mainloop()

