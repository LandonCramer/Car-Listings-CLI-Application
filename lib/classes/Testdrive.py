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
            CREATE TABLE IF NOT EXISTS testdrives (
            id INTEGER PRIMARY KEY,
            FOREIGN KEY (appt_id) REFERENCES appointments.id ON DELETE CASCADE,
            notes TEXT
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS testdrives
        """
        CURSOR.execute(sql)
        CONN.commit()    

    # ***********
    # PROPERTIES
    # ***********

    @property
    def notes(self):
        return self._notes
    @notes.setter
    def notes(self, notes):
        if not isinstance(notes, str):
            raise TypeError("Notes must be a string.")
        elif len(notes) > 150:
            raise ValueError("Notes must be less than 150 characters.")
        else:
            self._notes = notes