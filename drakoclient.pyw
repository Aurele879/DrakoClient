from tkinter import * 
import webbrowser
import minecraft_launcher_lib
import subprocess
from tkinter import ttk 
import threading
import uuid
import os
import customtkinter
from PIL import ImageTk, Image


#Variable de la fenetre du launcher :
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()  


#Fonction faisant apparaitre la barre de chargement :
def loading():
    progressbar = ttk.Progressbar(orient=HORIZONTAL, length=559, mode='indeterminate')
    progressbar.grid(column=0, row=0, columnspan=2, padx=71, pady=180)
    progressbar.start()


#Installation et lancement du jeu :
def launch_a():
    minecraft_directory = "game_data"
    vanilla_version = "1.16.5"
    launcher_title = "DrakoClient"
    version = minecraft_launcher_lib.forge.find_forge_version(vanilla_version)
    nikname = 'OfflinePlayer'
    options = {
        "username": nikname,
        "uuid": str(uuid.uuid4()),
        "token": "",
        "executablePath": 'javaw'
       }
    
    loading()
    print("installing minecraft's files")
    minecraft_launcher_lib.forge.install_forge_version(version, minecraft_directory)
    full_name_forge_version = version.replace("-", "-forge-")
    app.withdraw()
    command = minecraft_launcher_lib.command.get_minecraft_command(full_name_forge_version,minecraft_directory,options)
    print('game downloaded, launching')
    subprocess.call(command) 
    print("end of task")
    app.quit()


#Fonctions des boutons générés plus tard :
def btn_discord():
    webbrowser.open_new_tab("https://discord.gg/aAjvfRDSZd")

def btn_files():
    subprocess.run(['explorer', os.path.realpath("game_data")])


#Suite de la fenetre du launcher :
app.configure(fg_color = "#191919")
app.geometry("700x300")
app.title('DrakoClient')
app.iconbitmap('assets/icon.ico')

button = customtkinter.CTkButton(master=app, text="Jouer !", command=threading.Thread(target=launch_a).start, fg_color='#FF5100', hover_color="#9E3200")
button.place(relx=0.5, rely=0.8, anchor=CENTER)

button = customtkinter.CTkButton(master=app, text="Dossier du jeu", command=btn_files)
button.place(relx=0.8, rely=0.8, anchor=CENTER)

img = ImageTk.PhotoImage(Image.open("assets/title.png"))
panel = Label(app, image = img, bd= 0, highlightthickness= 0)
panel.place(x = 100, y = 10)

    #combobox = customtkinter.CTkOptionMenu(master=app,
    #                                    values=["DrakoClient 1.16.5", "DrakoClient Skyblock"],
    #                                    command=btn_files,
    #                                    )
    #combobox.place(relx=0.1, rely=0.77)
    #combobox.set("Choisir la version")


#Appartition de la fenetre :
app.resizable(False, False)
app.mainloop()