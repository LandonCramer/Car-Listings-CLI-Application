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
from classes.Employee import Employee

# python lib/debug.py


cust = Customer('Landon', 9995558765, 1)
s1 = Salesman('Matteo', 75_000, datetime.now(), 1)
s2 = Salesman('Conner', 71000, datetime.now(), 2)
st1 = ServiceTech('Matteo', 75_000, datetime.now(), 1)
st2 = ServiceTech('Conner', 71000, datetime.now(), 2)
fleet = helpers.generate_fleet()
car1 = fleet[0]
car2 = fleet[1]
car3 = fleet[2]


def reset_db():
    Car.drop_table()
    Car.create_table()
    Customer.drop_table()
    Customer.create_table()
    Employee.drop_table()
    Employee.create_table()
    for car in fleet:
        car.save()
    s1.save()
    s2.save()
    st1.save()
    st2.save()
    cust1 = Customer('Landon', 9995558765, datetime.now())
    cust2 = Customer('Connor', 8456777765, datetime.now())
    cust1.save()
    cust2.save()
    Appointment.drop_table()
    Appointment.create_table()
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
    td1 = Testdrive('TESTDRIVE', datetime.now(), 1, 1, 1, "The guy drove thru a McDonalds and ordered a 50-pc chicken nugget.")
    td2 = Testdrive('TESTDRIVE', datetime.now(), 3, 3, 3, "Dude crashed into lightpole then tried to bribe me with an expired Chuck E Cheese coupon.")
    td3 = Testdrive('TESTDRIVE', datetime.now(), 6, 3, 3, "The customer kept telling me about her toenail collection.")
    td4 = Testdrive('TESTDRIVE', datetime.now(), 7, 1, 3, "Person did not show up.")
    td5 = Testdrive('TESTDRIVE', datetime.now(), 2, 2, 3, "Testdrive actually went well.")

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