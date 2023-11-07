from datetime import datetime
from classes.Appointment import Appointment
from classes.Car import Car
from classes.Sale import Sale
from classes.Service import Service
from classes.Testdrive import Testdrive
from classes.Customer import Customer
import helpers
import random
from classes.Salesman import Salesman
from classes.ServiceTech import ServiceTech
from classes.Manager import Manager
from classes.Employee import Employee
from faker import Faker

# python lib/debug.py

fake = Faker()

def setup_db():
    Customer.drop_table()
    Employee.drop_table()
    Car.drop_table()
    Appointment.drop_table()

    Customer.create_table()
    Employee.create_table()
    Car.create_table()
    Appointment.create_table()

    cust1 = Customer.create(fake.name(), 9995558765, helpers.rand_date())
    cust2 = Customer.create(fake.name(), 8456777765, helpers.rand_date())
    cust3 = Customer.create(fake.name(), 9995558765, helpers.rand_date())
    cust4 = Customer.create(fake.name(), 8456777765, helpers.rand_date())
    cust5 = Customer.create(fake.name(), 9995558765, helpers.rand_date())
    cust6 = Customer.create(fake.name(), 8456777765, helpers.rand_date())
    cust7 = Customer.create(fake.name(), 9995558765, helpers.rand_date())
    cust8 = Customer.create(fake.name(), 8456777765, helpers.rand_date())
    cust9 = Customer.create(fake.name(), 9995558765, helpers.rand_date())
    cust10 = Customer.create(fake.name(), 8456777765, helpers.rand_date())
        
    # sm1 = Salesman.create(fake.name(), 75_000, helpers.rand_date())
    # sm2 = Salesman.create(fake.name(), 71000, helpers.rand_date())
    # sm3 = Salesman.create(fake.name(), 75_000, helpers.rand_date())
    # sm4 = Salesman.create(fake.name(), 71000, helpers.rand_date())
    # st1 = ServiceTech.create(fake.name(), 75_000, helpers.rand_date())
    # st2 = ServiceTech.create(fake.name(), 71000, helpers.rand_date())
    # man = Manager.create(fake.name(), 75_000, helpers.rand_date())

    # TODO Are these getters and setter defined wrong?
    for car in helpers.generate_fleet():
        car.create(car._vehicle_type, car._new, car._make, car._model, car._miles, car._fuel_type, car._color, car._transmission, car._year, car._price)

    # sale1 = Sale('SALE', helpers.bound_rand_date(cust1.join_date), cust1.id_, sm1.id_, fleet[0].id_, 69_000, 'Active')
    # sale2 = Sale('SALE', helpers.bound_rand_date(cust2.join_date), cust2.id_, sm1.id_, fleet[2].id_, 9_000, 'Closed')
    # sale3 = Sale('SALE', helpers.bound_rand_date(cust4.join_date), cust4.id_, sm2.id_, fleet[41].id_, 6_000, 'Active')
    # sale4 = Sale('SALE', helpers.bound_rand_date(cust5.join_date), cust5.id_, sm3.id_, fleet[33].id_, 19_000, 'Closed')
    # sale5 = Sale('SALE', helpers.bound_rand_date(cust7.join_date), cust7.id_, man.id_, fleet[12].id_, 16_000, 'Active')
    # serv1 = Service('SERVICE', helpers.rand_date(30), cust1.id_, sm1.id_, fleet[0].id_, 'Radio says demonic-sounding things in Latin on every station.', 200, 'Active')
    # serv2 = Service('SERVICE', helpers.rand_date(30), cust1.id_, sm1.id_, fleet[0].id_, 'I put Monster Energy into the gastank and now it does not run.', 550, 'Closed')
    # serv3 = Service('SERVICE', helpers.rand_date(30), cust1.id_, sm1.id_, fleet[0].id_, 'The car smells like feet.', 400, 'Active')
    # serv4 = Service('SERVICE', helpers.rand_date(30), cust1.id_, sm1.id_, fleet[0].id_, 'The car only goes reverse when my eyes are closed.', 550, 'Closed')
    # serv5 = Service('SERVICE', helpers.rand_date(30), cust1.id_, sm1.id_, fleet[0].id_, 'Will painting flames onto my car make it go faster?', 400, 'Active')
    # td1 = Testdrive('TESTDRIVE', helpers.rand_date(30), cust1.id_, sm1.id_, fleet[0].id_, "The guy drove thru a McDonalds and ordered a 50-pc chicken nugget.")
    # td2 = Testdrive('TESTDRIVE', helpers.rand_date(30), cust1.id_, sm1.id_, fleet[0].id_, "Dude crashed into lightpole then tried to bribe me with an expired Chuck E Cheese coupon.")
    # td3 = Testdrive('TESTDRIVE', helpers.rand_date(30), cust1.id_, sm1.id_, fleet[0].id_, "The customer kept telling me about her toenail collection.")
    # td4 = Testdrive('TESTDRIVE', helpers.rand_date(30), cust1.id_, sm1.id_, fleet[0].id_, "Person did not show up.")
    # td5 = Testdrive('TESTDRIVE', helpers.rand_date(30), cust1.id_, sm1.id_, fleet[0].id_, "Testdrive actually went well.")
    # td6 = Testdrive('TESTDRIVE', helpers.rand_date(30), cust1.id_, sm1.id_, fleet[0].id_, "The guy drove thru a McDonalds and ordered a 50-pc chicken nugget.")
    # td7 = Testdrive('TESTDRIVE', helpers.rand_date(30), cust1.id_, sm1.id_, fleet[0].id_, "Dude crashed into lightpole then tried to bribe me with an expired Chuck E Cheese coupon.")
    # td8 = Testdrive('TESTDRIVE', helpers.rand_date(30), cust1.id_, sm1.id_, fleet[0].id_, "The customer kept telling me about her toenail collection.")
    # td9 = Testdrive('TESTDRIVE', helpers.rand_date(30), cust1.id_, sm1.id_, fleet[0].id_, "Person did not show up.")
    # td10 = Testdrive('TESTDRIVE', helpers.rand_date(30), cust1.id_, sm1.id_, fleet[0].id_, "Testdrive actually went well.")
    # td11 = Testdrive('TESTDRIVE', helpers.rand_date(30), cust1.id_, sm1.id_, fleet[0].id_, "The guy drove thru a McDonalds and ordered a 50-pc chicken nugget.")
    # td12 = Testdrive('TESTDRIVE', helpers.rand_date(30), cust1.id_, sm1.id_, fleet[0].id_, "Dude crashed into lightpole then tried to bribe me with an expired Chuck E Cheese coupon.")
    # td13 = Testdrive('TESTDRIVE', helpers.rand_date(30), cust1.id_, sm1.id_, fleet[0].id_, "The customer kept telling me about her toenail collection.")
    # td14 = Testdrive('TESTDRIVE', helpers.rand_date(30), cust1.id_, sm1.id_, fleet[0].id_, "Person did not show up.")
    # td15 = Testdrive('TESTDRIVE', helpers.rand_date(30), cust1.id_, sm1.id_, fleet[0].id_, "Testdrive actually went well.")

if __name__ == '__main__':
    setup_db()
    print('Seeded database')
    import ipdb; ipdb.set_trace()