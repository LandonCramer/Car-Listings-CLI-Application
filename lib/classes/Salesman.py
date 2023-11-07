from classes.Employee import Employee

class Salesman(Employee):
    def __init__ (self, name, salary, hire_date, id_ = None, job_title=None):
        super().__init__(name, salary, hire_date, id_, job_title)

    @classmethod
    def find_by_id(cls, id_):
        super().find_by_id(cls, id_)