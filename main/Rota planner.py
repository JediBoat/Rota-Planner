import tkinter
import os
import os.path
from PIL import Image, ImageTk
import tkinter.messagebox
import customtkinter
from database import Database 


class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            corner_radius=0,
            fg_color="transparent",
            **kwargs)
        
        script_dir = os.path.dirname(__file__) 
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),script_dir, "images")#Assiagns path to image folder to the variable
        self.eventimg = customtkinter.CTkImage(Image.open(os.path.join(image_path, "addicon_w.png")), size=(130, 130))#Assiagns the size of the Image, path and image to the variable
        self.accountimg = customtkinter.CTkImage(Image.open(os.path.join(image_path, "accounticon_w.png")), size=(120, 120))
        self.excelimg = customtkinter.CTkImage(Image.open(os.path.join(image_path, "excelicon_w.png")), size=(130, 130))
        self.grid_rowconfigure(0, weight=1)#row 0 lots of space
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Create event button
        self.event_btn = customtkinter.CTkButton(
            self,
            corner_radius=15,
            font=("Comic sans", 30),
            hover_color="#3A8FFF",
            width=250,
            image=self.eventimg,
            text_color=("#000000", "#FFFFFF"),
            height=150,
            text="Create event",
            compound="top",
            anchor="s",
            command=lambda: self.master.show_frame(self.master.event_view_frame)
        )
        self.event_btn.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        # Add employee button
        self.worker_btn = customtkinter.CTkButton(
            self,
            corner_radius=15,
            font=("Comic sans", 30),
            hover_color="#3A8FFF",
            text_color=("#000000", "#FFFFFF"),
            width=250,
            image=self.accountimg,
            height=150,
            text="Add employee",
            compound="top",
            anchor="s",
            command=lambda: self.master.show_frame(self.master.employee_page)
        )
        self.worker_btn.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

        # Planner button
        self.planner_btn = customtkinter.CTkButton(
            self,
            corner_radius=15,
            font=("Comic sans", 30),
            hover_color="#3A8FFF",
            text_color=("#000000", "#FFFFFF"),
            width=250,
            image=self.excelimg,
            height=150,
            text="Planner",
            compound="top",
            anchor="s",
            command=lambda: self.master.show_frame(self.master.planner_frame)
        )
        self.planner_btn.grid(row=0, column=2, padx=20, pady=20, sticky="ew")

class AddEventPage(customtkinter.CTkFrame):
    def __init__(self, master, event_boxes):
        super().__init__(master)
        #puts the frame in the middle of the window and makes it responsive to window size
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.event_frame = event_boxes

        self.frame = customtkinter.CTkFrame(self, corner_radius=15, fg_color="transparent", border_width=5, border_color=("#C4C4C4", "#383737"))
        self.frame.grid(row=1, column=1)

        self.inner_frame = customtkinter.CTkFrame(self.frame, fg_color="transparent")
        self.inner_frame.grid(row=0, column=0, padx=30, pady=30)
        #labels and entry boxes for event title and details
        self.title_label = customtkinter.CTkLabel(self.inner_frame, text="Event title", font=("Comic sans", 20, "bold"), text_color=("#000000", "#FFFFFF"), anchor="w", width=500)
        self.title_label.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.title_entry = customtkinter.CTkEntry(self.inner_frame, placeholder_text="Please enter event title", font=("Comic sans", 20), width=400, height=50)
        self.title_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.des_label = customtkinter.CTkLabel(self.inner_frame, text="Event details", font=("Comic sans", 20, "bold"), text_color=("#000000", "#FFFFFF"), anchor="w", width=400)
        self.des_label.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.des_entry = customtkinter.CTkTextbox(self.inner_frame, height=400, width=600, activate_scrollbars=True, font=("Comic sans", 20))
        self.des_entry.grid(row=4, column=1, padx=5, pady=5)

        self.save_button = customtkinter.CTkButton(
            self.inner_frame, 
            text="Save", 
            text_color=("#000000", "#FFFFFF"),
            font=("Comic sans", 20), 
            width=200, 
            height=50
            ,command=self.store_event)  
        
        self.save_button.grid(row=5, column=1, padx=5, pady=5, sticky="nesw")

    def store_event(self):
        event_title = self.title_entry.get()
        event_details = self.des_entry.get("1.0", "end-1c")  # Get the text from the Text widget

        if event_title and event_details:
            self.db = Database()
            self.db.add_event(event_title, event_details)
            self.db.close_connection()
            self.title_entry.delete(0, "end")  # Clear the title entry
            self.des_entry.delete("1.0", "end")  # Clear the details text
            tkinter.messagebox.showinfo("Success", "Event saved successfully!")
            self.event_frame.refresh_event_boxes()  # Refresh the event boxes to show the new event
        else:
            tkinter.messagebox.showwarning("Input Error", "Please fill in both the title and details.")

