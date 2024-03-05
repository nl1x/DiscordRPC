import pypresence
import time
import random

rpc = pypresence.Client("836288137890234449")

folders = ["main", "calcul", "ping", "sinfo", "uinfo"]

rpc.start()
def valorant():
    rpc.set_activity(details="Joue à Valorant", state="Ranked [ Silver 1 | Raze ]", large_image="valorant", small_image="raze", start=time.time(), large_text="Coucou toi")

def python():
    started = time.time()
    while True:
        line = random.randint(0, 420)
        folder = random.choice(folders)
        rpc.set_activity(details="📁| Gaming Bot", state=f"📄| {folder}.py ; line {line}", large_image="python", small_image="vsc", start=started, large_text="Coucou toi")
        print(f"Fichier: {folder}\nLigne: {line}")
        time.sleep(20)

python()
input("Appuyer sur 'Entrer' pour fermer le programme...")