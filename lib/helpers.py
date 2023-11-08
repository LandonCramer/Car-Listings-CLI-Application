# python helpers.py
from datetime import datetime, timedelta
import random
import re
from rich import print
from rich import box
from rich.text import Text
from rich.panel import Panel
from rich.table import Table
from rich.console import Console




def current_date():
    return datetime.now()

year_range = range(current_date().year - 100, current_date().year + 1)
miles_range = range(300_001)

def parse_date(date):
    if isinstance(date, str):
        return datetime.strptime(date, '%m/%d/%Y')
    elif isinstance(date, datetime):
        return datetime.strftime(date, '%-m/%-d/%Y')
    else:
        raise TypeError(
            'Date must be a valid datetime object or a date string.'
            )

def rand_date(interval=(1*365)):
    current_time = datetime.now()
    start_date = current_time - timedelta(days=interval)
    return start_date + timedelta(days=random.randint(0, (current_time - start_date).days))

def bound_rand_date(dt_obj, current_date=None):
    if isinstance(dt_obj, datetime):
        current_date = datetime.now()
        return rand_date((current_date - dt_obj).days)
    else:
        raise ValueError(
            'Arguments must be datetime objects.'
        )

# TODO Add regex checkers to make sure all user input phones and dates are in the right format. 

def datetime_to_dict(dt):
    date_dict = {
        'year': dt.year,
        'month': dt.month,
        'day': dt.day,
        'hour': dt.hour,
        'minute': dt.minute,
        'second': dt.second,
        'weekday': dt.weekday(),  # 0 for Monday, 1 for Tuesday, ..., 6 for Sunday
        'week': dt.isocalendar()[1]  # ISO week number
    }
    return date_dict

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
    weights = [i - current_date().year + 75 for i in years]  # Weights favoring recent years
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
    weights = [0.65, 0.1, 0.15, 0.2]
    return random.choices(options, weights=weights , k=1)[0]

def rand_color():
    colors = [
        'Black',
        'Grey',
        'White',
        'Blue',
        'Red',
        'Gold',
        'Green'
    ]
    weights = [
        0.19,
        0.29,
        0.26,
        0.23,
        0.01,
        0.01,
        0.01
    ]
    return random.choices(colors, weights=weights, k=1)[0]

def rand_new():
    bools = ['New', 'Used']
    weights = [0.75, 0.25]
    return random.choices(bools, weights=weights, k=1)[0]

def rand_transmission():
    bools = ['Automatic', 'Manual']
    weights = [0.75, 0.25]
    return random.choices(bools, weights=weights, k=1)[0]

def rand_car():
    from classes.Car import Car
    make_and_model = rand_vehicle()
    return Car(
        make_and_model[2],
        rand_new(),
        make_and_model[0], 
        make_and_model[1],
        rand_miles(),
        rand_fuel_type(),
        rand_color(),
        rand_transmission(),
        rand_year()
        )

def generate_fleet():

    fleet = []

    for _ in range(50):
        fleet.append(rand_car())
    
    return fleet

# *********************
# CLI FUNCTIONS
# *********************

def browse_cars(customer, salesman):
    print(customer, salesman)

def to_sales(customer):
    from classes.Salesman import Salesman

    salesman = Salesman.find_by_id(random.randint(0, len(Salesman.get_all()) -1))
    text = Text("Enter a number for your choice:\n1. Browse Cars\n2. My Cars\n3. Sell Car\n4. Return to Lobby")
    text.stylize('cyan')
    print(Panel.fit(text))
    choice = input()

    if int(choice) == 1:
        browse_cars(customer, salesman)
    elif int(choice) == 2:
        #my_cars(customer, salesman)
        pass
    elif int(choice) == 3:
        pass
    elif int(choice) == 4:
        pass
    else:
        text = Text("Not a valid choice.")
        text.stylize('magenta')
        print(Panel.fit(text))
        to_sales(customer)

def to_lobby(customer):
    text = Text("Enter a number for your choice:\n1. Sales\n2. Service\n3. Leave Dealership")
    text.stylize('cyan')
    print(Panel.fit(text))
    choice = input()
    if int(choice) == 1:
        to_sales(customer)
    elif int(choice) == 2:
        #to_service(customer)
        pass
    elif int(choice) == 3:
        pass
    else:
        text = Text("Not a valid choice.")
        text.stylize('magenta')
        print(Panel.fit(text))
        to_lobby(customer)

def welcome():
    text = Text("*** WELCOME TO THE DEALERSHIP ***")
    text.stylize('bold blue')
    print(Panel.fit(text))

def create_customer():
    from classes.Customer import Customer
    text = Text('Please enter your phone:')
    text.stylize('green')
    print(text)
    phone = input()
    phone = phone.strip()
    if not re.match('^\d{10}$', phone):
        text = Text('Phone must be a 10 digit number with no spaces or special characters.')
        text.stylize('magenta')
        print(Panel.fit(text))
        create_customer()
    else:
        if phone in Customer.phone_numbers():
            searched_customer = Customer.get_by('phone', phone)
            text = Text(f"Are you {searched_customer.name}? Y/N:")
            text.stylize('yellow')
            print(Panel.fit(text))
            yn = input()
            if yn.lower() == "y":
                to_lobby(searched_customer)
            elif yn.lower() == "n":
                text = Text("That phone number is already in use.")
                text.stylize('magenta')
                print(Panel.fit(text))
                create_customer()
        else:
            text = Text("Please enter your name:")
            text.stylize('green')
            print(text)
            name = input()
            new_customer = Customer.create(name, phone, datetime.now())
            to_lobby(new_customer)

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()