from classes.Salesman import Salesman
from classes.Customer import Customer
from classes.Car import Car

from helpers import (
    welcome,
    create_customer,
    browse_cars,
    list_cars,
    show_car
    )

from debug import setup_db

def main():
    setup_db()
    welcome()
    # create_customer()
    # show_car(Customer.get_by('id', 1), Salesman.get_by('id', 1), Car.get_by('id', 50))
    browse_cars(Customer.get_by('id', 1), Salesman.get_by('id', 1))
if __name__ == "__main__":
    main()