from classes.__init__ import CURSOR, CONN
from classes.Appointment import Appointment

class Sale(Appointment):
    all = {}

    def __init__(self, type_, date, customer_id, employee_id, car_id, id=None, balance=50_000, status=True):
        self.balance = balance
        self.status = status
    
#     # *********************
#     # CREATE / DROP TABLES
#     # *********************

#     @classmethod
#     def create_table(cls):
#         sql = """
#             CREATE TABLE IF NOT EXISTS sales (
#             id INTEGER PRIMARY KEY,
#             appt_id INTEGER,
#             balance INTEGER,
#             status TEXT)
#         """
#         CURSOR.execute(sql)
#         CONN.commit()

#     @classmethod
#     def drop_table(cls):
#         sql = """
#             DROP TABLE IF EXISTS sales
#         """
#         CURSOR.execute(sql)
#         CONN.commit()

#     # ***********
#     # PROPERTIES
#     # ***********

#     @property
#     def balance(self):
#         return self._balance
#     @balance.setter
#     def balance(self, balance):
#         if not isinstance(balance, int):
#             raise TypeError("Balance must be an integer.")
#         elif balance <= 0:
#             raise ValueError("Balance must be greater than 0.")
#         else:
#             self._balance = balance

#     @property
#     def status(self):
#         return "Active" if self._status else "Closed"
#     @status.setter
#     def status(self, status):
#         if not isinstance(status, bool):
#             raise TypeError("Active state must be a boolean.")
#         else:
#             self._status = "Active" if status else "Closed"
        
#     @property
#     def id(self):
#         return self._id
#     @id.setter
#     def id(self, id):
#         if not id:
#             self._id = None
#         elif not isinstance(id, int) or isinstance(id, bool):
#             raise TypeError("ID must be an integer.")
#         else:
#             self._id = id

#     # *************
#     # CLASSMETHODS
#     # *************

#     # ************
#     # ORM METHODS
#     # ************

#     def save(self):
#         sql = """
#             INSERT INTO sales (balance, status)
#             VALUES (?, ?)
#         """
#         CURSOR.execute(sql, (self.balance, self.status))
#         CONN.commit()

#         self.id = CURSOR.lastrowid
#         type(self).all[self.id] = self

#     @classmethod
#     def create(cls, balance, status):
#         appointment = cls(balance, status)
#         appointment.save()

#         cls.all[appointment.id] = appointment

#         return appointment
    
#     def update(self, id):
#         sql = """
#             UPDATE appointments
#             SET balance = ?, status = ?
#             WHERE id = ?
#         """
#         CURSOR.execute(sql, (self.balance, self.status, id))
#         CONN.commit()