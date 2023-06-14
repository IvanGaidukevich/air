from db_connector import DBConnector


class DataExtractor:
    """
    Class for extracting data from DB
    """
    def __init__(self):
        self.db = DBConnector()

    def get_cities(self) -> list:
        """
        For getting list of all cities, which have airports
        :return: list
        """
        db_connection = self.db.db_connect()
        cursor = db_connection.cursor()
        cursor.execute(f"SELECT DISTINCT city FROM airports ORDER BY city ASC")
        return [city for cities in cursor.fetchall() for city in cities]
