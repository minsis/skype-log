import sqlite3
from platform import system
from os.path import exists, isdir, join
from os import environ, listdir
import ErrHandle as ErrHandle

class Skypper:

    def __init__(self, skype_path=None):
        """Initilize variables looking for the OS type and path of Skype"""

        self.os_platform = system()
        self.home_dir = environ["HOME"]

        if skype_path is not None:
            self.skype_path = skype_path
        elif self.os_platform == "Linux":
            self.skype_path = home_dir + "/.Skype/"
        elif self.os_platform == "Windows":
            self.skype_path = environ["APPDATA"] + "\\Skype\\"
        else:
            if exists(self.skype_path): pass

        if not exists(self.skype_path): ErrHandle.no_path()

        self.get_skype_user_path()

    def get_skype_user_path(self):
        """Get the Skype user folder, or give a list if multiple found"""

        default_skype_folders = ["Content", "DataRv", "My Skype Received Files", "RootTools", "shared_dynco", "shared_httpfe"]

        if self.skype_path == None: self.__init__()

        skype_users_dir = ( [ directory for directory in listdir(self.skype_path)
                            if isdir(join(self.skype_path, directory)) and directory not in default_skype_folders ] )

    def get_database_path():
        """Get the path of the SQLite database for Skype"""
        pass
