from classes.__init__ import CURSOR, CONN

class Testdrive:
    all = {}

    def __init__(self, notes="He went through a McDonalds drive-thru and ordered a 50 pc McNuggets.", id=None):
        self.notes = notes
        self.id = id
    
    # *********************
    # CREATE / DROP TABLES
    # *********************

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS testdrives (
            id INTEGER PRIMARY KEY,
            appt_id INTEGER,
            notes TEXT)
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
    
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        if not id:
            self._id = None
        elif not isinstance(id, int) or isinstance(id, bool):
            raise TypeError("ID must be an integer.")
        else:
            self._id = id
    
    # *************
    # CLASSMETHODS
    # *************

    # ************
    # ORM METHODS
    # ************

    def save(self):
        sql = """
            INSERT INTO testdrives (notes)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.notes,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, notes):
        appointment = cls(notes)
        appointment.save()

        cls.all[appointment.id] = appointment

        return appointment
    
    def update(self, id):
        sql = """
            UPDATE testdrives
            SET notes = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.notes, id))
        CONN.commit()