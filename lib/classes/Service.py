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
            FOREIGN KEY (appt_id) REFERENCES appointments.id
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