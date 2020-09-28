import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import json
import os
import tournamentManager
import tabManager

def changeTournamentFolderPath():

    # Window stuff
    tournamentPathWindow = tk.Toplevel(mainWindow)
    tournamentPathWindow.title("Tournaments Folder Path")
    tournamentPathWindow.geometry("350x90")
    tournamentPathWindow.resizable(0 , 0)

    # Tkinter widgets
    curPath = tk.Label(tournamentPathWindow, text="Current Path:")
    curPath.pack()
    curPath2 = tk.Label(tournamentPathWindow, text=f"{tournamentPathFolder}", font=("Helvetica", 8))
    curPath2.pack()
    newPathBtn = tk.Button(tournamentPathWindow, text="Change Path",
        command = lambda: tournamentManager.changingPath(mainWindow, configFile, curPath2 ))
    newPathBtn.pack(pady=10)

# Default tournaments folder path in case of errors
defaultPath = "pathdeprueba"
configFile = "config.json"

# Check if config.json exists
if os.path.exists('./config.json'):
    with open(configFile) as f:
        x = json.load(f)
        tournamentPathFolder = x["tournamentPathFolder"] # Store the path folder
else:
    configFile = open("config.json", "a")

    tournamentPath = {
        "tournamentPathFolder": defaultPath
    }

    addJson = json.dumps(tournamentPath)
    pathJson = open("config.json", "w")
    pathJson.write(addJson)
    pathJson.close()


mainWindow = tk.Tk()
mainWindow.title("osu! Tournament Assistant")
mainWindow.geometry("600x300")
mainWindow.resizable(0 , 0)

# Menu Bar
menubar = tk.Menu(mainWindow)
mainWindow.config(menu=menubar)

# Menu Bar Menus
menuAdd = tk.Menu(menubar, tearoff=0)
menuAdd.add_command(label="Tournament", command = lambda: tournamentManager.createTournament(mainWindow, tabControl))

menuSettings = tk.Menu(menubar, tearoff=0)
menuSettings.add_command(label="Tournament Folder Path", command = changeTournamentFolderPath)

# Menu Bar Sub-Menus
menubar.add_cascade(label="Add", menu=menuAdd)
menubar.add_cascade(label="Settings", menu=menuSettings)

tabControl = ttk.Notebook(mainWindow)
tab = ttk.Frame(tabControl)

# Create tabs with tourney names
tabManager.tabs(tournamentPathFolder, tabControl)

tabControl.pack(expand=1, fill="both")

mainWindow.mainloop()