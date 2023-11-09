# Honest Aang's New and Used Cars

![Alt text](dall__e_2023-11-08_19.28.00_-_an_image_of_a_young_monk_with_a_blue_arrow_tattoo_on_his_head__dressed_in_orange_and_yellow_robes__standing_beside_a_futuristic_car_in_a_setting_remin_720.png)

# Overview:
Are you tired of riding around on Appa or floating on a piece of driftwood? Do you dream of zooming through the four nations with the wind in your hair and a trusty steed at your command? Well, look no further! Honest Aang's New and Used Cars is here to fulfill your dreams. It's not just a Python-based CLI application that caters to car enthusiasts from all walks of life; it's also backed by an SQL database that stores a wide array of car listings and related information.
## SQL Database for Comprehensive Storage:
Our SQL database is the powerhouse behind Honest Aang's New and Used Cars, serving as the centralized repository for various types of data, including cars, customers, employees, and appointments.
#### Cars:
The database stores comprehensive information about each car listing. Details such as the car's make, model, price, and condition are meticulously organized, making it easy for users to find the perfect vehicle.
#### Customers:
For individuals interested in purchasing a car, the database holds valuable data on customers. This includes customer names, phone numbers, and the date they joined the dealership, enabling seamless interactions and personalized service.
#### Employees:
To ensure the dealership runs smoothly, the database contains employee records. This information encompasses employee names, salaries, job titles, and hire dates, allowing for effective management and coordination.
#### Appointments:
Appointments play a pivotal role in the car buying process. The database maintains a record of appointments, storing essential details such as the appointment type, date, associated customer, employee, car, and additional appointment-specific attributes.
#### Efficient Data Storage and Retrieval:
The structured design of our SQL database ensures efficient data storage and retrieval. Users can effortlessly browse, search, and filter cars and access customer information, employee details, and appointments. This integrated approach streamlines the car-buying process, making it both comprehensive and user-friendly.
#### User-Friendly CLI Integration:
Our Python-based CLI application seamlessly interacts with the SQL database, enabling users to access and manage cars, customers, employees, and appointments. Whether you're searching for the perfect car, coordinating with customers, managing your employee roster, or scheduling appointments, our application and database work in harmony to provide a seamless experience.


# Installation

* Ensure you have Python 3.8 installed on your system.
* Fork this repository into your local files and clone it using Git.
* Navigate to the cloned repository in your terminal.
* Run `pipenv install` to create a virtual environment and install the required Python packages.
* Activate the virtual environment with `pipenv shell`.
* You're ready to roll! Explore a variety of cars by running `python lib/cli.py` from your command line.
#### Dependencies
Honest Aang's New and Used Cars relies on several external Python packages to enhance its functionality and provide a seamless user experience. These packages can be easily installed using pip, Python's package manager, to set up the application and its dependencies. You can install the required packages with the following commands:
* ipdb: A powerful debugger for Python applications, providing an interactive and feature-rich debugging experience. Install it with `pip install ipdb`.
* Faker: A Python library for generating fake data, including names, addresses, and other information, useful for testing and populating the database with sample data. Install it with `pip install Faker`.
* Rich: A library for adding beautiful and sophisticated formatting to your command-line interface (CLI) application, making your interactions with Honest Aang's New and Used Cars more visually appealing and informative. Install it with `pip install rich`.

These dependencies are essential for a smooth and feature-rich experience when using Honest Aang's New and Used Cars.
# Usage


# ADD GIF

## Appointment Class
The Appointment class, defined in the Appointment.py file, is a versatile component of the Honest Aangs New and Used Cars application, facilitating the management of appointments between customers, employees, and cars. It serves as the base class for various types of appointments, including sales, services, and test drives, each providing distinct functionality.

#### Attributes
* type_: The type of appointment, categorized as SALE, SERVICE, or TESTDRIVE.
* date: The date and time of the appointment, represented as a string in the format MM/DD/YYYY.
* customer_id: The unique identifier of the customer associated with the appointment.
* employee_id: The unique identifier of the employee handling the appointment.
* car_id: The unique identifier of the car involved in the appointment.
* id_: A unique identifier for each appointment.
#### Methods
* Create / Drop Tables
    * create_table(): Creates a database table for storing appointments, including columns for type, date, customer ID, employee ID, car ID, balance, reason for visit, estimate, notes, and status.
    * drop_table(): Drops the appointment database table.
