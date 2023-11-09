import random
from classes.__init__ import CURSOR, CONN
from helpers import current_date, year_range
from classes.Appointment import Appointment
from classes.Testdrive import Testdrive

class Car:

    def __init__(self, vehicle_type, new, make, model, miles, fuel_type, color, transmission, year=None, price=None, id_=None, owned=False):
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
        self.owned = owned
        self.id_ = id_

    # **************
    # APPROVED LISTS
    # **************

    VEHICLE_TYPES = ['COUPE', 'SEDAN', 'TRUCK', 'VAN', 'SUV']
    FUEL_TYPES = ['GAS', 'DIESEL', 'ELECTRIC', 'HYBRID']

    # *********************
    # CREATE / DROP TABLES
    # *********************

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
                owned INTEGER
            );
            '''
        )
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute(
            '''
            DROP TABLE IF EXISTS cars;
            '''
        )
        CONN.commit()

    # **********
    # PROPERTIES
    # **********

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

    @property
    def new(self):
        return self._new
    @new.setter
    def new(self, new):
        if not isinstance(new, str):
            raise TypeError("New value must be either 'New' or 'Used'.")
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
        elif year not in year_range:
            raise ValueError(f'Year must be between {current_date().year - 100} and {current_date().year + 1}.')
        else:
            self._year = year

    @property
    def miles(self):
        return self._miles
    @miles.setter
    def miles(self, miles):
        if not isinstance(miles, int) or isinstance(miles, bool):
            raise TypeError('Miles must be an integer.')
        elif miles not in range(300_000):
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

    @property
    def transmission(self):
        return self._transmission
    @transmission.setter
    def transmission(self, transmission):
        if hasattr(self, 'transmission'):
            raise ValueError('Transmission cannot be re-assigned.')
        elif not isinstance(transmission, str):
            raise TypeError('Transmission value must be "Automatic" or "Manual".')
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
            price = base_price + (self.miles * miles_weight) + ((current_date().year - self.year) * age_weight) + (condition_weights[self.condition] * base_price)

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
    def owned(self):
        return self._owned
    @owned.setter
    def owned(self, owned):
        if not isinstance(owned, int):
            raise TypeError("Owned must be an boolean.")
        else:
            self._owned = owned

    # TODO Bell curve weights. Right now all cars seems to be poor for some reason.
    @property
    def condition(self):
        if self.miles == 0:
            return 'New' 
    
        age_weight = current_date().year - self.year / 15
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
    
    # ******
    # CREATE
    # ******

    def save(self):
        CURSOR.execute(
            '''
            INSERT INTO cars (vehicle_type, new, make, model, year, miles, fuel_type, color, transmission, price, id, owned)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''',
            (self._vehicle_type, self._new, self.make, self.model, self.year, self.miles, self._fuel_type, self.color, self._transmission, self.price, self.id_, self.owned)
        )
        CONN.commit()
        self.id = CURSOR.lastrowid
        return self

    @classmethod
    def create(cls, vehicle_type, new, make, model, year, miles, fuel_type, color, transmission, price, id_=None, owned=False):
        new_car = cls(vehicle_type, new, make, model, year, miles, fuel_type, color, transmission, price, id_, owned)
        new_car.save()
        return new_car
    
    @classmethod
    def instance_from_db(cls, row):
        return cls(
                row[1], # vehicle_type
                row[2], # new
                row[3], # make
                row[4], # model
                row[6], # miles
                row[7], # fuel_type
                row[8], # color
                row[9], # transmission
                row[5], # year
                row[10], # price
                bool(row[11]), # owned
                row[0] # id_
                )

    # ****
    # READ
    # ****

    @classmethod
    def get_by(cls, param='all', value=None):
        if isinstance(value, str) and value in ('vehicle_type', 'fuel_type'):
            value.strip().upper()
        elif isinstance(value, str):
            value.strip()
        elif not isinstance(value, int):
            raise TypeError(
                'Value must be an integer or string.'
            )

        search_params = ['all', 'id', 'vehicle_type', 'new', 'make', 'model', 'year', 'miles', 'fuel_type', 'color', 'transmission', 'price']
        
        if param not in search_params:
            raise ValueError("Incorrect search parameter inputted.")

        if param == 'all':
            sql = """
                SELECT * FROM cars
            """
        else:
            sql = f"""
                SELECT * FROM cars
                WHERE {param} = '{value}'
            """

        rows = CURSOR.execute(sql).fetchall()
        
        if not rows:
            print('No results found.')
            return
        
        elif len(rows) == 1:
            return cls.instance_from_db(rows[0])
        else:
            return [cls.instance_from_db(row) for row in rows]

    # ******
    # UPDATE
    # ******

    def update(self):
        CURSOR.execute(
            '''
            UPDATE cars
            SET vehicle_type = ?, new = ?, make = ?, model = ?, year = ?, miles = ?, fuel_type = ?, color = ?, transmission = ?, price = ? owned = ?
            WHERE id = ?
            ''',
            (self.vehicle_type, self.new, self.make, self.model, self.year, self.miles, self.fuel_type, self.color, self.transmission, self.price, self.id_, self.owned)
        )
        CONN.commit()
        return self

    # *******
    # DESTROY
    # *******
    
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

    # *************
    # CLASS METHODS
    # *************

    @classmethod
    def cars_w_appts(cls):
        CURSOR.execute(f"""
        SELECT DISTINCT cars.*
        FROM cars
        JOIN appointments ON cars.id = appointments.car_id
        """
        )
        rows = CURSOR.fetchall()
        return [Car.instance_from_db(row) for row in rows] if rows else None

    @classmethod
    def test_driven_cars(cls):
        CURSOR.execute(f"""
        SELECT DISTINCT cars.*
        FROM cars
        JOIN appointments ON cars.id = appointments.car_id
        WHERE type = 'TESTDRIVE'
        """
        )
        rows = CURSOR.fetchall()
        return [Car.instance_from_db(row) for row in rows] if rows else None

    @classmethod
    def cars_serviced(cls):
        CURSOR.execute(f"""
        SELECT DISTINCT cars.*
        FROM cars
        JOIN appointments ON cars.id = appointments.car_id
        WHERE type = 'SERVICE'
        """
        )
        rows = CURSOR.fetchall()
        return [Car.instance_from_db(row) for row in rows] if rows else None
    
    @classmethod
    def cars_in_shop(cls):
        CURSOR.execute(f"""
        SELECT DISTINCT cars.*
        FROM cars
        JOIN appointments ON cars.id = appointments.car_id
        WHERE type = 'SERVICE' AND status = 'Active'
        """
        )
        rows = CURSOR.fetchall()
        return [Car.instance_from_db(row) for row in rows] if rows else None
    
    @classmethod
    def owned_cars(cls):
        from classes.Sale import Sale
        return [Car.get_by('id', value.car_id) for value in Sale.all.values()]

    @classmethod
    def top_cars(cls, list_len):
        driven_car_ids = {}
        for testdrive in Testdrive.get_by():
            if testdrive.car_id in driven_car_ids.keys():
                driven_car_ids[testdrive.car_id] = driven_car_ids[testdrive.car_id] + 1
            else:
                driven_car_ids[testdrive.car_id] = 1
        tuple_list = [(key, value) for key, value in driven_car_ids.items()]
        top_cars = []
        for car in sorted(tuple_list, key=lambda x: x[1])[:list_len]:
            top_cars.append(cls.get_by('id', car[1]))
        return top_cars

    # TODO

    @classmethod
    def search_cars(cls, search_dict):

        # search_dict = {'vehicle_types': ['COUPE', 'VAN', 'TRUCK'], 'new': ['New'], 'makes': ['Any'], 'model': ['any'], 'year': [1978], 'miles': [250000], 'fuel_types': ['GAS'], 'colors': ['any'], 'transmission': ['Manual'], 'price': [1000000]}
        
        print(search_dict)

        search_params = []

        for value_list in search_dict.values():
            if not isinstance(value_list[0], int) and value_list[0].lower() == 'any':
                search_params.append('NOT NULL')
            elif all(isinstance(item, int) for item in value_list):
                search_params.append(str(value_list[0]))
            else:
                result_string = ''
                for val in value_list:
                    if value_list.index(val) == 0:
                        result_string = result_string + f"'{val}'"
                    else:
                        result_string = result_string + f" OR '{val}'"
                search_params.append(result_string)

        print(search_params)

        conditions = [
        "vehicle_type IS NOT NULL" if search_params[2] == 'NOT NULL' else f"vehicle_type = {search_params[2]}",
        "new IS NOT NULL" if search_params[3] == 'NOT NULL' else f"new = {search_params[3]}",
        "make IS NOT NULL" if search_params[4] == 'NOT NULL' else f"make = {search_params[4]}",
        "model IS NOT NULL" if search_params[0] == 'NOT NULL' else f"model = {search_params[0]}",
        "year IS NOT NULL" if search_params[5] == 'NOT NULL' else f"year > 0 ",
        "miles IS NOT NULL" if search_params[6] == 'NOT NULL' else f"miles < 1000000",
        "fuel_type IS NOT NULL" if search_params[7] == 'NOT NULL' else f"fuel_type = {search_params[7]}",
        "color IS NOT NULL" if search_params[1] == 'NOT NULL' else f"color = {search_params[1]}",
        "transmission IS NOT NULL" if search_params[8] == 'NOT NULL' else f"transmission = {search_params[8]}",
        "price IS NOT NULL" if search_params[9] == 'NOT NULL' else f"price < 1000000"
        ]

        # conditions = ["vehicle_type = 'COUPE' OR 'VAN' OR 'SEDAN'", "new = New", "make IS NOT NULL", "model IS NOT NULL", "year > '1978'", "miles < '250000'", "fuel_type = 'GAS' OR 'ELECTRIC'", "color IS NOT NULL", "transmission = 'Automatic'", "price < '1000000'"]

        print(conditions)

        sql = """
            SELECT *
            FROM cars
            WHERE {}
        """.format(" AND ".join(conditions))

        rows = CURSOR.execute(sql).fetchall()
        cars = []

        print(sql)
        print(rows)

        if not rows:
            print('No results found.')
            return
        elif len(rows) == 1:
            cars = [cls.instance_from_db(rows[0])]
        else:
            cars = [cls.instance_from_db(row) for row in rows]

        print(cars)
        return cars

    # ****************
    # INSTANCE METHODS
    # ****************

    def appts(self):
        return Appointment.get_by('car_id', self.id_)
        
    def services(self):
        return [appt for appt in self.appts() if appt.type_ == 'SERVICE']

    def open_tickets(self):
        return [service for service in self.services() if service.status == 'Active']

    def service_history(self):
        return [service for service in self.services() if service.status == 'Closed']

    def test_drives(self):
        return [appt for appt in self.appts() if appt.type_ == 'TESTDRIVE']

    def employees(self):
        from classes.Employee import Employee
        employee_ids = {appt.employee_id for appt in self.appts()}
        employees = []
        for id_ in employee_ids:
            employees.append(Employee.get_by('id', id_))
        return employees

    def customers(self): 
        from classes.Customer import Customer
        cust_ids = {appt.customer_id for appt in self.appts()}
        custs = []
        for id_ in cust_ids:
            custs.append(Customer.get_by('id', id_))
        return custs

    def list_details(self):
        print(f'--- {self.year} {self.make.upper()} {self.model.upper()} ---\nColor: {self.color}\nFuel Type: {self._fuel_type}\nMiles: {self.miles}\nCondition: {self.condition}\nPrice: {self.price}')
    
    def full_details(self):
        print(f'Vehicle Type: {self.vehicle_type}\nNew or Used: {self.new}\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}\nMiles: {self.miles}\nFuel Type: {self.fuel_type}\nColor: {self.color}\nTransmission: {self.transmission}\nPrice: {self.price}')