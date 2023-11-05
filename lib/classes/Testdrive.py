from classes.__init__ import CURSOR, CONN

class Testdrive:
    all = {}

    def __init__(self, notes="He went through a McDonalds drive-thru and ordered a 50 pc McNuggets."):
        self.notes = notes
    
    # *********************
    # CREATE / DROP TABLES
    # *********************

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY,
            FOREIGN KEY (appt_id) REFERENCES appointments.id ON DELETE CASCADE,
            notes TEXT
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS appointments;
        """
        CURSOR.execute(sql)
        CONN.commit()    