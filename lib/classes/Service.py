from classes.__init__ import CURSOR, CONN

class Service:
    all = {}

    def __init__(self, reason_for_visit='The radio says demonic-sounding things in Latin on every station.', estimate=500, status=True, id=None):
        self.reason_for_visit = reason_for_visit
        estimate = estimate
        self.status = "Active" if status else "Closed"
        self.id = id
    
    # *********************
    # CREATE / DROP TABLES
    # *********************

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS services (
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
            DROP TABLE IF EXISTS services;
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
    
    @property
    def status(self):
        return "Active" if self._status else "Closed"
    @status.setter
    def status(self, status):
        if not isinstance(status, bool):
            raise TypeError("Active state must be a boolean.")
        else:
            self._status = "Active" if status else "Closed"

    @property
    def id(self):
        return self._id
    @id.setter
    def id_(self, id):
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
            INSERT INTO sales (reason_for_visit, estimate, status)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.reason_for_visit, self.estimate, self.status))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, reason_for_visit, estimate, status):
        appointment = cls(reason_for_visit, estimate, status)
        appointment.save()

        cls.all[appointment.id] = appointment

        return appointment
    
    def update(self, id):
        sql = """
            UPDATE services
            SET reason_for_visit = ?, estimate = ?, status = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.reason_for_visit, self.estimate, self.status, id))
        CONN.commit()