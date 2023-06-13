class ControllerAirports:
    """
    Controller class
    """
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_airports(self, lat_min: str, lat_max: str, lon_min: str, lon_max: str):
        """
        For getting airports from model and show them in view
        :param lat_min: min latitude in degrees
        :param lat_max: max latitude in degrees
        :param lon_min: min longitude in degrees
        :param lon_max: max longitude in degrees
        :return:
        """
        self.model.lat_min = lat_min
        self.model.lat_max = lat_max
        self.model.lon_min = lon_min
        self.model.lon_max = lon_max
        airports = self.model.search_airports()
        self.view.show_airports(airports)

    def get_routes(self, src_city: str, dst_city: str):
        """
        for getting routes from model and show them in view
        :param src_city: source city (from)
        :param dst_city: destination city (to)
        :return:
        """
        self.model.src_city = src_city
        self.model.dst_city = dst_city
        routes = self.model.search_routes()
        self.view.show_routes(routes)
