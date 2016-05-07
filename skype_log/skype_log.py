import sqlite3
from platform import system
from os.path import exists, isdir, join
from os import environ, listdir
from .ErrHandle import *

class Skypper:

    def __init__(self, skype_path=None):
        """Initilize variables looking for the OS type and path of Skype"""

        self.os_platform = system()
        self.home_dir = environ["HOME"]
        self.skype_user_path = None

        if skype_path is not None:
            self.skype_path = skype_path
        elif self.os_platform == "Linux":
            self.skype_path = self.home_dir + "/.Skype/"
        elif self.os_platform == "Windows":
            self.skype_path = environ["APPDATA"] + "\\Skype\\"

        if not exists(self.skype_path): no_path()

    def get_skype_user_path(self):
        """Get list of Skype user folder(s)"""

        default_skype_folders = ["Content", "DataRv", "My Skype Received Files", "RootTools", "shared_dynco", "shared_httpfe"]

        if self.skype_path == None: self.__init__()

        self.skype_user_path = ( [ directory for directory in listdir(self.skype_path)
                            if isdir(join(self.skype_path, directory)) and directory not in default_skype_folders ] )

        return(self.skype_user_path)

    def get_database_path(self):
        """Get the path of the SQLite database for Skype"""

        if self.skype_user_path == None: self.get_skype_user_path()
