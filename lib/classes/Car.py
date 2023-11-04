from datetime import datetime
from helpers import current_date

class Car:
    
    VEHICLE_TYPES = ['COUPE', 'SEDAN', 'TRUCK', 'VAN', 'SUV']
    FUEL_TYPES = ['GAS', 'DIESEL', 'ELECTRIC', 'HYBRID']

    def __init__(self, vehicle_type, new, make, model, year, miles, fuel_type, color, transmission, price, owner_id = None, appt_id = None):
        self.vehicle_type = vehicle_type
        self.new = new
        self.make = make
        self.model = model
        self.year = year
        self.miles = miles
        self.fuel_type = fuel_type
        self.color = color
        self.transmission = transmission
        self.price = price
        self.owner_id = owner_id
        self.appt_id = appt_id

    @property
    def vehicle_type(self):
        return self._vehicle_type
    @vehicle_type.setter
    def vehicle_type(self, vehicle_type):
        if hasattr(self, 'vehicle_type'):
            raise ValueError('Vehicle type can not be reset')
        elif vehicle_type not in VEHICLE_TYPES:
            raise ValueError(f'Vehicle type must be one of the following: {[print(type) for type in VEHICLE_TYPES]}')
        else:
            self._vehicle_type = vehicle_type

    @property
    def new(self):
        return self._new
    @new.setter
    def new(self, new):
        if not isinstance(new, bool):
            raise TypeError("New value must be a boolean.")
        else:
            self._new = new

    @property 
    def make(self):
        return self._make
    @make.setter
    def make(self, make):
        if hasattr(self, 'make'):
            raise ValueError('Make can not be reset')
        elif not isinstance(make, str):
            raise TypeError("Make must be a string.")
        elif len(make) not in range(1, 21):
            raise ValueError("Make must be a string between 1 and 20 characters.")
        
    @property 
    def model(self):
        return self._model
    @model.setter
    def make(self, model):
        if hasattr(self, 'model'):
            raise ValueError('Model can not be reset')
        elif not isinstance(model, str):
            raise TypeError("Model must be a string.")
        elif len(model) not in range(1, 21):
            raise ValueError("Model must be a string between 1 and 20 characters.")
        
    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, year):
        if hasattr(self, 'year'):
            raise ValueError('Year can not be reset')
        elif not isinstance(year, int):
            raise TypeError('Year must be an int')
        elif year not in range(current_date.year - 100, current_date.year + 1):
            raise ValueError(f'Year must be between {current_date.year - 100} and {current_date.year + 1}.')
        else:
            self._year = year

    @property
    def miles(self):
        return self._miles
    @miles.setter
    def miles(self, miles):
        if not isinstance(miles, int):
            raise TypeError('Miles must be an integer.')
        elif miles not in range(0, 300_000):
            raise ValueError('Mileage must be less than 300,000.')
        else:
            self._miles = miles

    @property
    def fuel_type(self):
        return self._fuel_type
    @fuel_type.setter
    def fuel_type(self, fuel_type):
        if fuel_type not in FUEL_TYPES:
            raise ValueError(f'Type must be one of the following: {[print(type) for type in FUEL_TYPES]}')
        else:
            self._fuel_type = fuel_type

    