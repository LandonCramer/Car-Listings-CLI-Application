from datetime import datetime
from helpers import parse_date
from Sale import Sale
from Service import Service
from Testdrive import Testdrive
from classes.__init__ import CURSOR, CONN

class Appointment:
    all = {}

    APPT_TYPES = ['SALE', 'SERVICE', 'TESTDRIVE']

    def __init__(self, type_, date, customer_id, employee_id, car_id, id_ = None):
        self.type_ = type_
        self.date = date
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.car_id = car_id
        self.id_ = id_
        # depending on type_, create a row in the respective table
    
    # *********************
    # CREATE / DROP TABLES
    # *********************

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY,
            type TEXT,
            date TEXT,
            customer_id INTEGER,
            employee_id INTEGER,
            car_id INTEGER)
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
    def type_(self):
        return self._type_
    @type_.setter
    def type_(self, type_):
        if type_ not in type(self).APPT_TYPES:
            raise TypeError('Appointment type must be one of the following: SALE, SERVICE, TESTDRIVE')
        else:
            self._type_ = type_

    @property
    def date(self):
        return parse_date(self._date)
    @date.setter
    def date(self, date):
        if not isinstance(date, datetime):
            raise TypeError('Appointment date must be a valid Date object.')
        else:
            self._date = date

    @property
    def customer_id_(self):
        return self._customer_id_ 
    @customer_id_.setter
    def customer_id_(self, customer_id_):
        if not customer_id_:
            self._customer_id_ = None
        elif not isinstance(customer_id_, int) or isinstance(customer_id_, bool):
            raise TypeError("Customer ID must be an integer.")
        else:
            self._customer_id_ = customer_id_

    @property
    def employee_id_(self):
        return self._employee_id_ 
    @employee_id_.setter
    def employee_id_(self, employee_id_):
        if not employee_id_:
            self._employee_id_ = None
        elif not isinstance(employee_id_, int) or isinstance(employee_id_, bool):
            raise TypeError("Employee ID must be an integer.")
        else:
            self._employee_id_ = employee_id_

    @property
    def car_id_(self):
        return self._car_id_ 
    @car_id_.setter
    def car_id_(self, car_id_):
        if not car_id_:
            self._car_id_ = None
        elif not isinstance(car_id_, int) or isinstance(car_id_, bool):
            raise TypeError("Car ID must be an integer.")
        else:
            self._car_id_ = car_id_

    @property
    def id_(self):
        return self._id_ 
    @id_.setter
    def id_(self, id_):
        if not id_:
            self._id_ = None
        elif not isinstance(id_, int) or isinstance(id_, bool):
            raise TypeError("ID must be an integer.")
        else:
            self._id_ = id_

    # *************
    # CLASSMETHODS
    # *************

    @classmethod
    def get_all(cls):
        pass

    @classmethod
    def get_appts_by_type(cls, type):
        pass

    @classmethod
    def get_appts_by_date(cls, date):
        pass

    @classmethod
    def get_appts_by_customer_id(cls, id):
        pass

    @classmethod
    def get_appts_by_employee_id(cls, id):
        pass

    @classmethod
    def get_appts_by_car_id(cls, id):
        pass

    # ************
    # ORM METHODS
    # ************

    def save(self):
        sql = """
            INSERT INTO appointments (type, date, customer_id, employee_id, car_id)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.type_, self.date, self.customer_id, self.employee_id, self.car_id))
        CONN.commit()

        type(self).all[self.id_] = self

    @classmethod
    def create(cls, type, date, customer_id, employee_id, car_id):
        appointment = cls(type, date, customer_id, employee_id, car_id)
        appointment.save()

        cls.all[appointment.id_] = appointment

        return appointment
    
    def update(self, id):
        sql = """
            UPDATE appointments
            SET type = ?, date = ?, customer_id = ?, employee_id = ?, car_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.type_, self.date, self.customer_id, self.employee_id, self.car_id, id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM appointments
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id_,))
        CONN.commit()

        del type(self).all[self.id_]
        self.id_ = None