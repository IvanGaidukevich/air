from tkinter import *
from tkinter import ttk
from data_extractor import DataExtractor


class AirportLocatorView(ttk.Notebook):
    def __init__(self, parent):
        super().__init__(parent)
        """
        set the controller
        """
        self.controller = None
        self.data_extractor = DataExtractor()

        """
        Frames
        """
        self.frame1 = ttk.Frame(self)
        self.frame2 = ttk.Frame(self)

        """
        Tabs
        """
        self.add(self.frame1, text="Airport locator")
        self.add(self.frame2, text="Routes locator")
        self.grid()

        """
        Entries
        """
        self.lat_min_entry = ttk.Entry(self.frame1, width=15)
        self.lat_min_entry.insert(0, "0")
        self.lat_max_entry = ttk.Entry(self.frame1, width=15)
        self.lat_max_entry.insert(0, "0")
        self.lon_min_entry = ttk.Entry(self.frame1, width=15)
        self.lon_min_entry.insert(0, "0")
        self.lon_max_entry = ttk.Entry(self.frame1, width=15)
        self.lon_max_entry.insert(0, "0")

        """
        Labels
        """
        self.lat_min_label = ttk.Label(self.frame1, text="Min latitude:")
        self.lat_max_label = ttk.Label(self.frame1, text="Max latitude:")
        self.lon_min_label = ttk.Label(self.frame1, text="Min longitude:")
        self.lon_max_label = ttk.Label(self.frame1, text="Max longitude:")
        self.src_city_label = ttk.Label(self.frame2, text="From city:")
        self.dst_city_label = ttk.Label(self.frame2, text="To city:")

        """
        Table Airport locator
        """
        self.tree = ttk.Treeview(self.frame1, columns=("country", "city", "airport", "latitude", "longitude"),
                                 show="headings", height=25)
        self.tree.heading("city", text="city", anchor=W)
        self.tree.heading("country", text="country", anchor=W)
        self.tree.heading("airport", text="airport", anchor=W)
        self.tree.heading("latitude", text="latitude", anchor=W)
        self.tree.heading("longitude", text="longitude", anchor=W)
        self.tree.column("#1", stretch=NO, width=100)
        self.tree.column("#2", stretch=NO, width=120)
        self.tree.column("#3", stretch=NO, width=300)
        self.tree.column("#4", stretch=NO, width=140)
        self.tree.column("#5", stretch=NO, width=140)

        """
        Table Route locator
        """
        self.tree2 = ttk.Treeview(self.frame2, columns=("source airport", "destination airport", "airplane"),
                                  show="headings", height=25)
        self.tree2.heading("source airport", text="source airport", anchor=W)
        self.tree2.heading("destination airport", text="destination airport", anchor=W)
        self.tree2.heading("airplane", text="airplane", anchor=W)
        self.tree2.column("#1", stretch=NO, width=300)
        self.tree2.column("#2", stretch=NO, width=300)
        self.tree2.column("#3", stretch=NO, width=200)

        """
        Buttons
        """
        self.search_airports_btn = ttk.Button(self.frame1, text="Search airports", width=15,
                                              command=self.clicked_show_airports)
        self.clear_btn = ttk.Button(self.frame1, text="Clear forms", width=15, command=self.clicked_clear_form)
        self.search_routes_btn = ttk.Button(self.frame2, text="Search routes", width=15,
                                            command=self.clicked_show_routes)
        """
        Comboboxes
        """
        self.src_city_cbox = ttk.Combobox(self.frame2, values=self.data_extractor.get_cities(), state="readonly")
        self.dst_city_cbox = ttk.Combobox(self.frame2, values=self.data_extractor.get_cities(), state="readonly")

        """
        Grid template Airport locator
        """
        self.lat_min_label.grid(row=0, column=0)
        self.lat_max_label.grid(row=0, column=2)
        self.lon_min_label.grid(row=1, column=0)
        self.lon_max_label.grid(row=1, column=2)
        self.lat_min_entry.grid(row=0, column=1)
        self.lat_max_entry.grid(row=0, column=3)
        self.lon_min_entry.grid(row=1, column=1)
        self.lon_max_entry.grid(row=1, column=3)
        self.search_airports_btn.grid(row=0, column=4)
        self.clear_btn.grid(row=1, column=4)
        self.tree.grid(row=2, column=0, columnspan=5)

        '''
        Grid Template Routes locator
        '''
        self.src_city_cbox.grid(row=0, column=1, padx=10)
        self.dst_city_cbox.grid(row=0, column=3, padx=10)
        self.src_city_label.grid(row=0, column=0, padx=10)
        self.dst_city_label.grid(row=0, column=2, padx=10)
        self.search_routes_btn.grid(row=0, column=4, padx=10)
        self.tree2.grid(row=1, column=0, columnspan=5, pady=10)

    def set_controller(self, controller):
        """
        For setting the controller
        :param controller:
        """
        self.controller = controller

    def clicked_show_airports(self):
        """
        When the 'Show Airports' button was clicked
        """
        if self.controller:
            self.controller.get_airports(self.lat_min_entry.get(),
                                         self.lat_max_entry.get(),
                                         self.lon_min_entry.get(),
                                         self.lon_max_entry.get())

    def clicked_show_routes(self):
        """
        When the 'Show Routes' button was clicked
        """
        if self.controller:
            self.controller.get_routes(self.src_city_cbox.get(),
                                       self.dst_city_cbox.get())

    def clicked_clear_form(self):
        """
        For clearing form
        """
        self.tree.delete(*self.tree.get_children())
        self.lat_min_entry.delete(0, END)
        self.lat_min_entry.insert(0, "0")
        self.lat_max_entry.delete(0, END)
        self.lat_max_entry.insert(0, "0")
        self.lon_min_entry.delete(0, END)
        self.lon_min_entry.insert(0, "0")
        self.lon_max_entry.delete(0, END)
        self.lon_max_entry.insert(0, "0")

    def show_routes(self, routes):
        """
        For showing the table of routes
        """
        self.tree2.delete(*self.tree2.get_children())
        for route in routes:
            self.tree2.insert("", END, values=route)

    def show_airports(self, airports):
        """
        For showing the table of airports
        """
        self.tree.delete(*self.tree.get_children())
        for airport in airports:
            self.tree.insert("", END, values=airport)
