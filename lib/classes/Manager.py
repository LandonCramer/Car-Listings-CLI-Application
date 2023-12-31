from classes.Salesman import Salesman
from classes.ServiceTech import ServiceTech

class Manager(Salesman, ServiceTech):
    def __init__(self, name, salary, hire_date=None, id_ = None, job_title=None):
        super().__init__(name, salary, hire_date, id_, job_title)
    
    @classmethod
    def create(cls, name, salary, hire_date=None):
        # TODO Specify super for which class to look for.
        return super().create(cls, name, salary, hire_date)