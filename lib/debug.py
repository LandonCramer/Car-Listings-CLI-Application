from datetime import datetime
from classes.Appointment import Appointment
from classes.Car import Car
from classes.Sale import Sale
from classes.Service import Service
from classes.Testdrive import Testdrive
from classes.Customer import Customer
from helpers import rand_date, bound_rand_date, generate_fleet
import random
from classes.Salesman import Salesman
from classes.ServiceTech import ServiceTech
# from classes.Manager import Manager
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

    cust1 = Customer.create(fake.name(), 9995558765, rand_date())
    cust2 = Customer.create(fake.name(), 8474923978, rand_date())
    cust3 = Customer.create(fake.name(), 9957239498, rand_date())
    cust4 = Customer.create(fake.name(), 8453534234, rand_date())
    cust5 = Customer.create(fake.name(), 9997329585, rand_date())
    cust6 = Customer.create(fake.name(), 8857639385, rand_date())
    cust7 = Customer.create(fake.name(), 1284757385, rand_date())
    cust8 = Customer.create(fake.name(), 2748340857, rand_date())
    cust9 = Customer.create(fake.name(), 1203970875, rand_date())
    cust10 = Customer.create(fake.name(), 1308757459, rand_date())
        
    sm1 = Salesman.create(fake.name(), 75_000, rand_date())
    sm2 = Salesman.create(fake.name(), 71000, rand_date())
    sm3 = Salesman.create(fake.name(), 75_000, rand_date())
    sm4 = Salesman.create(fake.name(), 71000, rand_date())
    st1 = ServiceTech.create(fake.name(), 75_000, rand_date())
    st2 = ServiceTech.create(fake.name(), 71000, rand_date())
    # man = Manager.create(fake.name(), 75_000, rand_date())

    # TODO Are these getters and setter defined wrong?
    fleet = generate_fleet()
    for car in fleet:
        car.create(car._vehicle_type, car._new, car._make, car._model, car._miles, car._fuel_type, car._color, car._transmission, car._year, car._price)

    sale1 = Sale.create('SALE', bound_rand_date(cust1.join_date), 1, 1, 1, 69_000, 'Closed')
    sale2 = Sale.create('SALE', bound_rand_date(cust2.join_date), 2, 1, 2, 9_000, 'Closed')
    sale3 = Sale.create('SALE', bound_rand_date(cust4.join_date), 4, 2, 43, 6_000, 'Closed')
    sale4 = Sale.create('SALE', bound_rand_date(cust5.join_date), 5, 3, 6, 19_000, 'Closed')
    sale5 = Sale.create('SALE', bound_rand_date(cust7.join_date), 7, 4, 12, 16_000, 'Closed')
    sale6 = Sale.create('SALE', bound_rand_date(cust1.join_date), 1, 4, 11, 69_000, 'Closed')
    sale7 = Sale.create('SALE', bound_rand_date(cust2.join_date), 2, 1, 24, 9_000, 'Closed')
    sale8 = Sale.create('SALE', bound_rand_date(cust4.join_date), 4, 3, 42, 6_000, 'Closed')
    sale9 = Sale.create('SALE', bound_rand_date(cust5.join_date), 8, 2, 16, 19_000, 'Closed')
    sale10 = Sale.create('SALE', bound_rand_date(cust7.join_date), 10, 2, 22, 16_000, 'Closed')
    sale11 = Sale.create('SALE', bound_rand_date(cust1.join_date), 1, 1, 14, 69_000, 'Closed')
    sale12 = Sale.create('SALE', bound_rand_date(cust2.join_date), 2, 1, 21, 9_000, 'Closed')
    sale13 = Sale.create('SALE', bound_rand_date(cust4.join_date), 4, 2, 41, 6_000, 'Closed')
    sale14 = Sale.create('SALE', bound_rand_date(cust5.join_date), 5, 1, 3, 19_000, 'Closed')
    sale15 = Sale.create('SALE', bound_rand_date(cust7.join_date), 7, 7, 5, 16_000, 'Closed')
    
    serv1 = Service.create('SERVICE', bound_rand_date(st1.hire_date), 1, 5, 1, 'Radio says demonic-sounding things in Latin on every station.', 200, 'Active')
    serv2 = Service.create('SERVICE', bound_rand_date(st2.hire_date), 1, 6, 1, 'I put Monster Energy into the gastank and now it does not run.', 550, 'Closed')
    serv3 = Service.create('SERVICE', bound_rand_date(st1.hire_date), 7, 5, 12, 'The car smells like feet.', 400, 'Active')
    serv4 = Service.create('SERVICE', bound_rand_date(st2.hire_date), 4, 6, 43, 'The car only goes reverse when my eyes are closed.', 550, 'Closed')
    serv5 = Service.create('SERVICE', bound_rand_date(st2.hire_date), 1, 6, 1, 'Will painting flames onto my car make it go faster?', 400, 'Active')
    td1 = Testdrive.create('TESTDRIVE', bound_rand_date(sm1.hire_date), 1, 1, 1, "The guy drove thru a McDonalds and ordered a 50-pc chicken nugget.")
    td2 = Testdrive.create('TESTDRIVE', bound_rand_date(sm1.hire_date), 3, 1, 1, "Dude crashed into lightpole then tried to bribe me with an expired Chuck E Cheese coupon.")
    td3 = Testdrive.create('TESTDRIVE', bound_rand_date(sm1.hire_date), 3, 1, 3, "The customer kept telling me about her toenail collection.")
    td4 = Testdrive.create('TESTDRIVE', bound_rand_date(sm1.hire_date), 1, 1, 3, "Person did not show up.")
    td5 = Testdrive.create('TESTDRIVE', bound_rand_date(sm2.hire_date), 4, 2, 1, "Testdrive actually went well.")
    td6 = Testdrive.create('TESTDRIVE', bound_rand_date(sm3.hire_date), 7, 3, 1, "The guy drove thru a McDonalds and ordered a 50-pc chicken nugget.")
    td7 = Testdrive.create('TESTDRIVE', bound_rand_date(sm4.hire_date), 6, 4, 3, "Dude crashed into lightpole then tried to bribe me with an expired Chuck E Cheese coupon.")
    td8 = Testdrive.create('TESTDRIVE', bound_rand_date(sm4.hire_date), 7, 4, 1, "The customer kept telling me about her toenail collection.")
    td9 = Testdrive.create('TESTDRIVE', bound_rand_date(sm1.hire_date), 1, 1, 3, "Person did not show up.")
    td10 = Testdrive.create('TESTDRIVE', bound_rand_date(sm1.hire_date), 1, 1, 33, "Testdrive actually went well.")
    td11 = Testdrive.create('TESTDRIVE', bound_rand_date(sm3.hire_date), 7, 3, 3, "The guy drove thru a McDonalds and ordered a 50-pc chicken nugget.")
    td12 = Testdrive.create('TESTDRIVE', bound_rand_date(sm2.hire_date), 7, 2, 1, "Dude crashed into lightpole then tried to bribe me with an expired Chuck E Cheese coupon.")
    td13 = Testdrive.create('TESTDRIVE', bound_rand_date(sm3.hire_date), 8, 3, 22, "The customer kept telling me about her toenail collection.")
    td14 = Testdrive.create('TESTDRIVE', bound_rand_date(sm3.hire_date), 10, 3, 4, "Person did not show up.")
    td15 = Testdrive.create('TESTDRIVE', bound_rand_date(sm2.hire_date), 9, 2, 5, "Testdrive actually went well.")

    owned_cars = [Car.get_by('id', id_) for id_ in Sale.owned_cars()]
    for car in owned_cars:
        car.owned = True
        car.update()

if __name__ == '__main__':
    setup_db()

    print('Seeded database')
    import ipdb; ipdb.set_trace()