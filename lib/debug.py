from datetime import datetime
from classes.Appointment import Appointment
from classes.Car import Car
from classes.Customer import Customer
from classes.Employee import Employee
from helpers import generate_fleet

# python lib/debug.py

cust = Customer('Landon', 9995558765, 1)
emp = Employee('Matteo', 75_000, datetime.now(), 1)
appt = Appointment(datetime.now(), 1, 1, 1, 1)
fleet = generate_fleet()

def reset_db():
    Car.drop_table()
    Car.create_table()

def seed_db():
    reset_db()
    for car in fleet:
        car.save()

if __name__ == '__main__':
    seed_db()
    print('Seeded database')
    import ipdb; ipdb.set_trace()