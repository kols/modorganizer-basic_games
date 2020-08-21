# -*- encoding: utf-8 -*-

from PyQt5.QtCore import QDir, QFileInfo, QStandardPaths

from pathlib import Path

import mobase

from ..basic_game import BasicGame


class TheBindingOfIsaacRebirthGame(BasicGame):
    Name = "The Binding of Isaac: Rebirth - Support Plugin"
    Author = "Luca/EzioTheDeadPoet"
    Version = "0.1.0"

    GameName = "The Binding of Isaac: Rebirth"
    GameShortName = "thebindingofisaacrebirth"
    GameNexusName = "thebindingofisaacrebirth"
    GameNexusId = 1293
    GameSteamId = 250900
    GameBinary = "isaac-ng.exe"
    GameDocumentsDirectory = str(Path(QStandardPaths.writableLocation(QStandardPaths.HomeLocation)).joinpath("Documents", "My Games", "Binding of Isaac Afterbirth+"))
    GameDataPath = str(Path(QStandardPaths.writableLocation(QStandardPaths.HomeLocation)).joinpath("Documents", "My Games", "Binding of Isaac Afterbirth+ Mods"))
    
    
    def iniFiles(self):
        return [
            "options.ini"
        ]