import sqlite3
from platform import system
from os.path import exists, isdir, join
from os import environ, listdir
from .ErrHandle import *

class Skypper:

    default_skype_folders = ["Content", "DataRv", "My Skype Received Files", "RootTools", "shared_dynco", "shared_httpfe"]

    def __init__(self, skype_path=None, skype_user=dict()):
        """Initilize variables"""

        self.os_platform = system()
        self.home_dir = environ["HOME"]
        self.skype_user_dict = skype_user
        self.skype_path = skype_path

    def get_skype_path(self, skype_path=None):
        """Return Skype path for speicifc OS"""

        if skype_path is not None:
            self.skype_path = skype_path
        elif self.skype_path is not None:
            pass
        elif self.os_platform == "Linux":
            self.skype_path = self.home_dir + "/.Skype/"
        elif self.os_platform == "Windows":
            self.skype_path = environ["APPDATA"] + "\\Skype\\"

        if not exists(self.skype_path): no_path()

        return(self.skype_path)

    def get_skype_user(self):
        """Return dictionary of Skype user and path names(s)"""

        if self.skype_path == None: self.get_skype_path()

        if
        self.skype_user_list = ( [ directory for directory in listdir(self.skype_path)
                            if isdir(join(self.skype_path, directory)) and directory not in default_skype_folders ] )

        for user in self.skype_user_list:
            self.skype_user_dict[user] = { "username" : user, "path" : join(self.skype_path, user) }

        return(self.skype_user_dict)

    def get_skype_database_path(self):
        """Return skype_user_dict with SQLite database path added"""

        if self.skype_user == None: self.get_skype_user_path()

        for user_path in self.skype_user_path:

        if not exists(self.skype_database_path): no_database()
