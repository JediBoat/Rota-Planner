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

        self.grid_rowconfigure(0, weight=1)#row 0 lots of space
        self.grid_columnconfigure(1, weight=1)#col 2 free space col 1 fixed

        #sidebar
        self.sidebar = customtkinter.CTkFrame(self,corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nswe")
        self.sidebar.grid_rowconfigure(4, weight=1)

        #main part of the grid
        self.main = customtkinter.CTkFrame(self, width=1200, height=700, corner_radius=0)
        self.main.grid(row=0, column=1)




if __name__ == "__main__":
    app = App()
    app.mainloop()

