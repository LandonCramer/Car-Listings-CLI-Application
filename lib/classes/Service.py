from classes.__init__ import CURSOR, CONN
from classes.Appointment import Appointment

class Service(Appointment):
    all = {}

    def __init__(self, type_, date, customer_id, employee_id, car_id, reason_for_visit, estimate, status, id_=None):
        super().__init__(type_, date, customer_id, employee_id, car_id, id_)
        self.reason_for_visit = reason_for_visit
        self.estimate = estimate
        self.status = status

    # *************
    # CREATE TABLE
    # *************

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS services (
            id INTEGER PRIMARY KEY,
            type TEXT,
            date TEXT,
            customer_id INTEGER,
            employee_id INTEGER,
            car_id INTEGER,
            reason_for_visit TEXT,
            estimate INTEGER,
            status INTEGER)
        """
        super().create_table(sql)

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
        return self._status
    @status.setter
    def status(self, status):
        if not isinstance(status, str):
            raise TypeError("Status must be a string.")
        else:
            self._status = status

    # **************
    # CLASS METHODS
    # **************

    @classmethod
    def get_active_appts(cls):
        table_name = cls.__name__.lower() + 's'
        
        sql = f"""
            SELECT * FROM {table_name}
            WHERE status = "Active"
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def get_closed_appts(cls):
        table_name = cls.__name__.lower() + 's'
        
        sql = f"""
            SELECT * FROM {table_name}
            WHERE status = "Closed"
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]