from helpers import (
    welcome,
    create_customer,
    browse_cars
    )

from debug import setup_db

def main():
    setup_db()
    welcome()
    # create_customer()
    browse_cars()
if __name__ == "__main__":
    main()
