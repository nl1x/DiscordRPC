from cx_Freeze import setup, Executable

setup(

    name= "Discord RichPresence",
    version= "1.0",
    description= "Afficher un statut personnalisé sur discord. [By Zeynix]",
    executables= [Executable("richpresence.py")] 

)