* Properties
    * Custom setters and getters for properties like type_, date, customer_id, and others ensure data integrity and validity.
* Create, Read, Update, Delete (CRUD) Operations
    * save(): Inserts a new appointment into the database, distinguishing between sale, service, and test drive appointments, and maintaining an appointments dictionary for easy access.
    * create(cls, *args): A flexible method that creates an appointment based on its subclass (Sale, Service, or Testdrive) and saves it to the database.
    * instance_from_db(row): Constructs an appointment instance from a database row and updates the appointments dictionary accordingly.
    * get_by(param, value): Retrieves appointments based on various parameters, distinguishing between appointment types.
    * update(): Updates appointment details, such as balance, reason for visit, estimate, notes, or status.
    * delete(): Removes an appointment from the database and the appointments dictionary.

The Appointment class functions as a foundation for managing appointments in the Honest Aangs New and Used Cars application. It enables users to schedule and track various appointment types, helping to maintain efficient customer and vehicle management.

## Car Class
The Car class, defined in the Car.py file, represents the fundamental structure for vehicles in the Honest Aangs New and Used Cars application. It encapsulates the essential attributes and behaviors of cars, allowing for effective management of cars in the system.

#### Attributes
* vehicle_type: The type of the vehicle (e.g., COUPE, SEDAN, TRUCK).
* new: Indicates whether the car is new or used.
* make: The car's make, such as the manufacturer.
* model: The car's model name.
* miles: The mileage of the car.
* fuel_type: The type of fuel the car uses (e.g., GAS, DIESEL, ELECTRIC).
* color: The color of the car.
* transmission: The transmission type (Automatic or Manual).
* year: The manufacturing year of the car.
* price: The price of the car.
* owned: Indicates if the car is currently owned.
* id_: A unique identifier for each car.
#### Methods
* Create / Drop Tables
    * create_table(): Creates a database table to store car information.
    * drop_table(): Drops the car database table.
* Properties
    * Properties like vehicle_type, new, make, model, and others have custom getters and setters to ensure data integrity.
* Create, Read, Update, Delete (CRUD) Operations
    * save(): Inserts a new car into the database.
    * update(): Updates the car's information in the database.
    * delete(): Removes the car from the database.
    * get_by(param, value): Retrieves cars based on various parameters.
    * instance_from_db(row): Constructs a Car instance from a database row.
* Class Methods
    * Methods like cars_w_appts(), test_driven_cars(), and others return lists of cars with specific characteristics, such as cars with associated appointments or test-driven cars.
* Instance Methods
    * appts(): Returns a list of appointments associated with the car.
    * services(): Filters and returns service appointments related to the car.
    * open_tickets(): Filters and returns active service appointments for the car.
    * service_history(): Filters and returns closed service appointments for the car.
    * test_drives(): Filters and returns test drive appointments for the car.
    * employees(): Retrieves a list of employees associated with the car's appointments.
    * customers(): Retrieves a list of customers who have had appointments related to the car.
    * list_details(): Displays essential car details, including make, model, color, mileage, condition, and price.
    * full_details(): Displays comprehensive car details, including vehicle type, new or used status, make, model, year, mileage, fuel type, color, transmission, and price.

The Car class forms the backbone of the Honest Aangs New and Used Cars application, enabling users to manage and explore a wide range of vehicles efficiently.


## Employee Class
The Employee class, defined in the Employee.py file, plays a crucial role in the Honest Aangs New and Used Cars application, responsible for managing employees, their details, and their activities within the dealership. This class serves as a base for different employee roles such as Salesmen, Service Techs, and Managers.

