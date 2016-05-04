import sqlite3
from platform import system
from os.path import exists
from os import environ
import ErrHandle as ErrHandle

class Skypper:

    def __init__(self, skype_path=None):
        self.os_platform = system()
        self.home_dir = environ["HOME"]
        self.default_skype_folders = ["DataRv", "shared_dynco", "shared_httpfe"]

        if skype_path is not None:
            self.skype_path = skype_path
        elif self.os_platform == "Linux":
            self.skype_path = home_dir + "/.Skype/"
        elif self.os_platform == "Windows":
            self.skype_path = environ["APPDATA"] + "\\Skype\\"
        else:
            if exists(self.skype_path): pass

        if not exists(self.skype_path): ErrHandle.no_path()
