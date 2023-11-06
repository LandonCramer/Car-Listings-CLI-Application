from datetime import datetime
from helpers import parse_date
from classes.__init__ import CURSOR, CONN


# I added Job_title and hire_date not sure if you want it but just in case...

class Employee:
    def __init__(self, name, salary, hire_date, id_ = None, job_title = None):
        self.name = name
        self.salary = salary
        
        self.hire_date = hire_date
        self.id_ = id_
        self.job_title = type(self).__name__
    
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

    # @property
    # def job_title(self):
    #     return self._job_title

    # @job_title.setter
    # def job_title(self):
    #     self._job_title = str(type(self))
    # def job_title(self, job_title):
    #     if isinstance(job_title, str) and len(job_title) > 0:
    #         self._job_title = job_title
    #     else:
    #         raise ValueError(
    #             "job_title must be a non-empty string"
    #         )
    
    @property
    def hire_date(self):
        return parse_date(self._hire_date)
    
    @hire_date.setter
    def hire_date(self, hire_date):
        if not isinstance(hire_date, datetime):
            raise TypeError('Hire date must be a valid Date object.')
        else:
            self._hire_date = hire_date

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
    def get_all(cls):
        """ Return a list containing Employee objects per row in the table """
        sql = """
            SELECT *
            FROM employees
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.new_from_db(row) for row in rows]

    def save(self):
        """ Insert a new row with the name, salary, and hire date (hire date converted to a string, Format YYYY-MM-DD) """
        sql = """
            INSERT INTO employees (name, salary, job_title, hire_date)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.salary, self.job_title, self.hire_date.strftime('%Y-%m-%d')))
        CONN.commit()

    @classmethod
    def create(cls, name, salary, job_title, hire_date):
        """ Initialize a new Employee instance and save the object to the database """
        employee = Employee(name, salary, job_title, hire_date)
        employee.save()
        return employee

    def update(self):
        """ Update the table row corresponding to the current Employee instance """
        sql = """
            UPDATE employees
            SET name = ?, salary = ?, job_title = ?, hire_date = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.salary, self.job_title, self.hire_date.strftime('%Y-%m-%d'), self.id))
        CONN.commit()

    def delete(self):
        """ Delete the table row corresponding to the current Employee instance """
        sql = """
            DELETE FROM employees
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()