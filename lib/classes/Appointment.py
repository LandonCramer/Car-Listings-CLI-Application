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
    def customer_id_(self):
        return self._customer_id_ 
    @customer_id_.setter
    def customer_id_(self, customer_id_):
        if not customer_id_:
            self._customer_id_ = None
        elif not isinstance(customer_id_, int) or isinstance(customer_id_, bool):
            raise TypeError("Customer ID must be an integer.")
        else:
            self._customer_id_ = customer_id_

    @property
    def employee_id_(self):
        return self._employee_id_ 
    @employee_id_.setter
    def employee_id_(self, employee_id_):
        if not employee_id_:
            self._employee_id_ = None
        elif not isinstance(employee_id_, int) or isinstance(employee_id_, bool):
            raise TypeError("Employee ID must be an integer.")
        else:
            self._employee_id_ = employee_id_

    @property
    def car_id_(self):
        return self._car_id_ 
    @car_id_.setter
    def car_id_(self, car_id_):
        if not car_id_:
            self._car_id_ = None
        elif not isinstance(car_id_, int) or isinstance(car_id_, bool):
            raise TypeError("Car ID must be an integer.")
        else:
            self._car_id_ = car_id_

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
    