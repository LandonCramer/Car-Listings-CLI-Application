from classes.__init__ import CURSOR, CONN
from classes.Appointment import Appointment

class Sale(Appointment):
    all = {}

    def __init__(self, type_, date, customer_id, employee_id, car_id, balance, status, id_=None):
        super().__init__(type_, date, customer_id, employee_id, car_id, id_)
        self.balance = balance
        self.status = status

    # *************
    # CREATE TABLE
    # *************

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY,
            type TEXT,
            date TEXT,
            customer_id INTEGER,
            employee_id INTEGER,
            car_id INTEGER,
            balance INTEGER,
            status INTEGER)
        """
        super().create_table(sql)
 
    # ***********
    # PROPERTIES
    # ***********

    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, balance):
        if not isinstance(balance, int):
            raise TypeError("Balance must be an integer.")
        elif balance <= 0:
            raise ValueError("Balance must be greater than 0.")
        else:
            self._balance = balance

    @property
    def status(self):
        return "Active" if self._status else "Closed"
    @status.setter
    def status(self, status):
        if not isinstance(status, bool):
            raise TypeError("Active state must be a boolean.")
        else:
            self._status = status