#### Attributes
* name: The name of the employee.
* salary: The employee's salary, which must be within the range of $50,000 to $250,000.
* hire_date: The date when the employee was hired, represented as a datetime object.
* id_: A unique identifier for each employee.
* job_title: The job title of the employee, based on the subclass.
#### Methods
* Create / Drop Tables
    * create_table(): Creates a database table to store the attributes of Employee instances, including name, salary, job title, and hire date.
    * drop_table(): Drops the employee database table.
* Properties
    * Custom setters and getters for properties like name, salary, hire_date, and id_ ensure data validity.
* Create, Read, Update, Delete (CRUD) Operations
    * save(): Inserts a new employee into the database with their name, salary, job title, and hire date.
    * create(cls, der_cls, name, salary, hire_date): Initializes and saves a new employee object to the database based on the employee's subclass (Salesman, ServiceTech, or Manager).
    * instance_from_db(cls, row): Constructs an employee instance from a database row.
    * get_by(cls, param='all', value=''): Retrieves employees based on various parameters, distinguishing between employee roles.
    * update(): Updates employee details, such as name, salary, job title, and hire date.
    * delete(): Removes an employee from the database.
* Class Methods
    * employee_of_the_month(cls, role): Identifies the employee of the month within a specific role based on their performance in appointments.
* Instance Methods
    * appts(self): Retrieves appointments associated with the employee.
    * testdrives(self): Retrieves test drive appointments handled by the employee (available to Salesmen and Managers only).
     *services(self): Retrieves service appointments handled by the employee (available to Service Techs and Managers only).
    * sales(self): Retrieves sales appointments handled by the employee (available to Salesmen and Managers only).
    * customers(self): Retrieves the customers associated with the employee's appointments.
    * cars(self): Retrieves the cars associated with the employee's appointments.

The Employee class acts as the foundation for employee management, facilitating the organization of staff, tracking their performance, and their involvement in various types of appointments within the Honest Aangs New and Used Cars application. This class also ensures the integrity of employee data, making it a central component of the application.


## Customer Class
The Customer class, defined in the customer.py file, is a fundamental part of the Honest Aangs New and Used Cars application, responsible for managing customer information and their interactions with the dealership. Customers can be associated with appointments, cars, and employees.
#### Attributes
* name: The name of the customer.
* phone: The customer's phone number, a 10-digit integer.
* join_date: The date when the customer joined the dealership, represented as a datetime object.
* id_: A unique identifier for each customer.
#### Methods
* Create / Drop Tables
    * create_table(): Creates a database table to store the attributes of Customer instances, including name, phone, and join date.
    * drop_table(): Drops the customer database table.
* Properties
    * Custom setters and getters for properties like name, phone, join_date, and id_ ensure data validity.
* Create, Read, Update, Delete (CRUD) Operations
    * save(): Inserts a new customer into the database with their name, phone, and join date.
    * create(cls, name, phone, join_date): Initializes and saves a new Customer instance to the database.
    * instance_from_db(cls, row): Constructs a customer instance from a database row.
    * get_by(cls, param='all', value=None): Retrieves customers based on various parameters.
    * update(): Updates customer details, such as name, phone, and join date.
    * delete(): Removes a customer from the database.
* Instance Methods
    * appts(self): Retrieves appointments associated with the customer.
    * cars_test_driven(self): Retrieves cars test-driven by the customer.
    *cars_serviced(self): Retrieves cars serviced for the customer (only closed service appointments).
    * cars_in_shop(self): Retrieves cars currently in service for the customer (only active service appointments).
    * employees(self): Retrieves employees associated with the customer's appointments.
* Class Methods
    * phone_numbers(cls): Retrieves phone numbers of all customers in the database.

The Customer class facilitates the management of customer data and their interactions within the Honest Aangs New and Used Cars application. It ensures the accuracy of customer information, making it a vital component for tracking customer history and building strong customer relationships within the dealership.




## Contributing
- <b>Conner Adams
- Joseph Lee
- Landon Cramer
</b>

## License
The MIT License(MIT)

Permission is herby granted, free of charge, to any person obtaining a copy of this software and associated document files ("Honest Aang's New and Used Cars"). You are free to bend it, twist it, or even throw it into the spirit portal (though we don't recommend that). Remember, with great bending power comes great responsibility. Enjoy exploring our world of cars!