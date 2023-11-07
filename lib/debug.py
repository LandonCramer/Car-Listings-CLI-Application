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
current_date = datetime.now()

fleet = helpers.generate_fleet()
for car in fleet:
    car.save()
sm1 = Salesman(fake.name(), 75_000, helpers.rand_date())
sm2 = Salesman(fake.name(), 71000, helpers.rand_date())
sm3 = Salesman(fake.name(), 75_000, helpers.rand_date())
sm4 = Salesman(fake.name(), 71000, helpers.rand_date())
st1 = ServiceTech(fake.name(), 75_000, helpers.rand_date())
st2 = ServiceTech(fake.name(), 71000, helpers.rand_date())
man = Manager(fake.name(), 75_000, helpers.rand_date())

sm1.save()
sm2.save()
st1.save()
st2.save()
sm3.save()
sm4.save()
man.save()

employees = Employee.get_all()

cust1 = Customer(fake.name(), 9995558765, helpers.rand_date())
cust2 = Customer(fake.name(), 8456777765, helpers.rand_date())
cust3 = Customer(fake.name(), 9995558765, helpers.rand_date())
cust4 = Customer(fake.name(), 8456777765, helpers.rand_date())
cust5 = Customer(fake.name(), 9995558765, helpers.rand_date())
cust6 = Customer(fake.name(), 8456777765, helpers.rand_date())
cust7 = Customer(fake.name(), 9995558765, helpers.rand_date())
cust8 = Customer(fake.name(), 8456777765, helpers.rand_date())
cust9 = Customer(fake.name(), 9995558765, helpers.rand_date())
cust10 = Customer(fake.name(), 8456777765, helpers.rand_date())

cust1.save()
cust2.save()
cust3.save()
cust4.save()
cust5.save()
cust6.save()
cust7.save()
cust8.save()
cust9.save()
cust10.save()

customers = Customer.get_all()

def reset_db():
    cust1 = customers[0]
    cust2 = customers[1]
    cust4 = customers[3]
    cust5 = customers[4]
    cust7 = customers[6]
    
    Car.drop_table()
    Car.create_table()
    Customer.drop_table()
    Customer.create_table()
    cust1.save()
    cust2.save()
    cust3.save()
    cust4.save()
    cust5.save()
    cust6.save()
    cust7.save()
    cust8.save()
    cust9.save()
    cust10.save()
    Employee.drop_table()
    Employee.create_table()
    Appointment.drop_table()
    Appointment.create_table()
    sale1 = Sale('SALE', helpers.rand_date(helpers.bound_rand_date(cust1.join_date)), cust1.id_, sm1.id_, fleet[0].id_, 69_000, 'Active')
    sale2 = Sale('SALE', helpers.rand_date((current_date - cust1.join_date)), cust2.id_, sm1.id_, fleet[2].id_, 9_000, 'Closed')
    sale3 = Sale('SALE', helpers.rand_date((current_date - cust1.join_date)), cust4.id_, sm2.id_, fleet[41].id_, 6_000, 'Active')
    sale4 = Sale('SALE', helpers.rand_date((current_date - cust1.join_date)), cust5.id_, sm3.id_, fleet[33].id_, 19_000, 'Closed')
    sale5 = Sale('SALE', helpers.rand_date((current_date - cust1.join_date)), cust7.id_, man.id_, fleet[12].id_, 16_000, 'Active')
    serv1 = Service('SERVICE', helpers.rand_date(30), 1, 1, 4, 'Radio says demonic-sounding things in Latin on every station.', 200, 'Active')
    serv2 = Service('SERVICE', helpers.rand_date(30), 1, 2, 5, 'I put Monster Energy into the gastank and now it does not run.', 550, 'Closed')
    serv3 = Service('SERVICE', helpers.rand_date(30), 2, 3, 6, 'The car smells like feet.', 400, 'Active')
    serv4 = Service('SERVICE', helpers.rand_date(30), 2, 2, 7, 'The car only goes reverse when my eyes are closed.', 550, 'Closed')
    serv5 = Service('SERVICE', helpers.rand_date(30), 3, 3, 8, 'Will painting flames onto my car make it go faster?', 400, 'Active')
    td1 = Testdrive('TESTDRIVE', helpers.rand_date(30), 1, 1, 1, "The guy drove thru a McDonalds and ordered a 50-pc chicken nugget.")
    td2 = Testdrive('TESTDRIVE', helpers.rand_date(30), 3, 3, 3, "Dude crashed into lightpole then tried to bribe me with an expired Chuck E Cheese coupon.")
    td3 = Testdrive('TESTDRIVE', helpers.rand_date(30), 6, 3, 3, "The customer kept telling me about her toenail collection.")
    td4 = Testdrive('TESTDRIVE', helpers.rand_date(30), 7, 1, 3, "Person did not show up.")
    td5 = Testdrive('TESTDRIVE', helpers.rand_date(30), 2, 2, 3, "Testdrive actually went well.")
    td6 = Testdrive('TESTDRIVE', helpers.rand_date(30), 1, 1, 1, "The guy drove thru a McDonalds and ordered a 50-pc chicken nugget.")
    td7 = Testdrive('TESTDRIVE', helpers.rand_date(30), 3, 3, 34, "Dude crashed into lightpole then tried to bribe me with an expired Chuck E Cheese coupon.")
    td8 = Testdrive('TESTDRIVE', helpers.rand_date(30), 6, 3, 31, "The customer kept telling me about her toenail collection.")
    td9 = Testdrive('TESTDRIVE', helpers.rand_date(30), 7, 1, 4, "Person did not show up.")
    td10 = Testdrive('TESTDRIVE', helpers.rand_date(30), 2, 2, 4, "Testdrive actually went well.")
    td11 = Testdrive('TESTDRIVE', helpers.rand_date(30), 1, 1, 1, "The guy drove thru a McDonalds and ordered a 50-pc chicken nugget.")
    td12 = Testdrive('TESTDRIVE', helpers.rand_date(30), 3, 3, 1, "Dude crashed into lightpole then tried to bribe me with an expired Chuck E Cheese coupon.")
    td13 = Testdrive('TESTDRIVE', helpers.rand_date(30), 6, 3, 4, "The customer kept telling me about her toenail collection.")
    td14 = Testdrive('TESTDRIVE', helpers.rand_date(30), 7, 1, 33, "Person did not show up.")
    td15 = Testdrive('TESTDRIVE', helpers.rand_date(30), 2, 2, 3, "Testdrive actually went well.")

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
    td6.save()
    td7.save()
    td8.save()
    td9.save()
    td10.save()
    td11.save()
    td12.save()
    td13.save()
    td14.save()
    td15.save()



