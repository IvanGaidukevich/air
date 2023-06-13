from db_connector import DBConnector, CONFIG


class DataExtractor:
    def __init__(self):
        self.db = DBConnector(CONFIG['host'],
                              CONFIG['user'],
                              CONFIG['passwd'],
                              CONFIG['database'])

    def get_cities(self):
        db_connection = self.db.db_connect()
        cursor = db_connection.cursor()
        cursor.execute(f"SELECT DISTINCT city FROM airports ORDER BY city ASC")
        return [city for cities in cursor.fetchall() for city in cities]
