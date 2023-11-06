from datetime import datetime
from classes.Appointment import Appointment
from classes.Car import Car
from classes.Sale import Sale
from classes.Service import Service
from classes.Testdrive import Testdrive
from classes.Customer import Customer
import helpers
from classes.Salesman import Salesman
from classes.ServiceTech import ServiceTech

# cust = Customer('Landon', 9995558765, 1)
# emp = Employee('Matteo', 75_000, datetime.now(), 1)
fleet = helpers.generate_fleet()

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