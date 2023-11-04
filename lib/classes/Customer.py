import re

class Customer:
    def __init__(self, name, phone):
        self._name = name
        self._phone = phone
    
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
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, phone):
        if not re.match('^\d{10}$', phone):
            raise ValueError('Phone number must be a valid 10 digit integer.')
        #TODO if phone found in db raise ValueError
        else:
            self._phone = phone