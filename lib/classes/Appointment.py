from datetime import datetime
from helpers import parse_date

class Appointment:
    def __init__(self, date, customer_id, employee_id, car_id, id_ = None):
        self._date = date
        self._customer_id = customer_id
        self._employee_id = employee_id
        self._car_id = car_id
        self.id_ = id_
    
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
        if not (isinstance(customer_id, int) and customer_id != None) or isinstance(customer_id, bool):
            raise TypeError('Customer ID must be an integer or None.')
        else:
            self._customer_id = customer_id

    @property
    def employee_id(self):
        return self._employee_id
    @employee_id.setter
    def employee_id(self, employee_id):
        if not (isinstance(employee_id, int) and employee_id != None) or isinstance(employee_id, bool):
            raise TypeError('Employee ID must be an integer or None.')
        else:
            self._employee_id = employee_id

    @property
    def car_id(self):
        return self._car_id
    @car_id.setter
    def car_id(self, car_id):
        if not (isinstance(car_id, int) and car_id != None) or isinstance(car_id, bool):
            raise TypeError('Car ID must be an integer or None.')
        else:
            self._car_id = car_id

    @property
    def id_(self):
        return self._id_ 
    @id_.setter
    def id_(self, id_):
        if not (isinstance(id_, int) and id_ != None) or isinstance(id_, bool):
            raise TypeError("ID must be an integer.")
        else:
            self._id_ = id_
    