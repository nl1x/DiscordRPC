"""

On créer une fonction qui :
    - Créer le widget : def create_entry()
    - Stock le widget dans la variable self.widget_type (List)
    - Pour la frame :
        - On créer une frame qui va contenir :
            - Le widget
            - Une "description" (Qui dira par exemple : "Détails: {widget}")
        - On stock la frame dans la variable self.frames (List)

FRAME:
    - On créer une frame principale expand=True
        - On créer une frame de gauche side=LEFT
        - On créer une frame de droite side=RIGHT

    si x < 6:
        left_frame
    sinon:
        right_frame

"""
from tkinter import *
import pypresence
import time
import pickle

class Widget:

    def __init__(self, root, color):

        self.main_frame = Frame(root, bg=color)
        self.main_frame.pack(expand=True)

        self.side_frame = Frame(self.main_frame, bg=color)
        self.side_frame.pack(expand=True)

        self.right_frame = Frame(self.side_frame, bg=color)
        self.right_frame.pack(side=RIGHT, padx=20)
        
        self.left_frame = Frame(self.side_frame, bg=color)
        self.left_frame.pack(side=LEFT, padx=20)

        self.bottom_frame = Frame(self.main_frame, bg=color)
        self.bottom_frame.pack(side=BOTTOM, pady=20)
    
        self.frames = []
        self.entries = {}
        self.descriptions = []
        self.buttons = []
        
        self.font = "Bahnschrift"

    def create_entry(self, main_background=None, second_background=None, description=None):
        
        if len(self.frames) > 4:
            new_frame = Frame(self.right_frame, bg=main_background)
        else:
            new_frame = Frame(self.left_frame, bg=main_background)

        self.entries[description] = Entry(
            new_frame,
            background = second_background,
            foreground = "white",
            font=(self.font, 15),
            relief=FLAT,
            highlightcolor = "#4D809C",
            highlightthickness=1
        )
        new_desc = Label(
            new_frame,
            background = main_background,
            foreground = "#B9BBBE",
            text = description,
            font=(self.font, 10, "bold"),
            anchor="w"
        )

        self.frames.append(new_frame)
        self.descriptions.append(new_desc)

    def create_button(self, main_background=None, second_background=None, text=None):

        new_button = Button(
            self.right_frame,
            background = second_background,
            foreground = "white",
            activebackground = "#37996C",
            relief = FLAT, overrelief = FLAT,
            highlightthickness = 0, bd = 0,
            text = text,
            font=(self.font, 20, "bold"),
            width=15,
            command=self.apply_changes
        )

        self.buttons.append(new_button)

    def get_entries(self):
        self.current_entries = {}
        for entry in self.entries:
            self.current_entries[entry] = self.entries[entry].get()
            if entry == "DÉBUT" or entry == "FIN":
                if self.current_entries[entry] == "now" or self.current_entries[entry] == "maintenant":
                    self.current_entries[entry] = time.time()
                else:
                    try:
                        self.current_entries[entry] = int(self.current_entries[entry])
                    except:
                        self.current_entries[entry] = None
            if self.current_entries[entry] == "":
                self.current_entries[entry] = None
        return self.current_entries

    def connect_to_discord(self, application_id):
        try:
            self.rpc.close()
        except:
            pass
        self.rpc = pypresence.Client(application_id)
        self.rpc.start()

    def load_data(self):

        try:
            with open("assets/data/data.do_not_delete", "rb") as fic:
                record = pickle.Unpickler(fic)
                data = record.load()
                self.apply_changes(entries=data)
                for x in data:
                    if data[x] != None:
                        self.entries[x].insert(0, str(data[x]))
                fic.close()
        except Exception as error:
            print("[ERROR] Une erreur s'est produite lors du chargement des données :")
            print(error)

    def save_data(self, data):
        try:
            with open("assets/data/data.do_not_delete", "wb") as fic: # On créé / ouvre le fichier data.data en tant que fic en mode 'wb' pour pouvoir écrire dedans
                record = pickle.Pickler(fic) # Pour dire le fichier dans lequel on veut enregistrer la donnée
                record.dump(data) # On copie le contenu de data et on le colle dans le fichier fic
                fic.close()
        except Exception as error:
            print("[ERROR] Une erreur s'est produite lors de la sauvegarde des données")
            print(error)

    def apply_changes(self, entries=None):
        self.buttons[0].config(state="disabled")

        if entries == None:
            entries = self.get_entries()

        application_id = entries["APPLICATION ID"]
        
        state = entries["STATE"]
        details = entries["DÉTAILS"]
        start = entries["DÉBUT"]
        end = entries["FIN"]

        large_image = entries["GRANDE IMAGE"]
        large_image_text = entries["TEXTE GRANDE IMAGE"]

        small_image = entries["PETITE IMAGE"]
        small_image_text = entries["TEXTE PETITE IMAGE"]

        self.connect_to_discord(application_id=application_id)

        self.rpc.set_activity(
            state=state, details=details,
            start=start, end=end,
            large_image=large_image, large_text=large_image_text,
            small_image=small_image, small_text=small_image_text)
        
        self.buttons[0].config(state="normal")

    def pack_all(self):

        for frame in self.frames:
            frame.pack(expand=True, pady=5)
        
        for entry in self.entries:
            self.entries[entry].pack(side=BOTTOM, padx=4)
        
        for text in self.descriptions:
            text.pack(side=TOP, anchor="w")

        for button in self.buttons:
            button.pack(expand=True, pady=5)