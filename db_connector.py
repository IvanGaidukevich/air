import sqlite3
import pathlib
from pathlib import Path


class DBConnector:
    """
    Class for connection to SQLITE DB
    """
    def __init__(self):
        self.db_path = Path(pathlib.Path.cwd(), 'airports.db')

    def db_connect(self):
        """
        For connecting to MYSQL DB
        :return: mysql connection object
        """
        try:
            sqlite_connection = sqlite3.connect(self.db_path)
            return sqlite_connection
        except sqlite3.Error as error:
            print("SQLite connection error", error)


