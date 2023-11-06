from datetime import datetime
from classes.Appointment import Appointment
from classes.Car import Car
from classes.Sale import Sale
from classes.Service import Service
from classes.Testdrive import Testdrive
from classes.Customer import Customer

from helpers import rand_car, generate_fleet
from classes.Salesman import Salesman
from classes.ServiceTech import ServiceTech

# python lib/debug.py

# cust = Customer('Landon', 9995558765, 1)
# emp = Employee('Matteo', 75_000, datetime.now(), 1)
fleet = generate_fleet()

def reset_db():
    Car.drop_table()
    Car.create_table()

def seed_db():
    reset_db()
    for car in fleet:
        car.save()

td = Testdrive('TESTDRIVE', datetime.now(), 2, 2, 2, 2, 'teststring')
sale = Sale('SALE', datetime.now(), 1, 1, 1, 1)
service = Service('SERVICE', datetime.now(), 3, 3, 3, 3)
salesman = Salesman('Landon', 80000, datetime.now(), 1)
st = ServiceTech('Landon', 80000, datetime.now(), 1)
# Appointment.drop_table()
# Appointment.create_table()
# Sale.drop_table()
# Sale.create_table()
# Service.drop_table()
# Service.create_table()
# Testdrive.drop_table()
# Testdrive.create_table()
# appt1 = Appointment('SALE', datetime.now(), 1, 1, 1, 1)
# appt2 = Appointment('TESTDRIVE', datetime.now(), 2, 2, 2, 2)
# appt3 = Appointment('SERVICE', datetime.now(), 3, 3, 3, 3)
# appt4 = Appointment('SERVICE', datetime.now(), 4, 4, 4, 4)
# appt5 = Appointment('TESTDRIVE', datetime.now(), 5, 5, 5, 5)
# appt1.save()
# appt2.save()
# appt3.save()
# appt4.save()
# appt5.save()


if __name__ == '__main__':
    seed_db()
    print('Seeded database')
    import ipdb; ipdb.set_trace()