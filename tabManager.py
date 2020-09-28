import tkinter
from tkinter import ttk
import os

def tabs(path, tabControl):
    tournamentList = [f for f in os.listdir(path)]
    for tournamentTitle in tournamentList:
        tab = ttk.Frame(tabControl)
        tabControl.add(tab, text=f"{tournamentTitle}")