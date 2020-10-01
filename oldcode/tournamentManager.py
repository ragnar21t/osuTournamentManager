import json
from tkinter import filedialog
import tkinter as tk
from pathlib import Path
import os

def changingPath(mainWindow, configFile, pathLabel):
    newPath = filedialog.askdirectory()
    print(f"The selected path is: {newPath}")

    with open(configFile) as f:
        data = json.load(f)
        data["tournamentPathFolder"] = newPath
        print(f"Changed path to: {newPath}")

        configFile = open("config.json", "a")

        addJson = json.dumps(data)
        pathJson = open("config.json", "w")
        pathJson.write(addJson)
        pathJson.close()

    pathLabel.config(text=f"{newPath}")

def createTournament(root, tabControl):
    print("Creating Tournament...")
    createTournamentWindow = tk.Toplevel(root)
    createTournamentWindow.title("Tournament Creator")
    createTournamentWindow.geometry("250x200")
    createTournamentWindow.resizable(0 , 0)
    
    # Values that will be stored to {tournamentName}.json
    tournamentData = {}

    frame = tk.Frame(createTournamentWindow)

    tk.Label(frame, text="Tournament Name").grid(row=0, pady=10)
    tournamentNameEntry = tk.Entry(frame)
    tournamentNameEntry.grid(row=0, column=1)

    tk.Label(frame, text="Acronym (OWC...)").grid(row=1, pady=10)
    tournamentAcronymEntry = tk.Entry(frame)
    tournamentAcronymEntry.grid(row=1, column=1)

    tk.Label(frame, text="Teams Size").grid(row=2, pady=10)
    teamsSizeEntry = tk.Entry(frame)
    teamsSizeEntry.grid(row=2, column=1)

    frame.pack()
    tk.Button(createTournamentWindow, text="Create", command = lambda: storeTournamentData(tournamentData, tournamentNameEntry, tournamentAcronymEntry, teamsSizeEntry, createTournamentWindow)).pack()

def storeTournamentData(tournamentData, tournamentNameEntry, tournamentAcronymEntry, teamsSizeEntry, topRoot):
    # Capturing data
    tournamentName = tournamentNameEntry.get()
    tournamentAcronym = tournamentAcronymEntry.get()
    teamsSize = teamsSizeEntry.get()

    topRoot.destroy()

    print(f"{tournamentName} {tournamentAcronym} {teamsSize}")

    with open("config.json") as f:
        x = json.load(f)
        tournamentPathFolder = x["tournamentPathFolder"]

    tournamentData["tournamentName"] = tournamentName
    tournamentData["acronym"] = tournamentAcronym
    tournamentData["teams_size"] = teamsSize

    nameWithoutSpaces = tournamentName.replace(" ", "")

    os.mkdir(f"{tournamentPathFolder}/{nameWithoutSpaces}")

    jsonData = json.dumps(tournamentData)

    tournamentJson = open(f"{tournamentPathFolder}/{nameWithoutSpaces}/{nameWithoutSpaces}.json" , "x")
    tournamentJson.write(jsonData)
    tournamentJson.close()