import os
import json
import webbrowser
import tournament
import tkinter as tk
#from tinydb import TinyDB, Query

class Window:
    defaultPath = "./" #Default path variable if something breaks

    # Initialize with attributes
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

        # Creating the Window
        root = tk.Tk()
        root.title(title)
        root.geometry(f"{width}x{height}")
        root.resizable(0 , 0) # Not Resizable

        # Menu Bar stuff
        menubar = tk.Menu(root)
        root.config(menu=menubar)

            # Each menu options
        menuAdd = tk.Menu(menubar, tearoff=0)
        menuAdd.add_command(label="Tournament", command = lambda : self.createTournament(root, "tournament.json"))

        menuOptions = tk.Menu(menubar, tearoff=0)
        menuOptions.add_command(label="GitHub Page", command = lambda : self.callback("https://github.com/ragnar21t/osuTournamentManager/"))
        menuOptions.add_command(label="Help", command = lambda : self.callback("https://github.com/ragnar21t/osuTournamentManager/wiki"))
        menuOptions.add_command(label="Settings")

            # Adding the main menus
        menubar.add_cascade(label="Add", menu=menuAdd)
        menubar.add_cascade(label="Options", menu=menuOptions)

        root.mainloop()

    def checkConfigFile(self):
        # This function exists just to check if config.json exists. 
        # That file right now doesnt do anything but who knows...

        print("Checking if config.json exists...")

        # Checking if the file exists. If not, it creates the .json and adds $defaultPath to "tournamentdbPath"
        if os.path.exists("./config.json"):
            print("Config file exists...")
            with open("./config.json") as configFile:
                fileLoad = json.load(configFile)
                
                tournamentdbPath = fileLoad["tournamentdbPath"]
        else:
            print("Config file doesn't exist. Creating config.json...")
            configFile = open("config.json", "a")

            configFileJson = {
                "tournamentdbPath": self.defaultPath,
            }

            self.addToConfigFile(configFileJson)
            with open("./config.json") as configFile:
                fileLoad = json.load(configFile)

        return tournamentdbPath
    
    def checkTournamentDB(self):
        # We check if the database exists. If it doesn't, we create one

        print("Checking database...")
        if os.path.exists("tournament.json"):
            print("Tournament Database Exists...")
        else:
            print("Database not found, creating one...")
            dbFile = open("tournament.json", "a")
            dbFile.close()

    def addToConfigFile(self, data):

        # Function to write data to the config.json file.

        addToJson = json.dumps(data)
        jsonFile = open("config.json", "w")
        jsonFile.write(addToJson)
        jsonFile.close()

    def createTournament(self, root, dbFile):
        creationWindow = tk.Toplevel(root)
        creationWindow.title("Tournament Data")
        creationWindow.geometry("300x120")
        creationWindow.attributes("-topmost", True)
        creationWindow.after(1, lambda : creationWindow.focus_force())
        creationWindow.resizable(0 , 0) # Not Resizable
        creationWindow.wm_attributes('-toolwindow', 1)
        creationWindow.rowconfigure(3, weight=1)
        creationWindow.columnconfigure(1, weight=1)

        #Labels
        tk.Label(creationWindow, text="Tournament Name: ").grid(pady=2.5, padx=2.5, row=0, column=0)
        tk.Label(creationWindow, text="Acronym (OWC, SFT...): ").grid(pady=2.5 , padx=2.5, row=1, column=0)
        tk.Label(creationWindow, text="Teams Size (1 -> 8):  ").grid(pady=2.5, padx=2, row=2, column=0)

        # Entries
        tournamentName = tk.Entry(creationWindow, width="30")
        tournamentName.grid(row=0, column=1, sticky="e", padx=5)

        tournamentAcronym = tk.Entry(creationWindow, width="30")
        tournamentAcronym.grid(row=1, column=1, sticky="e", padx=5)

        teamSize = tk.Spinbox(creationWindow, from_=1, to=8, width="30")
        teamSize.grid(row=2, column=1, sticky="e", padx=5)

        # Submit button
        sendData = tk.Button(creationWindow, text="Submit", command = lambda : tournament.Tournament(tournamentName, tournamentAcronym, teamSize, "tournament.json"))
        sendData.grid(padx=7.5, row=3, columnspan=2, sticky="e")

    def generateTabs(self):
        pass

    def updateTabs(self):
        pass

    def callback(self, url):
        webbrowser.open_new(url)

Window(600,300,"osu! Tournament Assistant")