from classes.Salesman import Salesman
from classes.Customer import Customer

from helpers import (
    welcome,
    create_customer,
    browse_cars,
    list_cars
    )

from debug import setup_db

def main():
    setup_db()
    welcome()
    create_customer()
    # browse_cars(Customer.get_by('id', 1), Salesman.get_by('id', 1))
if __name__ == "__main__":
    main()