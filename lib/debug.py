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
# fleet = generate_fleet()

# def reset_db():
#     Car.drop_table()
#     Car.create_table()

# def seed_db():
#     reset_db()
#     for car in fleet:
#         car.save()

# td = Testdrive('TESTDRIVE', datetime.now(), 2, 2, 2, 2, 'teststring')
# sale = Sale('SALE', datetime.now(), 1, 1, 1, 1)
# service = Service('SERVICE', datetime.now(), 3, 3, 3, 3)
# salesman = Salesman('Landon', 80000, datetime.now(), 1)
# st = ServiceTech('Landon', 80000, datetime.now(), 1)

Sale.drop_table()
Sale.create_table()
Service.drop_table()
Service.create_table()
Testdrive.drop_table()
Testdrive.create_table()

sale1 = Sale('SALE', datetime.now(), 1, 1, 1, 69_000, True)
sale2 = Sale('SALE', datetime.now(), 2, 2, 2, 9_000, True)
sale3 = Sale('SALE', datetime.now(), 3, 3, 3, 6_000, True)
serv1 = Service('SERVICE', datetime.now(), 1, 1, 1, 'Radio makes demonic noises on every station.', 200, True)
serv2 = Service('SERVICE', datetime.now(), 2, 2, 2, 'I put Monster Energy into the gastank and now it does not run.', 550, True)
serv3 = Service('SERVICE', datetime.now(), 3, 3, 3, 'The car smells like feet.', 400, True)
td1 = Testdrive('TESTDRIVE', datetime.now(), 1, 1, 1, "The guy drove through a McDonalds and bought a 50 pc chicken nugget.")
td2 = Testdrive('TESTDRIVE', datetime.now(), 3, 3, 3, "Dude crashed into a Burger King.")
td3 = Testdrive('TESTDRIVE', datetime.now(), 3, 3, 3, "Testdrive actually went well.")
sale1.save()
sale2.save()
sale3.save()
serv1.save()
serv2.save()
serv3.save()
td1.save()
td2.save()
td3.save()
sale1.delete()
serv1.delete()
td1.delete()


if __name__ == '__main__':
    # seed_db()
    print('Seeded database')
    import ipdb; ipdb.set_trace()