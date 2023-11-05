from datetime import datetime
from classes.Appointment import Appointment
from classes.Car import Car
from classes.Customer import Customer
from classes.Employee import Employee
from helpers import rand_car, generate_fleet

# python lib/debug.py

# cust = Customer('Landon', 9995558765, 1)
# emp = Employee('Matteo', 75_000, datetime.now(), 1)

Appointment.drop_table()
Appointment.create_table()
appt1 = Appointment('SALE', datetime.now(), 1, 1, 1, 1)
appt2 = Appointment('TESTDRIVE', datetime.now(), 2, 2, 2, 2)
appt3 = Appointment('SERVICE', datetime.now(), 3, 3, 3, 3)
appt4 = Appointment('SERVICE', datetime.now(), 4, 4, 4, 4)
appt5 = Appointment('TESTDRIVE', datetime.now(), 5, 5, 5, 5)
appt1.save()
appt2.save()
appt3.save()
appt4.save()
appt5.save()

# fleet = generate_fleet()

# fleet = generate_fleet()

# def setup_db():
#     Doctor.drop_table()
#     Patient.drop_table()
#     Appointment.drop_table()

#     Doctor.create_table()
#     Patient.create_table()
#     Appointment.create_table()

#     # Create seed data
#     doctor_1 = Doctor.create("Dr Bob", "123-456-7890", "Allergy and immunology")
#     doctor_2 = Doctor.create("Dr Alice", "123-456-7890", "Anesthesiology")
#     doctor_3 = Doctor.create("Dr Carol", "123-456-7890", "Dermatology")
#     doctor_4 = Doctor.create("Dr Dave", "123-456-7890", "Diagnostic radiology")

#     patient_1 = Patient.create("Alice Smith", "alice@gmail.com", "123-456-7890")
#     patient_2 = Patient.create("Bob Jones", "bob@gmail.com", "123-456-7890")
#     patient_3 = Patient.create("Carol Spellman", "carol@gmail.com", "123-456-7890")
#     patient_4 = Patient.create("Dave Montgomery", "dave@gmail.com", "123-456-7890")
#     patient_5 = Patient.create("Eve Sullivan", "eve@gmail.com", "123-456-7890")

#     Appointment.create("01/01/2021", "01:00PM", "Checkup", doctor_1.id, patient_1.id)
#     Appointment.create("01/02/2021", "02:00PM", "Checkup", doctor_2.id, patient_2.id)
#     Appointment.create("01/03/2021", "03:00PM", "Checkup", doctor_3.id, patient_3.id)
#     Appointment.create("01/04/2021", "04:00PM", "Checkup", doctor_4.id, patient_4.id)
#     Appointment.create("01/05/2021", "05:00PM", "Checkup", doctor_1.id, patient_5.id)

if __name__ == '__main__':
    # setup_db()
    print('Seeded database')
    import ipdb; ipdb.set_trace()