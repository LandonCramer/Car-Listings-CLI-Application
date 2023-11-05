from datetime import datetime
import random
from helpers import current_date

class Car:
    
    # ! Approved Types
    VEHICLE_TYPES = ['COUPE', 'SEDAN', 'TRUCK', 'VAN', 'SUV']
    FUEL_TYPES = ['GAS', 'DIESEL', 'ELECTRIC', 'HYBRID']

    def __init__(self, vehicle_type, new, make, model, year, miles, fuel_type, color, transmission, price=None, id_ = None, owner_id = None, appt_id = None):
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
        self.id_ = id_
        self.owner_id = owner_id
        self.appt_id = appt_id

    # ! Properties
    @property
    def vehicle_type(self):
        return self._vehicle_type
    @vehicle_type.setter
    def vehicle_type(self, vehicle_type):
        if hasattr(self, 'vehicle_type'):
            raise ValueError('Vehicle type can not be reset')
        elif vehicle_type not in type(self).VEHICLE_TYPES:
            raise ValueError(f'Vehicle type must be one of the following: {[v_type for v_type in self.VEHICLE_TYPES]}')
        else:
            self._vehicle_type = vehicle_type

    @property
    def new(self):
        return self._new
    @new.setter
    def new(self, new):
        if not isinstance(new, bool):
            raise TypeError('New value must be a boolean.')
        elif new:
            self._new = 'New'
        else:
            self._new = "Used"

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
        else:
            self._make = make
        
    @property 
    def model(self):
        return self._model
    @model.setter
    def model(self, model):
        if hasattr(self, 'model'):
            raise ValueError('Model can not be reset')
        elif not isinstance(model, str):
            raise TypeError("Model must be a string.")
        elif len(model) not in range(1, 21):
            raise ValueError("Model must be a string between 1 and 20 characters.")
        else:
            self._model = model
        
    # @property
    # def year(self):
    #     return self._year
    # @year.setter
    # def year(self, year):
    #     if hasattr(self, 'year'):
    #         raise ValueError('Year can not be reset')
    #     elif not isinstance(year, int) or isinstance(year, bool):
    #         raise TypeError('Year must be an int')
    #     elif year not in range(current_date.year - 100, current_date.year + 1):
    #         raise ValueError(f'Year must be between {current_date.year - 100} and {current_date.year + 1}.')
    #     else:
    #         self._year = year

    @property
    def miles(self):
        return self._miles
    @miles.setter
    def miles(self, miles):
        if not isinstance(miles, int) or isinstance(miles, bool):
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
        if fuel_type not in type(self).FUEL_TYPES:
            raise ValueError(f'Type must be one of the following: {[f_type for f_type in type(self).FUEL_TYPES]}')
        else:
            self._fuel_type = fuel_type

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError('Color must be of type string.')
        elif len(color) not in range(1, 21):
            raise ValueError("Color must be a string between 1 and 20 characters.")
        else:
            self._color = color

    @property
    def transmission(self):
        return self._transmission
    @transmission.setter
    def transmission(self, transmission):
        if hasattr(self, 'transmission'):
            raise ValueError('Transmission cannot be re-assigned.')
        elif not isinstance(transmission, bool):
            raise TypeError('Transmission value must be a boolean.')
        elif transmission:
            self._transmission = 'Automatic'
        else:
            self._transmission = "Manual"

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        if not price:
            miles_weight = -0.5  # Lower miles means a higher price
            age_weight = -0.3  # Lower age means a higher price
            condition_weights = {
            'New': 0.4,  # Better condition means a higher price
            'Excellent': 0.3,
            'Very Good': 0.2,
            'Good': 0.1,
            'Fair': 0.0,
            'Poor': -0.1  # Worse condition means a lower price
            }

            # Calculate the price based on the factors and weights
            base_price = random.randint(0, 300_001)
            price = base_price + (self.miles * miles_weight) + ((current_date.year - self.year) * age_weight) + (condition_weights[self.condition] * base_price)

            # Ensure the price is within the valid range (5000 to 500,000)
            self._price = int(max(5_000, min(price, 1_000_000)))
        elif not isinstance(price, int) or isinstance(price, bool):
            raise TypeError('Price must be of type integer.')
        elif price not in range(1_000_000):
            raise ValueError('Price must be between 0 and 1,000,000.')
        else:
            self._price = price


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

    @property
    def owner_id_(self):
        return self._owner_id_ 
    @owner_id_.setter
    def owner_id_(self, owner_id_):
        if not owner_id_:
            self._owner_id_ = None
        elif not isinstance(owner_id_, int) or isinstance(owner_id_, bool):
            raise TypeError("Owner ID must be an integer.")
        else:
            self._owner__id_ = owner_id_

    @property
    def appt_id_(self):
        return self._appt_id_ 
    @appt_id_.setter
    def appt_id_(self, appt_id_):
        if not appt_id_:
            self._appt_id_ = None
        elif not isinstance(appt_id_, int) or isinstance(appt_id_, bool):
            raise TypeError("Appointment ID must be an integer.")
        else:
            self._appt__id_ = appt_id_

    @property
    def condition(self):
        if self.miles == 0:
            return 'New' 
    
        age_weight = current_date.year - self.year / 15
        mileage_weight = self.miles / 200000
        
        condition_score = age_weight + mileage_weight

        if condition_score < 0.4:
            return 'Excellent'
        elif condition_score < 0.7:
            return 'Very Good'
        elif condition_score < 1:
            return 'Good'
        elif condition_score < 1.5:
            return 'Fair'
        else:
            return 'Poor'
    
    # ! Instance Methods
    def list_details(self):
        print(f'--- {self.year} {self.make.upper()} {self.model.upper()} ---\nColor: {self.color}\nFuel Type: {self._fuel_type}\nMiles: {self.miles}\nCondition: {self.condition}\nPrice: {self.price}')
    
    def list_details(self):
        print(f'')