# python helpers.py
import re
from datetime import datetime
import random

current_date = datetime.now()
year_range = range(current_date.year - 100, current_date.year + 1)
miles_range = range(300_001)

def parse_date(datetime_obj):
    return f'{datetime_obj.month}/{datetime_obj.day}/{datetime_obj.year}'

def pascal_to_words(string):
    return ' '.join(re.findall(r'[A-Z][a-z0-9]*', string))

# ! Random Fleet Generation Functions

random_car_stuff = {
    'Ford': [
        ("F-150", 'TRUCK'),
        ("Escape", 'SUV'),
        ("Explorer", 'SUV'),
        ("Edge", 'SUV'),
        ("Mustang", 'COUPE'),
        ("Ranger", 'TRUCK'),
        ("Expedition", 'SUV'),
        ("Fusion", 'SEDAN'),
        ("Focus", 'SEDAN'),
        ("Bronco", 'SUV')
    ],
    'Chevrolet': [
        ("Malibu", 'SEDAN'),
        ("Camaro", 'COUPE'),
        ("Silverado", 'TRUCK'),
        ("Equinox", 'SUV'),
        ("Traverse", 'SUV'),
        ("Tahoe", 'SUV'),
        ("Suburban", 'VAN'),
        ("Impala", 'SEDAN'),
        ("Blazer", 'SUV'),
        ("Corvette", 'COUPE')
    ],
    'Audi': [
        ("A3", 'SEDAN'),
        ("A4", 'SEDAN'),
        ("A5", 'COUPE'),
        ("A6", 'SEDAN'),
        ("A7", 'SEDAN'),
        ("A8", 'SEDAN'),
        ("Q3", 'SUV'),
        ("Q5", 'SUV'),
        ("Q7", 'SUV'),
        ("Q8", 'SUV')
    ],
    'Jeep': [
        ("Wrangler", 'SUV'),
        ("Cherokee", 'SUV'),
        ("Grand Cherokee", 'SUV'),
        ("Gladiator", 'TRUCK'),
        ("Compass", 'SUV'),
        ("Renegade", 'SUV'),
        ("Wagoneer", 'VAN'),
        ("Grand Wagoneer", 'VAN'),
        ("Commander", 'SUV'),
        ("Patriot", 'SUV')
    ],
    'Kia': [
        ("Seltos", 'SUV'),
        ("Sportage", 'SUV'),
        ("Forte", 'SEDAN'),
        ("Sorento", 'SUV'),
        ("Soul", 'SUV'),
        ("Optima", 'SEDAN'),
        ("Telluride", 'SUV'),
        ("Stinger", 'COUPE'),
        ("Rio", 'SEDAN'),
        ("Cadenza", 'SEDAN')
    ],
    'Toyota': [
        ("Corolla", 'SEDAN'),
        ("Camry", 'SEDAN'),
        ("Rav4", 'SUV'),
        ("Prius", 'SEDAN'),
        ("Highlander", 'SUV'),
        ("Tacoma", 'TRUCK'),
        ("Sienna", 'VAN'),
        ("Yaris", 'SEDAN'),
        ("Tundra", 'TRUCK'),
        ("Supra", 'COUPE')
    ]
}

def rand_vehicle():
    rand_make, available_models = random.choice(list(random_car_stuff.items()))
    rand_model = random.choice(available_models)
    return (rand_make, rand_model[0], rand_model[1])

def rand_year():
    years = list(year_range)
    weights = [i - current_date.year + 75 for i in years]  # Weights favoring recent years
    return random.choices(years, weights=weights)[0]

def rand_miles():
    miles = list(miles_range)
    weights = [
        10 if i < 100000 else
        3 if i < 200_000 else
        1 for i in miles
    ]  
    return random.choices(miles, weights=weights)[0]

def rand_fuel_type():
    options = ['GAS', 'DIESEL', 'ELECTRIC', 'HYBRID']
    weights = [0.65, 0.2, 0.15, 0.2]
    return random.choices(options, weights=weights , k=1)[0]

def rand_color():
    return random.choice(['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'white', 'cyan', 'magenta']).title()

def rand_car():
    from classes.Car import Car
    make_and_model = rand_vehicle()
    return Car(
        make_and_model[2],
        # TODO Should we weight new so only a certain percentage of cars are used?
        random.choice([True, False]),
        make_and_model[0], 
        make_and_model[1],
        rand_miles(),
        rand_fuel_type(),
        rand_color(),
        # TODO Should we weight new so only a certain percentage of cars are manual?
        random.choice([True, False]),
        rand_year()
        )

def generate_fleet():
    fleet = []

    for _ in range(50):
        fleet.append(rand_car())
    
    return fleet