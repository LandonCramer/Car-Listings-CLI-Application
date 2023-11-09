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
from richstyling import user_input, menu, error, listing, details, qualifier, department

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
        ("Liberty", 'SUV'),
        ("Gladiator", 'TRUCK'),
        ("Compass", 'SUV'),
        ("Renegade", 'SUV'),
        ("Wagoneer", 'VAN'),
        ("Grand Cherokee", 'VAN'),
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

def snake_case_to_title_case(input_string):
    words = input_string.split('_')  # Split the snake case string into words
    title_case_string = ' '.join(word.capitalize() for word in words) 
    if title_case_string == 'Id':
        return 'ID'
    return title_case_string


# *********************
# CLI FUNCTIONS
# *********************

def view_car_details(customer, salesman, car):
    # print(customer, salesman, car)
    pass

def list_cars(customer, salesman, current_list):
    from classes.Car import Car
    table = Table(title="Here are your search results.")

    for key in current_list[0].__dict__.keys():
        if key != '_owned':
            table.add_column(snake_case_to_title_case(key))
    for car in current_list:
        table.add_row(f"{car.vehicle_type}", f"{car.new}", f"{car.make}", f"{car.model}", f"{car.year}", f"{car.miles}", f"{car.fuel_type}", f"{car.color}", f"{car.transmission}", f"{car.price}", f"{car.owned}")

    console = Console()
    console.print(table)

    user_input("Please select a vehicle by Id.")
    selected_id = input()

    view_car_details(customer, salesman, Car.get_by('id',selected_id))
    pass

#customer, salesman
def browse_cars(customer, salesman):
    from classes.Car import Car
    search_dict = {}

    def choose_max_price():
        user_input("Please enter the maximum price you would like to see or Any to see all.")
        choice = input()

        if choice.lower() == "any":
            search_dict["price"] = ["any"]
        elif choice.isdigit() and len(choice):
            price = int(choice)
            search_dict["price"] = [price]
        else:
            error("That is an invalid string.")
            choose_max_price()

        list_cars(customer, salesman, Car.search_cars(search_dict))

    def choose_transmission():
        valid_choices = ['Manual', 'Automatic', 'Any']

        menu("Transmission: Manual, Automatic")
        user_input("Enter Manual, Automatic, or Any:")
        choice = input().strip()

        if choice.title() not in valid_choices:
            error('That is not a valid choice.')
            choose_transmission()
        elif choice.title() == 'Any':
            search_dict['transmission'] = ['any']
        else:
            search_dict['transmission'] = [choice.title()]
        
        choose_max_price()

    def choose_fuel_type():
        valid_choices = ['GAS', 'DIESEL', 'ELECTRIC', 'HYBRID', 'ANY']
   
        menu('Fuel Types: Gas, Diesel, Electric, Hybrid')
        user_input("Enter desired fuel type(s) separated by commas or Any to see all.")
        choice = input()
        fuel_types = [fuel_type.strip().upper() for fuel_type in choice.split(',')]

        for item in fuel_types:
            if item not in valid_choices:
                error("One or more of your choices is not a valid fuel type.")
                choose_fuel_type()
        
        if 'ANY' in fuel_types:
            search_dict['fuel_types'] = ['any']
        else:
            search_dict['fuel_types'] = fuel_types 

        choose_transmission()

    def choose_mileage():
        user_input("Please enter the maximum mileage you would like to see or Any to see all.")
        choice = input().strip()

        if choice.lower() == "any":
            search_dict["miles"] = ["any"]
        elif choice.isdigit() and len(choice):
            miles = int(choice)
            search_dict["miles"] = [miles]
        else:
            error("That is an invalid string.")
            choose_mileage()

        choose_fuel_type()

    def choose_year():
        user_input("Please enter a year representing the oldest car you would like to see or Any to see all.")
        choice = input().strip()

        if choice.lower() == "any":
            search_dict["year"] = ["any"]
        elif len(str(choice)) != 4:
            error("Please enter a valid year in format YYYY.")
            choose_year()
        else:
            year = int(choice) 
            search_dict["year"] = [year]
        
        choose_mileage()

    def choose_make():
        valid_choices = ['Ford', 'Chevrolet', 'Audi', 'Jeep', 'Kia', 'Toyota', 'Any']
    
        menu("Makes: Ford, Chevrolet, Audi, Jeep, Kia, Toyota")
        user_input("Enter desired vehicle make(s) separated by commas or Any to see all.")
        choice = input()
        makes = [make.strip().title() for make in choice.split(',')]

        for item in makes:
            if item.title() not in valid_choices:
                error("One or more of your selections is not a valid make.")
                choose_make()
        
        if "Any" in makes:
            search_dict["makes"] = ['any']
        else:
            search_dict['makes'] = makes
        
        choose_year()

    def choose_condition():
        valid_choices = ['New', 'Used', 'Any']

        menu("Condition: New, Used")
        user_input("Enter New, Used, or Any:")
        choice = input().strip()

        if choice.title() not in valid_choices:
            error('That is not a valid choice.')
            choose_condition()
        elif choice.title() == 'Any':
            search_dict['new'] = ['any']
        else:
            search_dict['new'] = [choice.title()]
        
        choose_make()

    def choose_type():
        valid_choices = ['SEDAN', 'COUPE', 'VAN', 'TRUCK', 'SUV', 'ANY']

        menu('Vehicle Types: Sedan, Coupe, Van, Truck, SUV')
        user_input("Enter desired vehicle type(s) separated by commas or Any to see all.")
        choice = input()
        vehicle_types = [vehicle.strip().upper() for vehicle in choice.split(',')]

        for item in vehicle_types:
            if item not in valid_choices:
                error("You have entered one or more incorrect vehicle types.")
                choose_type()

        if 'ANY' in vehicle_types:
            search_dict['vehicle_types'] = ['any']
        else:
            search_dict['vehicle_types'] = vehicle_types 
        
        choose_condition()
    
    model = ["any"]
    search_dict["model"] = model

    colors = ["any"]
    search_dict["colors"] = colors

    choose_type()

