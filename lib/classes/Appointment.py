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
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY,
            type TEXT,
            date TEXT,
            customer_id INTEGER,
            employee_id INTEGER,
            car_id INTEGER,
            balance INTEGER,
            reason_for_visit TEXT,
            estimate INTEGER,
            notes TEXT,
            status INTEGER,
            FOREIGN KEY (customer_id) references customers(id),
            FOREIGN KEY (employee_id) references employees(id),
            FOREIGN KEY (car_id) references cars(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = f"""
            DROP TABLE IF EXISTS appointments
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
        return self._date
    @date.setter
    def date(self, date):
        if isinstance(date, datetime):
            self._date = parse_date(date)
        elif isinstance(date, str):
            self._date = date
        else:
            raise TypeError('Date must be a valid Date object or string.')

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

    # **************
    # CLASS METHODS
    # **************

    @classmethod
    def instance_from_db(cls, row):
        instance_id = row[0]
        row = list(row)
        row.pop(0)

        relevant_values = [item for item in row if item != '*']

        if row[0] == 'SALE':
            a, b, c, d, e, f, g = relevant_values
            from classes.Sale import Sale
            updated = Sale(a, b, c, d, e, f, g)
        elif row[0] == 'SERVICE':
            a, b, c, d, e, f, g, h = relevant_values
            from classes.Service import Service
            updated = Service(a, b, c, d, e, f, g, h)
        elif row[0] == 'TESTDRIVE':
            a, b, c, d, e, f = relevant_values
            from classes.Testdrive import Testdrive
            updated = Testdrive(a, b, c, d, e, f)
        else:
            raise ValueError("Invalid class name.")
        
        updated.id_ = instance_id
        cls.all[instance_id] = updated

        return updated

    @classmethod
    def get_by(cls, param='all', value=None):
        search_params = ['all', 'date', 'customer_id', 'employee_id', 'car_id', 'status']
        
        if param not in search_params:
            raise ValueError("Incorrect search parameter inputted.")
        
        appt_type = cls.__name__.upper()

        if appt_type == 'APPOINTMENT':
            if param == 'all':
                sql = """
                    SELECT * FROM appointments
                """
            else:
                sql = f"""
                    SELECT * FROM appointments
                    WHERE {param} = '{value}'
                """
        else:
            if param == 'all':
                sql = f"""
                    SELECT * FROM appointments
                    WHERE type = '{appt_type}'
                """    
            else:
                sql = f"""
                    SELECT * FROM appointments
                    WHERE type = '{appt_type}' AND {param} = '{value}'
                """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    # *************
    # CRUD METHODS
    # *************

    def save(self):
        attr_dict = self.__dict__
        all_keys = ['_type_', '_date', '_customer_id', '_employee_id', '_car_id', '_balance', '_reason_for_visit', '_estimate', '_notes', '_status']
        all_values = []

        for key in all_keys:
            if key in attr_dict.keys():
                all_values.append(attr_dict[key])
            else:
                all_values.append('*')

        if self.type_ == 'SALE' or self.type_ == 'SERVICE' or self.type_ == 'TESTDRIVE':
            sql = """
                INSERT INTO appointments (type, date, customer_id, employee_id, car_id, balance, reason_for_visit, estimate, notes, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
        else:
            raise ValueError('We do not offer that service.')
          
        CURSOR.execute(sql, tuple(all_values))
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
                UPDATE appointments
                SET balance = ?, status = ?
                WHERE id = ?
            """
            updated = (self.balance, self.status, self.id_)
        elif self.type_ == 'SERVICE':
            sql = """
                UPDATE appointments
                SET reason_for_visit = ?, estimate = ?, status = ?
                WHERE id = ?
            """
            updated = (self.reason_for_visit, self.estimate, self.status, self.id_)
        elif self.type_ == 'TESTDRIVE':
            sql = """
                UPDATE appointments
                SET notes = ?
                WHERE id = ?
            """
            updated = (self.notes, self.id_)
        else:
            raise ValueError("That is not a valid appointment type.")

        CURSOR.execute(sql, updated)
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