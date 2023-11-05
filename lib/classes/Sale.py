from classes.__init__ import CURSOR, CONN

class Sale:
    all = {}

    def __init__(self, balance=50_000, active=True):
        self.balance = balance
        self.active = "Active" if active == True else "Closed"
    
    # *********************
    # CREATE / DROP TABLES
    # *********************

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY,
            FOREIGN KEY (appt_id) REFERENCES appointments.id ON DELETE CASCADE,
            balance INTEGER,
            active: TEXT
            
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS sales
        """
        CURSOR.execute(sql)
        CONN.commit()

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
    def active(self):
        return "Active" if self._active else "Closed"
    @active.setter
    def active(self, active):
        if not isinstance(active, bool):
            raise TypeError("Active state must be a boolean.")
        else:
            self._active = "Active" if active else "Closed"