# planning events
class EmployeePage(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        #puts the frame in the middle of the window and makes it responsive to window size
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.outer_frame = customtkinter.CTkFrame(self, corner_radius=15, fg_color=("#C4C4C4", "#383737"))
        self.outer_frame.grid(row=1, column=1, sticky="nsew")
        self.outer_frame.grid_rowconfigure(0, weight=1)
        self.outer_frame.grid_rowconfigure(1, weight=0)
        self.outer_frame.grid_columnconfigure(0, weight=1)

        self.db = Database()
        Employees = self.db.search_employees()
        self.db.close_connection()

        self.refreshEmployees(Employees)

    #function to update the list of employees when a new employee is added
    def refreshEmployees(self, Employees):
            try:
                self.name_list.destroy()#stops it crashing when adding a new employee by destroying the old list and creating a new one
                self.button_bar.destroy()#stops it crashing when adding a new employee by destroying the old list and creating a new one
            except AttributeError:
                pass
            self.name_list = scrollableNames(self.outer_frame, title="Employees", values=Employees)#refreshes the list of employees when a new employee is added
            self.name_list.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

            self.button_bar = Employeebuttonbar(self.outer_frame, sframe=self.name_list, employee_page=self)
            self.button_bar.grid(row=1, column=0, padx=10, pady=10, sticky="nesw")
     

        
class Employeebuttonbar(customtkinter.CTkFrame):
    def __init__(self, master, sframe, employee_page):
        super().__init__(master)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.sframe = sframe
        self.employee_page = employee_page
        
        #buttons to add and remove employees
        self.add_button = customtkinter.CTkButton(
            self,
            text="Add Employee",
            height=50,
            text_color=("#000000", "#FFFFFF"),
            command = self.adding_employee,
            font=("Comic sans", 20)
        )
        self.add_button.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")

        self.remove_button = customtkinter.CTkButton(
            self,
            text="Remove Employee",
            text_color=("#000000", "#FFFFFF"),
            height=50,
            command = self.remove_employee,
            font=("Comic sans", 20)
        )
        self.remove_button.grid(row=0, column=1, padx=10, pady=10,sticky="nesw")

    def adding_employee(self):
                new_employee = customtkinter.CTkInputDialog(text="Enter employee name and the enter department seprated with a ' : '" + "\n"+ 
                                                            "So for example John:Christies or John:Events", title="Add Employee", font=("Comic sans", 20))
                new_employee_text = new_employee.get_input().split(":")
                print (new_employee_text)
                if self.isNullOrWhiteSpace(new_employee_text[0]) or self.isNullOrWhiteSpace(new_employee_text[1]) or self.correct_department(new_employee_text[1]):
                    tkinter.messagebox.showwarning("Input Error", "Please fill in the employee name.")
                else:
                    self.db = Database()
                    self.db.add_employee(new_employee_text[0], new_employee_text[1].replace(" ", ""))
                    self.employee_page.refreshEmployees(self.db.search_employees())
                    self.db.close_connection()
                    tkinter.messagebox.showinfo("Success", "Employee added successfully!")

    def remove_employee(self):
                self.db = Database()
                self.db.remove_employee(self.sframe.get())
                self.employee_page.refreshEmployees(self.db.search_employees())
                if not self.sframe.get(): 
                    tkinter.messagebox.showinfo("Failure","Please selected an employee")
                else:
                    tkinter.messagebox.showinfo("Success", "Employee removed successfully!")
                self.db.close_connection()


    def isNullOrWhiteSpace(self, str=None):
        return not str or str.isspace()
    
    def correct_department(self, text):
        text = text.replace(" ", "")
        text = text.lower()

        if text == "christies" or text == "events":
            return False
        else:
            return True


class Eventboxes(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.db = Database()
        result = self.db.get_events()
        self.db.close_connection

        self.event_boxes = EventList(self, event=result)
        self.event_boxes.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.add_btn = customtkinter.CTkButton(
            self,
            text="Add Event", 
            text_color=("#000000", "#FFFFFF"),
            font=("Comic sans", 20), 
            command=lambda: self.master.show_frame(self.master.add_event_page)
        )
        self.add_btn.grid(row=1, column=0, padx=10, pady=10, sticky="nesw")

    def refresh_event_boxes(self):
        self.db = Database()
        result = self.db.get_events()
        self.db.close_connection()
        self.event_boxes.destroy()  # Destroy the current EventList
        self.event_boxes = EventList(self, event=result)  # Create a new EventList with updated data
        self.event_boxes.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Place the new EventList in the grid


class Eventbox(customtkinter.CTkFrame): 
    def __init__(self, master, title, text): ####### Need to add functionality
        super().__init__(master)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.outer_frame = customtkinter.CTkFrame(self, corner_radius=15, fg_color="transparent", border_width=5, border_color=("#C4C4C4", "#383737"))
        self.outer_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.outer_frame.grid_rowconfigure(0, weight=1)
        self.outer_frame.grid_columnconfigure(0, weight=1)

        self.inner_frame = customtkinter.CTkFrame(self.outer_frame, fg_color=("#C4C4C4", "#383737"), corner_radius=15)
        self.inner_frame.grid(row=0, column=0, padx=15, pady=30, sticky="nsew")
        self.inner_frame.grid_columnconfigure(1, weight=1)
        self.inner_frame.grid_rowconfigure(2, weight=1)

        self.event_label = customtkinter.CTkLabel(self.inner_frame, text=title, font=("Comic sans", 20, "bold"), text_color=("#000000", "#FFFFFF"), anchor="w", width=500)
        self.event_label.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.event_details = customtkinter.CTkTextbox(self.inner_frame, activate_scrollbars=True, font=("Comic sans", 20), fg_color= "transparent")
        self.event_details.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        self.event_details.insert("0.0", text)

        self.go_button = customtkinter.CTkButton( ####### Need to add functionality
            self.inner_frame,
            text="Edit Event",
            text_color=("#000000", "#FFFFFF"),
            font=("Comic sans", 20)
        )
        self.go_button.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

        self.delete_button = customtkinter.CTkButton( ####### Need to add functionality
            self.inner_frame,
            text="Delete Event",
            text_color=("#000000", "#FFFFFF"),
            font=("Comic sans", 20),
            command= lambda: self.on_delete(title)
        )
        self.delete_button.grid(row=3, column=3, padx=10, pady=10, sticky="nswe", columnspan=2)

    def on_delete(self, title):
        confirm = tkinter.messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this event?")
        if confirm:
            self.destroy()  # Destroy the current EventList
            self.db = Database()
            self.db.remove_event(title)
            self.master.event_boxes.destroy()  # Destroy the current EventList
            self.master.event_boxes = EventList(self.master, event=self.db.get_events())
            self.db.close_connection()
            self.master.event_boxes.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
                
            tkinter.messagebox.showinfo("Success", "Event deleted successfully!")


class EventList(customtkinter.CTkScrollableFrame):
    def __init__(self, master, event):
        super().__init__(master, label_text="Events", label_font=("Comic sans", 20, 'bold'))

        #scrollable frame for events
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.event = event
        self.events = [] ####### Need to add functionality
        columns = 2

        for i, value in enumerate(self.event):
            row = i // columns
            column = (i % columns) + 1 #2 columns for events

            name = value[0]
            details = value[1]

            eventboxes = Eventbox(self, title=name, text=details)
            eventboxes.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")
            self.events.append(eventboxes) ####### Need to add functionality


    
class PlannerFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, sticky="nsew")
        custom_font = customtkinter.CTkFont("Comic sans", 20, 'bold')
        self.tab_view._segmented_button.configure(font=custom_font)


class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__( master, **kwargs)


        # create tabs
        self.add("Mon")
        self.add("Tues")
        self.add("Wed")
        self.add("Thurs")
        self.add("Fri")
        self.add("Sat")
        self.add("Sun")
        

        self._segmented_button.configure(command=self.tab_changed)
        self.refresh_tab_data("Mon")


    def tab_changed(self, selected_tab):
        self.refresh_tab_data(selected_tab)


    def refresh_tab_data(self, tab_name):
        tab = self.tab(tab_name)

        # Destroy the old frame if it exists
        old_frame = getattr( self, f"{tab_name.lower()}_tab", None)

        if old_frame is not None:
            old_frame.destroy()

        tab.grid_rowconfigure(0, weight=1)
        tab.grid_columnconfigure(0, weight=1)

        new_frame = TabbedFrame(tab)
        new_frame.grid( row=0, column=0, sticky="nsew")

        # Store reference
        setattr(self, f"{tab_name.lower()}_tab", new_frame )



#class for output and saving changing to excel file
class BtnOuput(customtkinter.CTkFrame):
    def __init__(self, master, sframe1, sframe2):
        super().__init__(master)


        self.scrollframe_1 = sframe1
        self.scrollframe_2 = sframe2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=0)

        self.button = customtkinter.CTkButton(
            self, 
            text="Confirm", 
            height=200,
            font=("Comic sans", 20), 
            text_color=("#000000", "#FFFFFF"),
            command=lambda: self.output.insert("end", str(self.scrollframe_1.get()) +"\n"+ str(self.scrollframe_2.get())+"\n\n"))
        
        self.button.grid(row=0, column=2, padx=10, pady=10, sticky="w")
        self.output = customtkinter.CTkTextbox(self, activate_scrollbars=True, font=("Comic sans", 20))
        self.output.grid(row=0, column=0,padx=10, pady=10, columnspan=2, sticky="nsew")


class TabbedFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.db = Database()
        values = self.db.search_employees()
        events = self.db.get_event_names()
        self.db.close_connection()
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        self.scrollable_checkbox_frame_1 = scrollableNames(self, title="Employees", values=values)
        self.scrollable_checkbox_frame_1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.scrollable_checkbox_frame_2 = scrollableNames(self, title="Events", values=events)
        self.scrollable_checkbox_frame_2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.scrollable_checkbox_frame_3 = scrollableNames(self, title="Events", values=events)
        self.scrollable_checkbox_frame_3.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        self.buttonbar = BtnOuput(self, sframe1=self.scrollable_checkbox_frame_1, sframe2=self.scrollable_checkbox_frame_3)
        self.buttonbar.grid(row=1, column=0,padx=10, pady=10,columnspan=3, sticky="ew")
        

         
class scrollableNames(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(
            master, label_text=title, label_font=("Comic sans", 20, 'bold'))
        
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
        self.db = Database()
        self.db.create_tables()
        self.db.close_connection()

        self.grid_rowconfigure(0, weight=1)#row 0 lots of space
        self.grid_columnconfigure(1, weight=1)#col 2 free space col 1 fixed

        
        self.planner_frame = PlannerFrame(self)
        self.event_view_frame = Eventboxes(self)
        self.add_event_page = AddEventPage(self, self.event_view_frame)
        self.employee_page = EmployeePage(self)
        self.main_frame = MainFrame(self)




        self.main_frame.grid(row=0, column=1, sticky="nsew")
        self.planner_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=15)
        self.add_event_page.grid(row=0,column=1, sticky="nsew", padx=20, pady=15)
        self.employee_page.grid(row=0, column=1, sticky="nsew", padx=20, pady=15)
        self.event_view_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=15)

        self.show_frame(self.main_frame)


        #sidebar
        self.sidebar = customtkinter.CTkFrame(self,corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nswe")
        self.sidebar.grid_rowconfigure(4, weight=1)

        #Nav buttons
        self.home_button = customtkinter.CTkButton(
            self.sidebar, 
            font=("Comic sans",20), 
            height=50, text="Home",
            text_color=("#000000", "#FFFFFF"),
            command=lambda: self.show_frame(self.main_frame))#Creates a button named Home for menu option
        
        self.home_button.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar, font=("Comic sans",17), text="Appearance Mode:", anchor="w")#Creates a laberl named Appearance for menu option
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))#Posistions it on the grid,therefore when the app expand or minmize it will srink or grow to accordance
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.sidebar, font=("Comic sans",20), text_color=("#000000", "#FFFFFF"), height=50, values=["System","Light", "Dark"],command=self.change_appearance_mode_event)#Creates a menu optition for system apperance within navigation frame
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=(10, 10), sticky="s")#places menu in an specfic area within the grid, therefore when the app expand or minmize it will srink or grow to accordance

    def show_frame(self, frame):
        frame.tkraise()
        #function to be run when certain buttons are clicked
    
    def change_appearance_mode_event(self, new_appearance_mode):#Creates a function that takes inputds of the user request  appearance  of application
        customtkinter.set_appearance_mode(new_appearance_mode)#Changes appearance on apps use input from the menu opition 




if __name__ == "__main__":
    app = App()
    app.mainloop()

