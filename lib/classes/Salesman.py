from classes.Employee import Employee
from datetime import datetime

class Salesman(Employee):
    def __init__(self, name, salary, hire_date=None, id_ = None, job_title=None):
        super().__init__(name, salary, hire_date, id_, job_title)
    
    @classmethod
    def create(cls, name, salary, hire_date=None):
        return super().create(cls, name, salary, hire_date)
    
    @classmethod
    def get_by(cls, param='all', value=''):
        return super().get_by(param, value)