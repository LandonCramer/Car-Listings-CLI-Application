import random
from classes.__init__ import CURSOR, CONN
from helpers import current_date

class Car:
    all = []

    # ! Approved Types
    VEHICLE_TYPES = ['COUPE', 'SEDAN', 'TRUCK', 'VAN', 'SUV']
    FUEL_TYPES = ['GAS', 'DIESEL', 'ELECTRIC', 'HYBRID']

    def __init__(self, vehicle_type, new, make, model, miles, fuel_type, color, transmission, year=None, price=None, id_ = None, owner_id = None, sale_id = None):
        self.vehicle_type = vehicle_type
        self.new = new
        self.make = make
        self.model = model
        self.miles = miles
        self.fuel_type = fuel_type
        self.color = color
        self.transmission = transmission
        self.year = year
        self.price = price
        self.id_ = id_
        # TODO Compute owner_id based on sale_id else None
        self.owner_id = owner_id
        self.sale_id = sale_id
        type(self).all.append(self)

    # ! Properties
    @property
    def vehicle_type(self):
        return self._vehicle_type.title()
    @vehicle_type.setter
    def vehicle_type(self, vehicle_type):
        if hasattr(self, 'vehicle_type'):
            raise ValueError('Vehicle type can not be reset')
        elif vehicle_type not in type(self).VEHICLE_TYPES:
            raise ValueError(f'Vehicle type must be one of the following: {[v_type for v_type in self.VEHICLE_TYPES]}')
        else:
            self._vehicle_type = vehicle_type

    # TODO Should we store the bool or the new/used in the db?
    @property
    def new(self):
        return 'New' if self._new else 'Used'
    @new.setter
    def new(self, new):
        if not isinstance(new, bool):
            raise TypeError('New value must be a boolean.')
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
    
    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, year):
        if hasattr(self, 'year'):
            raise ValueError('Year can not be reset')
        elif not isinstance(year, int) or isinstance(year, bool):
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
        if not isinstance(miles, int) or isinstance(miles, bool):
            raise TypeError('Miles must be an integer.')
        elif miles not in range(0, 300_000):
            raise ValueError('Mileage must be less than 300,000.')
        else:
            self._miles = miles

    @property
    def fuel_type(self):
        return self._fuel_type.title()
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

    # TODO Should we store the bool or the auto/manual in the db?
    @property
    def transmission(self):
        return 'Automatic' if self._transmission else 'Manual'
    @transmission.setter
    def transmission(self, transmission):
        if hasattr(self, 'transmission'):
            raise ValueError('Transmission cannot be re-assigned.')
        elif not isinstance(transmission, bool):
            raise TypeError('Transmission value must be a boolean.')
        else:
            self._transmission = transmission

    # TODO Bell curve price weights
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
            self._price = int(max(8_000, min(price, 1_000_000)))
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
    def owner_id(self):
        return self._owner_id
    @owner_id.setter
    def owner_id(self, owner_id):
        if not owner_id:
            self._owner_id = None
        elif not isinstance(owner_id, int) or isinstance(owner_id, bool):
            raise TypeError("Owner ID must be an integer.")
        else:
            self._owner__id = owner_id

    @property
    def sale_id(self):
        return self._sale_id 
    @sale_id.setter
    def sale_id(self, sale_id):
        if not sale_id:
            self._sale_id = None
        elif not isinstance(sale_id, int) or isinstance(sale_id, bool):
            raise TypeError("Appointment ID must be an integer.")
        else:
            self._sale_id = sale_id

    # TODO Bell curve weights. Right now all cars seems to be poor for some reason.
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
    
    # ! ORM Class Methods
    @classmethod
    def create_table(cls):
        CURSOR.execute(
            '''
            CREATE TABLE IF NOT EXISTS cars (
                id INTEGER PRIMARY KEY,
                vehicle_type TEXT,
                new INTEGER,
                make TEXT,
                model TEXT,
                year INTEGER,
                miles INTEGER,
                fuel_type TEXT,
                color TEXT,
                transmission INTEGER,
                price INTEGER,
                owner_id INTEGER,
                sale_id INTEGER
            );
            '''
        )
        CONN.commit()

    # FOREIGN KEY owner_id INTEGER references customers(id)
    # FOREIGN KEY sale_id INTEGER references appointments(id)

    @classmethod
    def drop_table(cls):
        CURSOR.execute(
            '''
            DROP TABLE IF EXISTS cars;
            '''
        )
        CONN.commit()
    
    @classmethod
    def create(cls, vehicle_type, new, make, model, year, miles, fuel_type, color, transmission, price, id_, owner_id, sale_id):
        new_car = cls(vehicle_type, new, make, model, year, miles, fuel_type, color, transmission, price, id_, owner_id, sale_id)
        new_car.save()
        return new_car
    
    @classmethod
    def new_from_db(cls, row):
        return cls(
                row[1], # vehicle_type
                bool(row[2]), # new
                row[3], # make
                row[4], # model
                row[6], # miles
                row[7], # fuel_type
                row[8], # color
                bool(row[9]), # transmission
                row[5], # year
                row[10], # price
                row[0], # id_
                row[11], # owner_id
                row[12] # sale_id
                )

    @classmethod
    def get_all(cls):

        CURSOR.execute(
            '''
            SELECT * FROM cars;
            '''
        )
        rows = CURSOR.fetchall()
        return [cls.new_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id_):
        CURSOR.execute(
            '''
            SELECT * FROM cars
            WHERE id = ?
            ''',
            (id_,)
        )
        row = CURSOR.fetchone()
        return cls.new_from_db(row) if row else None
    
    # TODO find_by_name seems inappropriate for Car because there is nothing stopping identical cars from existing.
    # TODO What other unique property besides name can we query cars by?
    # @classmethod
    # def find_by_name(cls, name):
    #     CURSOR.execute(
    #         '''
    #         SELECT * FROM cars
    #         WHERE id = ?
    #         ''',
    #         (name,)
    #     )
    #     row = CURSOR.fetchone()
    #     return cls.new_from_db(row) if row else None
    
    # def find_or_create_by(cls, vehicle_type, new, make, model, year, miles, fuel_type, color, transmission, price, id, owner_id, sale_id):
    #     return cls.find_by_name()

    # ! ORM Instance Methods

    def save(self):
        CURSOR.execute(
            '''
            INSERT INTO cars (vehicle_type, new, make, model, year, miles, fuel_type, color, transmission, price, id, owner_id, sale_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''',
            (self._vehicle_type, self._new, self.make, self.model, self.year, self.miles, self._fuel_type, self.color, self._transmission, self.price, self.id_, self.owner_id, self.sale_id)
        )
        CONN.commit()
        self.id = CURSOR.lastrowid
        return self
    
    def update(self):
        CURSOR.execute(
            '''
            UPDATE cars
            SET vehicle_type = ?, new = ?, make = ?, model = ?, year = ?, miles = ?, fuel_type = ?, color = ?, transmission = ?, price = ?, owner_id = ?, sale_id = ?
            WHERE id = ?
            ''',
            (self.vehicle_type, self.new, self.make, self.model, self.year, self.miles, self.fuel_type, self.color, self.transmission, self.price, self.id_, self.owner_id, self.sale_id)
        )
        CONN.commit()
        return self
    
    def delete(self):
        CURSOR.execute(
            '''
            DELETE FROM cars
            WHERE id = ?
            ''',
            (self.id_,)
        )
        CONN.commit()
        self.id = None
        return self

    # ! Class Methods
    @classmethod
    def cars_in_shop(cls):
        pass

    def test_driven_cars(cls):
        pass

    def owned_cars(cls):
        pass

    def top_cars(cls):
        pass

    def search_cars(cls):
        pass

    def filter_cars(cls):
        pass

    def get_cars_by_person(cls):
        pass

    # ! Instance Methods
    def appts(self):
        pass

    def services(self):
        pass

    def test_drives(self):
        pass

    def assoc_people(self):
        pass

    def employees(self):
        pass

    def customers(self): 
        pass

    def list_details(self):
        print(f'--- {self.year} {self.make.upper()} {self.model.upper()} ---\nColor: {self.color}\nFuel Type: {self._fuel_type}\nMiles: {self.miles}\nCondition: {self.condition}\nPrice: {self.price}')
    
    def full_details(self):
        print(f'Vehicle Type: {self.vehicle_type}\nNew or Used: {self.new}\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}\nMiles: {self.miles}\nFuel Type: {self.fuel_type}\nColor: {self.color}\nTransmission: {self.transmission}\nPrice: {self.price}')