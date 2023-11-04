from datetime import datetime
from helpers import parse_date

class Employee:
    def __init__(self, name, salary, hire_date):
        self.name = name
        self.salary = salary
        self.hire_date = hire_date
    
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
        return parse_date(self._hire_date)
    
    @hire_date.setter
    def hire_date(self, hire_date):
        if not isinstance(hire_date, datetime):
            raise TypeError('Hire date must be a valid Date object.')
        else:
            self._hire_date = hire_date