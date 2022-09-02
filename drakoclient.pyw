from tkinter import * 
import webbrowser
import minecraft_launcher_lib
import subprocess
from tkinter import ttk 
import threading
import uuid
import os

#Variable de la fenetre du launcher :
window = Tk()


#Fonction faisant apparaitre la barre de chargement :
def loading():
    pb = ttk.Progressbar(
        window,
        orient='horizontal',
        mode='indeterminate',
        length=380
    )
    pb.grid(column=0, row=0, columnspan=2, padx=10, pady=200)
    pb.start()


#Installation et lancement du jeu :
def launch_a():
    minecraft_directory = "game_data"
    vanilla_version = "1.16.5"
    launcher_title = "DrakoClient"
    version = minecraft_launcher_lib.forge.find_forge_version(vanilla_version)
    nikname = 'OfflinePlayer'
    options = {"username": nikname, "uuid": str(uuid.uuid4()), "token": ""}
    loading()
    print("installing minecraft's files")
    minecraft_launcher_lib.forge.install_forge_version(version, minecraft_directory)
    full_name_forge_version = version.replace("-", "-forge-")
    window.withdraw()
    command = minecraft_launcher_lib.command.get_minecraft_command(full_name_forge_version,minecraft_directory,options)
    print('game downloaded, launching')
    subprocess.call(command)
    print("end of task")
    window.quit()


#Fonctions des boutons générés plus tard :
def btn_discord():
    webbrowser.open_new_tab("https://discord.gg/aAjvfRDSZd")

def btn_files():
    subprocess.run(['explorer', os.path.realpath("game_data")])


#Suite de la fenetre du launcher :
window.iconbitmap('assets/launcher_icon.ico')
window.title("Drako Client")
window.geometry("744x300")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 300,
    width = 744,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"assets/background.png")
background = canvas.create_image(
    400.0, 250.0,
    image=background_img)

img0 = PhotoImage(file = f"assets/button_discord.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_discord,
    relief = "flat")

b0.place(
    x = 569, y = 230,
    width = 145,
    height = 40)

img1 = PhotoImage(file = f"assets/button_play.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = threading.Thread(target=launch_a).start,
    relief = "flat")

b1.place(
    x = 562, y = 157,
    width = 160,
    height = 50)

img2 = PhotoImage(file = f"assets/button_files.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_files,
    relief = "flat")

b2.place(
    x = 630, y = -4,
    width = 100,
    height = 100)


#Appartition de la fenetre :
window.resizable(False, False)
window.mainloop()