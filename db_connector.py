import mysql
from mysql.connector import DatabaseError

CONFIG = {"host": "localhost",
          "user": "root",
          "passwd": "gaydu777",
          "database": "flights"}


class DBConnector:
    """
    Class for connection to MYSQL DB
    """
    def __init__(self, host: str, user: str, passwd: str, database: str):
        """
        :param host: host name
        :param user: username
        :param passwd: password
        :param database: database name
        """
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database

    def db_connect(self):
        """
        For connecting to MYSQL DB
        :return: mysql connection object
        """
        try:
            return mysql.connector.connect(host=self.host, user=self.user, passwd=self.passwd, database=self.database)
        except DatabaseError:
            pass
