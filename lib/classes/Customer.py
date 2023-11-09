import re
from classes.__init__ import CURSOR, CONN
import helpers
from datetime import datetime
from classes.Car import Car
from classes.Appointment import Appointment

class Customer:
    def __init__(self, name, phone, join_date, id_=None):
        self._name = name
        self._phone = phone
        self._join_date = join_date
        self._id_ = id_
    
    # *********************
    # CREATE / DROP TABLES
    # *********************

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Customer instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT,
                phone TEXT,
                join_date TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS customers
        """
        
        CURSOR.execute(sql)
        CONN.commit()   

    # ***********
    # PROPERTIES
    # ***********

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string.')
        elif not name:
            raise ValueError('Name must be a non-empty string.')
        else:
            self._name = name
    
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, phone):
        if not re.match('^\d{10}$', phone):
            raise ValueError('Phone number must be a valid 10 digit integer.')
        else:
            self._phone = phone

    @property
    def join_date(self):
        return self._join_date
    @join_date.setter
    def join_date(self, join_date):
        if isinstance(join_date, datetime):
            self._join_date = join_date
        else:
            raise TypeError('Date must be a valid datetime object.')
    
    @property
    def id_(self):
        return self._id_ 
    @id_.setter
    def id_(self, id_):
        if not (isinstance(id_, int) and id_ != None) or isinstance(id_, bool):
            raise TypeError("ID must be an integer.")
        else:
            self._id_ = id_

    # ******
    # CREATE
    # ******

    def save(self):
        """ Insert a new row with the name, phone, and join date (join date converted to a string, Format YYYY-MM-DD) """
        sql = """
            INSERT INTO customers (name, phone, join_date)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.phone, helpers.parse_date(self.join_date)))
        CONN.commit()

    @classmethod
    def create(cls, name, phone, join_date):
        """ Initialize a new Customer instance and save the object to the database """
        customer = cls(name, phone, join_date)
        customer.save()
        return customer

    @classmethod
    def instance_from_db(cls, row):
        return cls(
            row[1], #name
            row[2], #phone
            helpers.parse_date(row[3]), #join_date
            row[0] #id_
        )

    # ****
    # READ
    # ****

    @classmethod
    def get_by(cls, param='all', value=None):
        if isinstance(value, str):
            value.strip()
        elif not isinstance(value, int):
            raise TypeError(
                'Value must be an integer, string, or valid MM/DD/YYYY date.'
            )

        search_params = ['all', 'id', 'name', 'phone', 'join_date']
        
        if param not in search_params:
            raise ValueError("Incorrect search parameter inputted.")

        elif param == 'all':
            sql = """
                SELECT * FROM customers
            """
        else:
            sql = f"""
                SELECT * FROM customers
                WHERE {param} = '{value}'
            """

        rows = CURSOR.execute(sql).fetchall()
        
        if not rows:
            print('No results found.')
            return
        
        elif len(rows) == 1:
            return cls.instance_from_db(rows[0])
        else:
            return [cls.instance_from_db(row) for row in rows]
    
    # ******
    # UPDATE
    # ******

    def update(self):
        """ Update the table row corresponding to the current Customer instance """
        sql = """
            UPDATE customers
            SET name = ?, phone = ?, join_date = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.phone, self.join_date, self.id_))
        CONN.commit()

    # *******
    # DESTROY
    # *******

    def delete(self):
        """ Delete the table row corresponding to the current Customer instance """
        sql = """
            DELETE FROM customers
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id))
        CONN.commit()

    # ****************
    # INSTANCE METHODS
    # ****************

    def appts(self):
        return Appointment.get_by('customer_id', self.id_)
    
    def active_services(self):
        from classes.Service import Service
        return [Service.get_by('id', service.id_) for appt in self.appts() if appt.type_ == 'SERVICE' and appt.status == 'Active'] if self.appts() else None

    def cars_test_driven(self):
        return [Car.get_by('id', appt.car_id) for appt in self.appts() if appt.type_ == 'TESTDRIVE'] if self.appts() else None
    
    def cars_serviced(self):
        return [Car.get_by('id', appt.car_id) for appt in self.appts() if appt.type_ == 'SERVICE' and appt.status == 'Closed'] if self.appts() else None

    def cars_in_shop(self):
        return [Car.get_by('id', appt.car_id) for appt in self.appts() if appt.type_ == 'SERVICE' and appt.status == 'Active'] if self.appts() else None

    def cars_owned(self):
        return [Car.get_by('id', appt.car_id) for appt in self.appts() if appt.type_ == 'SALE'] if self.appts() else None

    def employees(self):
        from classes.Employee import Employee
        employee_ids = {appt.employee_id for appt in self.appts()}
        employees = []
        for id_ in employee_ids:
            employees.append(Employee.get_by('id', id_))
        return employees
    
    # *************
    # CLASS METHODS
    # *************

    @classmethod
    def phone_numbers(cls):
        CURSOR.execute("""
            SELECT phone FROM customers
            """)
        rows = CURSOR.fetchall()
        return [row[0] for row in rows] if rows else None
