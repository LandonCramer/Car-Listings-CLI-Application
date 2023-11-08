from datetime import datetime, timedelta
import helpers
from classes.__init__ import CURSOR, CONN
from classes.Customer import Customer
from classes.Appointment import Appointment

class Employee:

    def __init__(self, name, salary, hire_date=None, id_=None, job_title=None):
        dt_obj = hire_date if hire_date else datetime.now()
        self.name = name
        self.salary = salary
        self.hire_date = dt_obj
        self.id_ = id_
        self.job_title = type(self).__name__

    # *********************
    # CREATE / DROP TABLES
    # *********************

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Employee instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name TEXT,
                salary INTEGER,
                job_title TEXT,
                hire_date TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS employees
        """
        
        CURSOR.execute(sql)
        CONN.commit()

    # **********
    # PROPERTIES
    # **********

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
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        if not isinstance(salary, int) or isinstance(salary, bool):
            raise TypeError('Salary must be an integer.')
        elif salary not in range(50_000, 250_001):
            raise ValueError('Salary must be between 50,000 and 250,000.')
        else:
            self._salary = salary

    @property
    def hire_date(self):
        return self._hire_date
    @hire_date.setter
    def hire_date(self, hire_date):
        if isinstance(hire_date, datetime):
            self._hire_date = hire_date
        else:
            raise TypeError('Date must be a valid datetime object.')

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

    # ******
    # CREATE
    # ******

    def save(self):
        """ Insert a new row with the name, salary, and hire date (hire date converted to a string, Format YYYY-MM-DD) """
        sql = """
            INSERT INTO employees (name, salary, job_title, hire_date)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.salary, self.job_title, helpers.parse_date(self.hire_date)))
        CONN.commit()

    # TODO Fix for this error: *** TypeError: create() missing 2 required positional arguments: 'salary' and 'hire_date'
    @classmethod
    def create(cls, der_cls, name, salary, hire_date):
        """ Initialize a new Employee instance and save the object to the database """
        if cls.__name__ == 'Employee':
            raise ValueError(
                'Can only be called on Salesmen, Service Techs, and Manager instances.'
            )
        elif not hire_date:
            hire_date = datetime.now()
        elif not isinstance(hire_date, datetime):
            raise TypeError('Date must be a valid datetime object or a date string in ISO format.')

        employee = der_cls(name, salary, hire_date)
        employee.save()
        return employee

    @classmethod
    def instance_from_db(cls, row):
        return cls(
            row[1], #name
            row[2], #salary
            helpers.parse_date(row[4]), #hire_date
            row[0], #id_
            row[3] #job_title
        )

    # ****
    # READ
    # ****

    @classmethod
    def get_by(cls, param='all', value=''):
        from classes.Salesman import Salesman; from classes.ServiceTech import ServiceTech; from classes.Manager import Manager;
        if isinstance(value, str):
            value.strip()
        elif not isinstance(value, int):
            raise TypeError(
                'Value must be an integer, string, or valid valid MM/DD/YYYY date.'
            )

        search_params = ['all', 'id', 'name', 'salary', 'job_title', 'hire_date']
        
        if param not in search_params:
            raise ValueError("Incorrect search parameter inputted.")
        
        emp_type = cls.__name__

        if emp_type.upper() == 'EMPLOYEE':
            if param == 'all':
                sql = """
                    SELECT * FROM employees
                """
            else:
                sql = f"""
                    SELECT * FROM employees
                    WHERE {param} = '{value}'
                """
        else:
            if param == 'all':
                sql = f"""
                    SELECT * FROM employees
                    WHERE job_title = '{emp_type}'
                """    
            else:
                sql = f"""
                    SELECT * FROM employees
                    WHERE job_title = '{emp_type}' AND {param} = '{value}'
                """

        rows = CURSOR.execute(sql).fetchall()
        sub_class = rows[0][3] if rows else None

        if not rows:
            print('No results found.')
            return
        elif len(rows) == 1:
            if sub_class == 'Salesman':
                return Salesman.instance_from_db(rows[0])
            elif sub_class == 'ServiceTech':
                return ServiceTech.instance_from_db(rows[0])
            if sub_class == 'Manager':
                return Manager.instance_from_db(rows[0])
        else:
            if sub_class == 'Salesman':
                return [Salesman.instance_from_db(row) for row in rows]
            elif sub_class == 'ServiceTech':
                return [ServiceTech.instance_from_db(row) for row in rows]
            if sub_class == 'Manager':
                return [Manager.instance_from_db(row) for row in rows]

    # ******
    # UPDATE
    # ******

    def update(self):
        """ Update the table row corresponding to the current Employee instance """
        sql = """
            UPDATE employees
            SET name = ?, salary = ?, job_title = ?, hire_date = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.salary, self.job_title, self.hire_date, self.id))
        CONN.commit()

    # *******
    # DESTROY
    # *******

    def delete(self):
        """ Delete the table row corresponding to the current Employee instance """
        sql = """
            DELETE FROM employees
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    # *************
    # CLASS METHODS
    # *************

    @classmethod
    def employee_of_the_month(cls, role):
        one_month_ago = datetime.now() - timedelta(days=30)
        valid_emps = cls.get_by('job_title', role)
        return max(valid_emps, key=lambda x: len([appt for appt in x.appts() if appt.date > one_month_ago]))

    # ****************
    # INSTANCE METHODS
    # ****************

    def appts(self):
        return Appointment.get_by('employee_id', self.id_)

    def testdrives(self):
        if self.job_title in ('Salesman', 'Manager'):
            return [appt for appt in self.appts() if appt.type_ == 'TESTDRIVE'] if self.appts() else None
        else:
            raise ValueError(
                'Only Salesmen and Managers have access to Testdrives.'
            )
    
    def services(self):
        if self.job_title in ('Service Tech', 'Manager'):
            return [appt for appt in self.appts() if appt.type_ == 'SERVICE'] if self.appts() else None
        else:
            raise ValueError(
                'Only Service Techs and Managers have access to Services.'
            )
    
    def sales(self):
        if self.job_title in ('Salesman', 'Manager'):
            return [appt for appt in self.appts() if appt.type_ == 'SALE'] if self.appts() else None
        else:
            raise ValueError(
                'Only Service Techs and Managers have access to Sales.'
            )
    
    def customers(self):
        from classes.Customer import Customer
        cust_ids = {appt.customer_id for appt in self.appts()}
        custs = []
        for id_ in cust_ids:
            custs.append(Customer.find_by_id(id_))
        return custs
    
    def cars(self):
        from classes.Car import Car
        car_ids = {appt.car_id for appt in self.appts()}
        cars = []
        for id_ in car_ids:
            cars.append(Car.find_by_id(id_))
        return cars
    