# sale1 = Sale('SALE', datetime.now(), 1, 1, 1, 69_000, 'Active')
# sale2 = Sale('SALE', datetime.now(), 2, 2, 2, 9_000, 'Closed')
# sale3 = Sale('SALE', datetime.now(), 3, 3, 3, 6_000, 'Active')
# sale4 = Sale('SALE', datetime.now(), 4, 2, 4, 19_000, 'Closed')
# sale5 = Sale('SALE', datetime.now(), 5, 3, 5, 16_000, 'Active')
# serv1 = Service('SERVICE', datetime.now(), 1, 1, 4, 'Radio says demonic-sounding things in Latin on every station.', 200, 'Active')
# serv2 = Service('SERVICE', datetime.now(), 1, 2, 5, 'I put Monster Energy into the gastank and now it does not run.', 550, 'Closed')
# serv3 = Service('SERVICE', datetime.now(), 2, 3, 6, 'The car smells like feet.', 400, 'Active')
# serv4 = Service('SERVICE', datetime.now(), 2, 2, 7, 'The car only goes reverse when my eyes are closed.', 550, 'Closed')
# serv5 = Service('SERVICE', datetime.now(), 3, 3, 8, 'Will painting flames onto my car make it go faster?', 400, 'Active')
# td1 = Testdrive('TESTDRIVE', datetime.now(), 1, 1, 1, "The guy drove thru a McDonalds and ordered a 50-pc chicken nugget.")
# td2 = Testdrive('TESTDRIVE', datetime.now(), 3, 3, 3, "Dude crashed into lightpole then tried to bribe me with an expired Chuck E Cheese coupon.")
# td3 = Testdrive('TESTDRIVE', datetime.now(), 6, 3, 3, "The customer kept telling me about her toenail collection.")
# td4 = Testdrive('TESTDRIVE', datetime.now(), 7, 3, 3, "Person did not show up.")
# td5 = Testdrive('TESTDRIVE', datetime.now(), 2, 3, 3, "Testdrive actually went well.")

# sale1.save()
# sale2.save()
# sale3.save()
# sale4.save()
# sale5.save()
# serv1.save()
# serv2.save()
# serv3.save()
# serv4.save()
# serv5.save()
# td1.save()
# td2.save()
# td3.save()
# td4.save()
# td5.save()

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
    reset_db()
    print('Seeded database')
    import ipdb; ipdb.set_trace()