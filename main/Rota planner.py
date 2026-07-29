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

class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            width=1200,
            height=700,
            corner_radius=0,
            fg_color="transparent",
            **kwargs)
        
        script_dir = os.path.dirname(__file__) 
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),script_dir, "images")#Assiagns path to image folder to the variable
        self.eventimg = customtkinter.CTkImage(Image.open(os.path.join(image_path, "addicon_w.png")), size=(130, 130))#Assiagns the size of the Image, path and image to the variable
        self.accountimg = customtkinter.CTkImage(Image.open(os.path.join(image_path, "accounticon_w.png")), size=(120, 120))
        self.excelimg = customtkinter.CTkImage(Image.open(os.path.join(image_path, "excelicon_w.png")), size=(130, 130))


        # Create event button
        self.event_btn = customtkinter.CTkButton(
            self,
            corner_radius=15,
            font=("Comic sans", 30),
            hover_color="#3A8FFF",
            width=250,
            image=self.eventimg,
            height=150,
            text="Create event",
            compound="top",
            anchor="s",
            command=self.event_page
        )

        self.event_btn.grid(row=2, column=0, padx=20, pady=20)

        # Add employee button
        self.worker_btn = customtkinter.CTkButton(
            self,
            corner_radius=15,
            font=("Comic sans", 30),
            hover_color="#3A8FFF",
            width=250,
            image=self.accountimg,
            height=150,
            text="Add employee",
            compound="top",
            anchor="s",
            command=self.employee_page
        )

        self.worker_btn.grid(row=2, column=1, padx=20, pady=20)

        # Planner button
        self.planner_btn = customtkinter.CTkButton(
            self,
            corner_radius=15,
            font=("Comic sans", 30),
            hover_color="#3A8FFF",
            width=250,
            image=self.excelimg,
            height=150,
            text="Planner",
            compound="top",
            anchor="s",
            command=self.planner_page
        )

        self.planner_btn.grid(row=2, column=2, padx=20, pady=20)


    def event_page(self):
        self.master.show_frame(self.master.event_frame)
 
    def employee_page(self):
        self.master.show_frame(self.master.menu_page)

    def planner_page(self):
        self.master.show_frame(self.master.excel_page)
        


class EventFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            **kwargs)
        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)
        custom_font = customtkinter.CTkFont("Comic sans", 20, 'bold')
        self.tab_view._segmented_button.configure(font=custom_font)


class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            width=1250,
            height=900,
            **kwargs)



        # create tabs
        self.add("Mon")
        self.add("Tues")
        self.add("Wed")
        self.add("Thurs")
        self.add("Fri")
        self.add("Sat")
        self.add("Sun")


        values = ["value 1", "value 2", "value 3", "value 4", "value 5", "value 6"]
        self.scrollable_checkbox_frame = scrollableNames(master=self.tab("Mon"), title="Employees", values=values)
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.button = customtkinter.CTkButton(master=self.tab("Mon"), text="Confirm", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def button_callback(self):
        print("checkbox_frame:", self.scrollable_checkbox_frame.get())
         
class scrollableNames(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(
            master, label_text=title,
            width=600, height=800)
        
        self.grid_columnconfigure(0, weight=1)
        custom_font = customtkinter.CTkFont("Comic sans", 20, 'bold')
        self.values = values
        self.checkboxes = []

        #create checkbox and append the checkbox to a list for each vaule in a list
        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value, font=custom_font)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    #returns the vaules of the checkboxes
    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes




#main window
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Rota Planner")
        self.geometry("1600x800")

        self.grid_rowconfigure(0, weight=1)#row 0 lots of space
        self.grid_columnconfigure(1, weight=1)#col 2 free space col 1 fixed

        
        self.event_frame = EventFrame(self)
        self.menu_page = MenuPage(self)
        self.excel_page = ExcelModePage(self)
        self.main_frame = MainFrame(self)



        self.main_frame.grid(row=0, column=1)

        self.event_frame.grid(row=0, column=1)

        self.menu_page.grid(row=0,column=1)

        self.excel_page.grid(row=0, column=1, sticky="nsew")

        self.show_frame(self.main_frame)


        #sidebar
        self.sidebar = customtkinter.CTkFrame(self,corner_radius=0, fg_color="#242424")
        self.sidebar.grid(row=0, column=0, sticky="nswe")
        self.sidebar.grid_rowconfigure(4, weight=1)


        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar, font=("Comic sans",17), text="Appearance Mode:", anchor="w")#Creates a laberl named Appearance for menu option
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))#Posistions it on the grid,therefore when the app expand or minmize it will srink or grow to accordance
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.sidebar, font=("Comic sans",20), height=50, values=["System","Light", "Dark"],command=self.change_appearance_mode_event)#Creates a menu optition for system apperance within navigation frame
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=(10, 10), sticky="s")#places menu in an specfic area within the grid, therefore when the app expand or minmize it will srink or grow to accordance

    def show_frame(self, frame):
        frame.tkraise()
        #function to be run when certain buttons are clicked
    def change_appearance_mode_event(self, new_appearance_mode):#Creates a function that takes inputds of the user request  appearance  of application
        customtkinter.set_appearance_mode(new_appearance_mode)#Changes appearance on apps use input from the menu opition 




if __name__ == "__main__":
    app = App()
    app.mainloop()

