from helpers import (
    welcome,
    create_customer
    )

from debug import setup_db

def main():
    setup_db()
    welcome()
    create_customer()
if __name__ == "__main__":
    main()
