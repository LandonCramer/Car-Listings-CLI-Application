from classes.__init__ import CURSOR, CONN
from classes.Appointment import Appointment

class Testdrive(Appointment):
    all = {}

    def __init__(self, type_, date, customer_id, employee_id, car_id, notes, id_=None): 
        super().__init__(type_, date, customer_id, employee_id, car_id, id_)
        self.notes = notes

    # ***********
    # PROPERTIES
    # ***********

    @property
    def notes(self):
        return self._notes
    @notes.setter
    def notes(self, notes):
        if not isinstance(notes, str):
            raise TypeError("Notes must be a string.")
        elif len(notes) > 150:
            raise ValueError("Notes must be less than 150 characters.")
        else:
            self._notes = notes