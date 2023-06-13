import tkinter as tk
from controller import ControllerAirports
from model import AirportLocator
from view import AirportLocatorView
from db_connector import DBConnector, CONFIG


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Py Airport Helper')

        """
        set database connection        
        """
        db = DBConnector(CONFIG['host'],
                         CONFIG['user'],
                         CONFIG['passwd'],
                         CONFIG['database'])
        """
        set the model
        """
        model = AirportLocator()
        model.set_db(db)

        """
        set the view
        """
        view = AirportLocatorView(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        """
        set the controller
        """
        controller = ControllerAirports(model, view)

        """
        connect the controller to the view
        """
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