def to_lobby(customer):
    menu("Enter a number for your choice:\n1. Sales\n2. Service\n3. Leave Dealership")
    choice = input()
    if int(choice) == 1:
        to_sales(customer)
    elif int(choice) == 2:
        to_service(customer)
    elif int(choice) == 3:
        pass
    else:
        error("Not a valid choice.")
        to_lobby(customer)

def to_service(customer):
    from classes.ServiceTech import ServiceTech
    from classes.Appointment import Appointment
    from classes.Car import Car
    from classes.Service import Service

    service_tech = ServiceTech.get_by('id', random.randint(0, len(ServiceTech.get_by()) - 1))
    
    department("*** WELCOME TO THE SERVICE DEPARTMENT ***")
    menu("How can we help you today?\n1. Drop off a vehicle for service.\n2. Pick up a serviced vehicle.\n3. Return to lobby.")
    choice = input()
    
    if choice == '1':
        new_appt = Appointment.create()
        print('Dropped off!')
    elif choice == '2':
        current_car = customer.cars_in_shop()[0]
        if current_car:
            table = Table(title="Your vehicle is ready for pickup!")
            table.add_column('Date')
            table.add_column('Year')
            table.add_column('Make')
            table.add_column('Model')
            table.add_column('Estimate')
            table.add_column('Status')

            all_appts = Service.get_by('car_id', current_car._id_)
            latest_index = len(all_appts) - 1
            
            for num in range(0, latest_index):
                all_appts[num].status = "Closed"

            for appt in all_appts:
                curr_car = Car.get_by('id', appt.car_id)
                table.add_row(f"{appt.date}", f"{curr_car.year}", f"{curr_car.make}", f"{curr_car.model}", f"{appt.estimate}", f"{appt.status}")
            console = Console()
            console.print(table)

            menu("What would you like to do?\n1. Pick up vehicle.\n2. Return to the service department.\n3. Return to the lobby.\n4. Leave dealership.")          
            choice = input()

            if choice == '1':
                text = Text("THANK YOU FOR YOUR BUSINESS!")
                text.stylize('green')
                print(text)
            elif choice == '2':
                to_service(customer)
            elif choice == '3':
                to_lobby(customer)
            elif choice == '4':
                pass
            else:
                error("That is not a valid option.")
                to_service(customer)
        else:
            error("You do not have any vehicles in the shop.")
            menu("What would you like to do?\n1. Return to the service department.\n2. Return to the lobby.\n3. Leave dealership.")
            choice = input()
            if choice == '1':
                to_service(customer)
            elif choice == '2':
                to_lobby(customer)
            elif choice == '3':
                pass
            else:
                error("That is not a valid option.")
                to_service(customer)
    elif choice == '3':
        to_lobby(customer)
    else:
        error("That is not a valid choice.")
        to_service()
  
def to_sales(customer):
    from classes.Salesman import Salesman
    salesman = Salesman.get_by('id', random.randint(0, len(Salesman.get_by()) - 1))
    
    menu("Enter a number for your choice:\n1. Browse Cars\n2. Return to Lobby")
    choice = input()

    if int(choice) == 1:
        browse_cars(customer, salesman)
    elif int(choice) == 2:
        to_lobby(customer)
    else:
        error("Not a valid choice.")
        to_sales(customer)

def create_customer():
    from classes.Customer import Customer
    user_input('Please enter your phone number.')
    phone = input()
    phone = phone.strip()
    if not re.match('^\d{10}$', phone):
        error('Phone must be a 10 digit number with no spaces or special characters.')
        create_customer()
    else:
        if phone in Customer.phone_numbers():
            searched_customer = Customer.get_by('phone', phone)
            qualifier(f"Are you {searched_customer.name}? Y/N:")
            yn = input()
            if yn.lower() == "y":
                to_lobby(searched_customer)
            elif yn.lower() == "n":
                error("That phone number is already in use.")
                create_customer()
        else:
            user_input('Please enter your name.')
            name = input()
            new_customer = Customer.create(name, phone, datetime.now())
            to_lobby(new_customer)

def welcome():
    department("*** WELCOME TO THE DEALERSHIP ***")
    create_customer()

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()