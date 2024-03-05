import pypresence
import time
import tkinter as tk
from widget import Widget

class Window:

    def __init__(self):

        self.background_color = "#36393F"
        self.input_color = "#2F3136"

        self.root = tk.Tk()
        self.widget = Widget(self.root, self.background_color)

        self.x_screen_size = self.root.winfo_screenwidth()
        self.y_screen_size = self.root.winfo_screenheight()

        self.initialize_widgets()
        self.window_config()

    def window_config(self):

        self.root.title("Discord RichPresence")
        self.root.iconbitmap("assets/icon/icon.ico")
        self.root.minsize(int(self.x_screen_size/2), int(self.y_screen_size/2))
        self.root.maxsize(self.x_screen_size, self.y_screen_size)
        self.root.geometry(f"{int(self.x_screen_size/1.5)}x{int(self.y_screen_size/1.5)}")
        self.root.config(background=self.background_color)

    def initialize_widgets(self):
        
        self.create_entry()
        self.create_validate_button()
        self.widget.load_data()

    def create_entry(self):
        
        parameters = [
            "STATE", "DÉBUT",
            "GRANDE IMAGE", "PETITE IMAGE",
            "APPLICATION ID", "DÉTAILS",
            "FIN", "TEXTE GRANDE IMAGE",
            "TEXTE PETITE IMAGE"
            ]

        for parameter in parameters:
            self.widget.create_entry(main_background=self.background_color, second_background=self.input_color, description=parameter)

    def create_validate_button(self):
        self.widget.create_button(second_background="#43B581", text="Appliquer")

    def run(self):
        self.widget.pack_all()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        entries = self.widget.get_entries()
        self.widget.save_data(entries)
        self.root.quit()


start = Window()
start.run()