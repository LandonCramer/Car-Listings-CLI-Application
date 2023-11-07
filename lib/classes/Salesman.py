from classes.Employee import Employee
from datetime import datetime

class Salesman(Employee):
    def __init__(self, name, salary, hire_date=None, id_ = None, job_title=None):
        super().__init__(name, salary, hire_date, id_, job_title)

    def save(self):
        super().save()

    @classmethod
    def create(cls, job_title, name, salary, hire_date=None):
        employee = cls(name, salary, hire_date)
        employee.save()
        return employee
