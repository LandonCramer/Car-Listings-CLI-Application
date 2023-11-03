from datetime import datetime

class Car:
    
    VEHICLE_TYPES = ['COUPE', 'SEDAN', 'TRUCK', 'VAN', 'SUV']

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
        if vehicle_type not in VEHICLE_TYPES:
            raise ValueError("Vehicle type must be: 'COUPE', 'SEDAN', 'TRUCK', 'VAN', or 'SUV'.")
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
        if not isinstance(make, str):
            raise TypeError("Make must be a string.")
        elif len(make) not in range(1, 21):
            raise ValueError("Make must be a string between 1 and 20 characters.")
        
    @property 
    def model(self):
        return self._model
    @model.setter
    def make(self, model):
        if not isinstance(model, str):
            raise TypeError("Model must be a string.")
        elif len(model) not in range(1, 21):
            raise ValueError("Model must be a string between 1 and 20 characters.")
        
    
        
    




    
        