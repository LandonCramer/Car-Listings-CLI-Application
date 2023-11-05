from classes.__init__ import CURSOR, CONN

class Service:
    all = {}

    def __init__(self, reason_for_visit='The radio says demonic-sounding things in Latin on every station.', estimate=500):
        self.reason_for_visit = reason_for_visit
        estimate = estimate
    
    # *********************
    # CREATE / DROP TABLES
    # *********************

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY,
            FOREIGN KEY (appt_id) REFERENCES appointments.id ON DELETE CASCADE,
            reason_for_visit TEXT,
            active TEXT     
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

    # ***********
    # PROPERTIES
    # ***********

    @property
    def reason_for_visit(self):
        return self._reason_for_visit
    @reason_for_visit.setter
    def reason_for_visit(self, reason):
        if not isinstance(reason, str):
            raise TypeError("Reason for visit must be a string.")
        elif len(reason) > 150:
            raise ValueError("Reason for visit must be less than 150 characters.")
        else:
            self._reason_for_visit = reason

    @property
    def estimate(self):
        return self._estimate
    @estimate.setter
    def estimate(self, estimate):
        if not isinstance(estimate, int):
            raise TypeError("Estimate value must be an integer.")
        elif estimate <= 0:
            raise ValueError("Estimate must be greater than 0.")
        else:
            self._estimate = estimate