import re


class AirportLocator:
    """
    Model class
    """
    def __init__(self):
        self.lat_min = "0"
        self.lat_max = "0"
        self.lon_min = "0"
        self.lon_max = "0"
        self.src_city = "0"
        self.dst_city = "0"
        self.db = None

    def set_db(self, db):
        """
        Set the database connection
        :param db: DBConnection object
        """
        self.db = db

    def search_airports(self) -> list:
        """
        For seaching airports by coordinates in DB
        :return: list of airports with fields country, city, airport, latitude, longitude
        """
        coordinates = (self.lat_min, self.lat_max, self.lon_min, self.lon_max)
        match = [re.match("^-?\d+$", item) for item in coordinates]
        if None in match:
            self.lat_min, self.lat_max, self.lon_min, self.lon_max = ("0", "0", "0", "0")
        db_connection = self.db.db_connect()
        cursor = db_connection.cursor()
        cursor.execute(f"SELECT country, city, airport, latitude, longitude FROM airports WHERE"
                       f" latitude BETWEEN {self.lat_min} and {self.lat_max} and"
                       f" longitude BETWEEN {self.lon_min} and {self.lon_max}")
        return cursor.fetchall()

    def search_routes(self) -> list:
        """
        For seaching routes by names of cities in DB
        :return: list of routes with fields src_airport, dst_airport, airplane
        """
        if None in (self.src_city, self.dst_city):
            self.src_city, self.dst_city = ("0", "0")
        db_connection = self.db.db_connect()
        cursor = db_connection.cursor()
        cursor.execute(f"SELECT src_airport, dst_airport, airplane FROM routes WHERE "
                       f"src_airport_id IN (SELECT id FROM airports WHERE city = '{self.src_city}') AND "
                       f"dst_airport_id IN (SELECT id FROM airports WHERE city = '{self.dst_city}')")
        return cursor.fetchall()
