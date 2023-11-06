import re
from classes.__init__ import CURSOR, CONN
import helpers
from datetime import datetime

class Customer:
    def __init__(self, name, phone, join_date, id_ = None):
        self._name = name
        self._phone = phone
        self._join_date = join_date
        self._id = id_
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string.')
        elif not name:
            raise ValueError('Name must be a non-empty string.')
        else:
            self._name = name
    
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, phone):
        if not re.match('^\d{10}$', phone):
            raise ValueError('Phone number must be a valid 10 digit integer.')
        #TODO if phone found in db raise ValueError
        else:
            self._phone = phone

    @property
    def join_date(self):
        return helpers.parse_date(self._join_date)
    @join_date.setter
    def join_date(self, join_date):
        if isinstance(join_date, datetime):
            self._join_date = helpers.parse_date(join_date)
        elif isinstance(join_date, str):
            self._join_date = join_date
        else:
            raise TypeError('Date must be a valid Date object or string.')
    
    @property
    def id_(self):
        return self._id_ 
    @id_.setter
    def id_(self, id_):
        if not (isinstance(id_, int) and id_ != None) or isinstance(id_, bool):
            raise TypeError("ID must be an integer.")
        else:
            self._id_ = id_


# ORM METHODS
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Customer instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT,
                phone TEXT,
                join_date TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS customers
        """
        
        CURSOR.execute(sql)
        CONN.commit()   

    @classmethod
    def get_all(cls):
        """ Return a list containing Customer objects per row in the table """
        sql = """
            SELECT *
            FROM customers
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    def save(self):
        """ Insert a new row with the name, phone, and join date (join date converted to a string, Format YYYY-MM-DD) """
        sql = """
            INSERT INTO customers (name, phone, join_date)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.phone, self.join_date))
        CONN.commit()

    @classmethod
    def create(cls, name, phone, join_date):
        """ Initialize a new Customer instance and save the object to the database """
        customer = Customer(name, phone, join_date)
        customer.save()
        return customer

    def update(self):
        """ Update the table row corresponding to the current Customer instance """
        sql = """
            UPDATE customers
            SET name = ?, phone = ?, join_date = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.phone, self.join_date.strftime('%Y-%m-%d'), self.id))
        CONN.commit()

    def delete(self):
        """ Delete the table row corresponding to the current Customer instance """
        sql = """
            DELETE FROM customers
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id))
        CONN.commit()

#New for Monday

    @classmethod
    def new_from_db(cls, row):
        return cls(
            row[1], #name
            row[2], #phone
            row[3], #joindate
            row[0] #id_
        )
    
  