from datetime import datetime
from helpers import parse_date
from classes.__init__ import CURSOR, CONN

class Appointment:
    all = {}

    APPT_TYPES = ['SALE', 'SERVICE', 'TESTDRIVE']

    def __init__(self, type_, date, customer_id, employee_id, car_id, id_=None):
        self.type_ = type_
        self.date = date
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.car_id = car_id
        self.id_ = id_
    
    # *********************
    # CREATE / DROP TABLES
    # *********************

    @classmethod
    def create_table(cls, sql):
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        table_name = cls.__name__.lower() + 's'

        sql = f"""
            DROP TABLE IF EXISTS {table_name}
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
    def instance_from_db(cls, row):
        instance_id = row[0]
        row.pop(0)

        if cls.__name__ == 'Sale':
            a, b, c, d, e, f, g = row
            updated = cls(a, b, c, d, e, f, g)
        elif cls.__name__ == 'Service':
            a, b, c, d, e, f, g, h = row
            updated = cls(a, b, c, d, e, f, g, h)
        elif cls.__name__ == 'Testdrive':
            a, b, c, d, e, f = row
            updated = cls(a, b, c, d, e, f)
        else:
            raise ValueError("Invalid class name.")
        
        cls.all[instance_id] = updated
        return updated

    @classmethod
    def get_all(cls):
        table_name = cls.__name__.lower() + 's'
        pass

    @classmethod
    def get_appts_by_date(cls, date):
        table_name = cls.__name__.lower() + 's'
        pass

    @classmethod
    def get_appts_by_customer_id(cls, id):
        table_name = cls.__name__.lower() + 's'
        pass

    @classmethod
    def get_appts_by_employee_id(cls, id):
        table_name = cls.__name__.lower() + 's'
        pass

    @classmethod
    def get_appts_by_car_id(cls, id):
        table_name = cls.__name__.lower() + 's'
        pass

    # ************
    # CRUD METHODS
    # ************

    def save(self):

        attrs = [self.type_, self.date, self.customer_id, self.employee_id, self.car_id]

        if self.type_ == 'SALE':
            sql = """
                INSERT INTO sales (type, date, customer_id, employee_id, car_id, balance, status)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            attrs.append(self.balance)
            attrs.append(self.status)

        elif self.type_ == 'SERVICE':
            sql = """
                INSERT INTO services (type, date, customer_id, employee_id, car_id, reason_for_visit, estimate, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
            attrs.append(self.reason_for_visit)
            attrs.append(self.estimate)
            attrs.append(self.status)

        elif self.type_ == 'TESTDRIVE':
            sql = """
                INSERT INTO testdrives (type, date, customer_id, employee_id, car_id, notes)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            attrs.append(self.notes)

        else:
            raise ValueError('We do not offer that service.')
        
        
        CURSOR.execute(sql, tuple(attrs))
        CONN.commit()

        self.id_ = CURSOR.lastrowid
        type(self).all[self.id_] = self

    @classmethod
    def create(cls, *args):

        if cls.__name__ == 'Sale':
            a, b, c, d, e, f, g = args
            appointment = cls(a, b, c, d, e, f, g)
        elif cls.__name__ == 'Service':
            a, b, c, d, e, f, g, h = args
            appointment = cls(a, b, c, d, e, f, g, h)
        elif cls.__name__ == 'Testdrive':
            a, b, c, d, e, f = args
            appointment = cls(a, b, c, d, e, f)
        else:
            raise ValueError("Invalid class name.")
  
        appointment.save()

        cls.all[appointment.id_] = appointment

        return appointment
    
    def update(self):
        if self.type_ == 'SALE':
            sql = """
                UPDATE sales
                SET balance = ?, status = ?
                WHERE id = ?
            """
            updated = (self.balance, self.status, self.id_)
        elif self.type_ == 'SERVICE':
            sql = """
                UPDATE services
                SET reason_for_visit = ?, estimate = ?, status = ?
                WHERE id = ?
            """
            updated = (self.reason_for_visit, self.estimate, self.status, self.id_)
        elif self.type_ == 'TESTDRIVE':
            sql = """
                UPDATE testdrives
                SET notes = ?
                WHERE id = ?
            """
            updated = (self.notes, self.id_)
        else:
            raise ValueError("That is not a valid appointment type.")

        CURSOR.execute(sql, updated)
        CONN.commit()

    def delete(self):
        table_name = type(self).__name__.lower() + 's'

        sql = f"""
            DELETE FROM {table_name}
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id_,))
        CONN.commit()

        del type(self).all[self.id_]
        self.id_ = None