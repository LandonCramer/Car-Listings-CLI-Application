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
            DROP TABLE IF EXISTS sales;
        """
        CURSOR.execute(sql)
        CONN.commit()