# python helpers.py

from datetime import datetime
import random

current_date = datetime.now()

def parse_date(datetime_obj):
    return f'{datetime_obj.month}/{datetime_obj.day}/{datetime_obj.year}'

random_car_stuff = {
    'Ford': [
    "F-150",
    "Escape",
    "Explorer",
    "Edge",
    "Mustang",
    "Ranger",
    "Expedition",
    "Fusion",
    "Focus",
    "Bronco"
],
    'Chevrolet': [
    "Malibu",
    "Camaro",
    "Silverado",
    "Equinox",
    "Traverse",
    "Tahoe",
    "Suburban",
    "Impala",
    "Blazer",
    "Corvette"
],
    'Audi': [
    "A3",
    "A4",
    "A5",
    "A6",
    "A7",
    "A8",
    "Q3",
    "Q5",
    "Q7",
    "Q8"
],
    'Jeep': [
    "Wrangler",
    "Cherokee",
    "Grand Cherokee",
    "Gladiator",
    "Compass",
    "Renegade",
    "Wagoneer",
    "Grand Wagoneer",
    "Commander",
    "Patriot"
],
    'Kia': [
    "Seltos",
    "Sportage",
    "Forte",
    "Sorento",
    "Soul",
    "Optima",
    "Telluride",
    "Stinger",
    "Rio",
    "Cadenza"
],
    'Toyota': [    
        "Corolla",
        "Camry",
        "Rav4",
        "Prius",
        "Highlander",
        "Tacoma",
        "Sienna",
        "Yaris",
        "Tundra",
        "Supra"
        ]
}

# TODO We will eventually have to bind this to the model of the car somehow.
def rand_v_type():
    return random.choice(['COUPE', 'SEDAN', 'TRUCK', 'VAN', 'SUV'])

# TODO ^ Maybe match a v_type value to each model in random cars, and assign v_type based on that value after make and model.
def rand_make_and_model():
    make, models = random.choice(list(random_car_stuff.items()))
    selected_model = random.choice(models)
    return (make, selected_model)

# TODO The further you are away from current_date.year, the smaller your weight is for random.choice
def rand_year():
    year = random.randint(current_date.year - 100, current_date.year)
    return year

# TODO Weight miles to favor average miles and not extreme values.
def rand_miles():
    return random.randint(0, 300_001)

def rand_fuel_type():
    options = ['GAS', 'DIESEL', 'ELECTRIC', 'HYBRID']
    weights = [0.65, 0.2, 0.15, 0.2]
    return random.choices(options, weights=weights , k=1)[0]

def rand_color():
    return random.choice(['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'white', 'cyan', 'magenta']).title()

def rand_car():
    from classes.Car import Car
    make_and_model = rand_make_and_model()
    return Car(
        rand_v_type(),
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
        car = rand_car()
        fleet.append(car)
    
    return fleet