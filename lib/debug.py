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

sale1 = Sale('SALE', datetime.now(), 1, 1, 1, 69_000, 'Active')
sale2 = Sale('SALE', datetime.now(), 2, 2, 2, 9_000, 'Closed')
sale3 = Sale('SALE', datetime.now(), 3, 3, 3, 6_000, 'Active')
sale4 = Sale('SALE', datetime.now(), 4, 2, 4, 19_000, 'Closed')
sale5 = Sale('SALE', datetime.now(), 5, 3, 5, 16_000, 'Active')
serv1 = Service('SERVICE', datetime.now(), 1, 1, 4, 'Radio says demonic-sounding things in Latin on every station.', 200, 'Active')
serv2 = Service('SERVICE', datetime.now(), 1, 2, 5, 'I put Monster Energy into the gastank and now it does not run.', 550, 'Closed')
serv3 = Service('SERVICE', datetime.now(), 2, 3, 6, 'The car smells like feet.', 400, 'Active')
serv4 = Service('SERVICE', datetime.now(), 2, 2, 7, 'The car only goes reverse when my eyes are closed.', 550, 'Closed')
serv5 = Service('SERVICE', datetime.now(), 3, 3, 8, 'Will painting flames onto my car make it go faster?', 400, 'Active')
td1 = Testdrive('TESTDRIVE', datetime.now(), 1, 1, 1, "The guy drove thru a McDonalds and bought a 50 pc chicken nugget.")
td2 = Testdrive('TESTDRIVE', datetime.now(), 3, 3, 3, "Dude crashed into lightpole then tried to bribe me with an expired Chuck E Cheese coupon.")
td3 = Testdrive('TESTDRIVE', datetime.now(), 6, 3, 3, "The customer kept telling me about her toenail collection.")
td4 = Testdrive('TESTDRIVE', datetime.now(), 7, 3, 3, "Person did not show up.")
td5 = Testdrive('TESTDRIVE', datetime.now(), 2, 3, 3, "Testdrive actually went well.")

sale1.save()
sale2.save()
sale3.save()
sale4.save()
sale5.save()
serv1.save()
serv2.save()
serv3.save()
serv4.save()
serv5.save()
td1.save()
td2.save()
td3.save()
td4.save()
td5.save()

# sale1.delete()
# serv1.delete()
# td1.delete()

# sale5.balance = 999999
# serv5.reason_for_visit = "My feet smell like tortilla chips."
# td5.notes = "My colon itches."

# sale5.update()
# serv5.update()
# td5.update()


if __name__ == '__main__':
    # seed_db()
    print('Seeded database')
    import ipdb; ipdb.set_trace()