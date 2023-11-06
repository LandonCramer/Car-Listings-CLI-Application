from datetime import datetime
from helpers import parse_date
from classes.Sale import Sale
from classes.Service import Service
from classes.Testdrive import Testdrive
from classes.__init__ import CURSOR, CONN

class Appointment:
    all = {}

    APPT_TYPES = ['SALE', 'SERVICE', 'TESTDRIVE']

    def __init__(self, type_, date, customer_id, employee_id, car_id, id=None):
        self.type_ = type_
        self.date = date
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.car_id = car_id
        self.id = id
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
    def customer_id(self):
        return self._customer_id
    @customer_id.setter
    def customer_id(self, customer_id):
        if not customer_id:
            self._customer_id = None
        elif not isinstance(customer_id, int) or isinstance(customer_id, bool):
            raise TypeError("Customer ID must be an integer.")
        else:
            self._customer_id = customer_id

    @property
    def employee_id(self):
        return self._employee_id
    @employee_id.setter
    def employee_id(self, employee_id):
        if not employee_id:
            self._employee_id = None
        elif not isinstance(employee_id, int) or isinstance(employee_id, bool):
            raise TypeError("Employee ID must be an integer.")
        else:
            self._employee_id = employee_id

    @property
    def car_id(self):
        return self._car_id
    @car_id.setter
    def car_id(self, car_id):
        if not car_id:
            self._car_id = None
        elif not isinstance(car_id, int) or isinstance(car_id, bool):
            raise TypeError("Car ID must be an integer.")
        else:
            self._car_id = car_id

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

    @classmethod
    def get_all(cls):
        pass

    @classmethod
    def get_appts_by_type(cls, type_):
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
        if self.type_ == 'SALE':
            Sale().save()
        elif self.type_ == 'SERVICE':
            Service().save()
        elif self.type_ == 'TESTDRIVE':
            Testdrive().save()
        else:
            raise ValueError('We do not offer that service.')
        
        sql = """
            INSERT INTO appointments (type, date, customer_id, employee_id, car_id)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.type_, self.date, self.customer_id, self.employee_id, self.car_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, type_, date, customer_id, employee_id, car_id):
        appointment = cls(type_, date, customer_id, employee_id, car_id)
        appointment.save()

        cls.all[appointment.id] = appointment

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
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None