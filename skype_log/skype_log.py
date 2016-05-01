import sqlite3
from platform import system
from os.path import exists
from os import environ

class Skypper:

    def __init__(self, skype_path=None):
        self.os_platform = system()
        self.home_dir = environ["HOME"]
        self.default_skype_folders = ["DataRv", "shared_dynco", "shared_httpfe"]

        try:
            if skype_path is not None:
                self.skype_path = skype_path

                if exists(self.skype_path): pass
            elif os_platform == "Linux":
                self.skype_path = home_dir + "/.Skype/"

                if exists(self.skype_path): pass
            elif os_platform == "Windows":
                self.skype_path = "%AppData%\Skype\\"

                if exists(self.skype_path): pass
            else:
                if exists(self.skype_path): pass
        except:
            raise ValueError("Unable to determin Skype path, you can override by passing the path of Skype")
