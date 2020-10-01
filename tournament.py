import os
import json
import tkinter as tk
from tinydb import TinyDB, Query

class Tournament(object):
    def __init__(self, name, acronym, teamSize, dbFile):
        self.name = name
        self.acronym = acronym
        self.teamSize = int(teamSize)

        self.insertData(dbFile)

    def insertData(self, dbFile):
        db = TinyDB(dbFile)
        
        db.insert({
            "name": self.name,
            "acronym": self.acronym,
            "teamSize": self.teamSize
        })