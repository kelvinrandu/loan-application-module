# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from psycopg2 import sql
from database import conn
from psycopg2 import connect, extras



cur = conn.cursor(cursor_factory=extras.RealDictCursor)


class User():

    def __init__(self, first_name, middle_name, last_name, id_number, email, pin , marital_status, number_of_dependants ):

        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name 
        self.id_number = id_number
        self.email = email
        self.pin = pin
        self.marital_status = marital_status
        self.number_of_dependants = number_of_dependants
        
 
    def create_personal_data(self):
       
        try:
            cur.execute(
                """
                INSERT INTO users(first_name, middle_name, last_name, id_number, email, pin,  marital_status, number_of_dependants)
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                (self.first_name, self.middle_name, self.last_name, self.id_number, self.email, self.pin,  self.marital_status, self.number_of_dependants))
            conn.commit() 
         
                       
            return self.id_number
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")
            

    def update_personal_data(self):
       
        try:
            cur.execute(
                """ 
                INSERT INTO banks(bank_name, bank_code, branch_name,  branch_code)VALUES('kcb','09688', 'parklands','0686867');
                """
            )
                # """
                # INSERT INTO users(first_name, middle_name, last_name, id_number, email, pin,  marital_status, number_of_dependants)
                # VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                # (self.first_name, self.middle_name, self.last_name, self.id_number, self.email, self.pin,  self.marital_status, self.number_of_dependants))
         
                       
            return 'personal information updated'
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")

    def delete_personal_data(self):
       
        try:
            cur.execute(
                """ 
                INSERT INTO banks(bank_name, bank_code, branch_name,  branch_code)VALUES('kcb','09688', 'parklands','0686867');
                """
            )
                # """
                # INSERT INTO users(first_name, middle_name, last_name, id_number, email, pin,  marital_status, number_of_dependants)
                # VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                # (self.first_name, self.middle_name, self.last_name, self.id_number, self.email, self.pin,  self.marital_status, self.number_of_dependants))
         
                       
            return 'personal information deleted'
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")


class Adress(User):

    def __init__(self, town):
        self.username = username
        self.email = email
        self.password = password 
        self.role = 0
 

    def create_personal_data(self):
       
        try:
            cur.execute(
                """ 
                INSERT INTO banks(bank_name, bank_code, branch_name,  branch_code)VALUES('kcb','09688', 'parklands','0686867');
                """
            )
                # """
                # INSERT INTO users(first_name, middle_name, last_name, id_number, email, pin,  marital_status, number_of_dependants)
                # VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                # (self.first_name, self.middle_name, self.last_name, self.id_number, self.email, self.pin,  self.marital_status, self.number_of_dependants))
         
                       
            return 'personal information saved'
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")
            

    def update_personal_data(self):
       
        try:
            cur.execute(
                """ 
                INSERT INTO banks(bank_name, bank_code, branch_name,  branch_code)VALUES('kcb','09688', 'parklands','0686867');
                """
            )
                # """
                # INSERT INTO users(first_name, middle_name, last_name, id_number, email, pin,  marital_status, number_of_dependants)
                # VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                # (self.first_name, self.middle_name, self.last_name, self.id_number, self.email, self.pin,  self.marital_status, self.number_of_dependants))
         
                       
            return 'personal information updated'
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")

    def delete_personal_data(self):
       
        try:
            cur.execute(
                """ 
                INSERT INTO banks(bank_name, bank_code, branch_name,  branch_code)VALUES('kcb','09688', 'parklands','0686867');
                """
            )
                # """
                # INSERT INTO users(first_name, middle_name, last_name, id_number, email, pin,  marital_status, number_of_dependants)
                # VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                # (self.first_name, self.middle_name, self.last_name, self.id_number, self.email, self.pin,  self.marital_status, self.number_of_dependants))
         
                       
            return 'personal information deleted'
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")


class Employment(User):

    def __init__(self, *args, **kwargs):
        self.username = username
        self.email = email
        self.password = password 
        self.role = 0
 

    def create_personal_data(self):
       
        try:
            cur.execute(
                """ 
                INSERT INTO banks(bank_name, bank_code, branch_name,  branch_code)VALUES('kcb','09688', 'parklands','0686867');
                """
            )
                # """
                # INSERT INTO users(first_name, middle_name, last_name, id_number, email, pin,  marital_status, number_of_dependants)
                # VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                # (self.first_name, self.middle_name, self.last_name, self.id_number, self.email, self.pin,  self.marital_status, self.number_of_dependants))
         
                       
            return 'personal information saved'
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")
            

    def update_personal_data(self):
       
        try:
            cur.execute(
                """ 
                INSERT INTO banks(bank_name, bank_code, branch_name,  branch_code)VALUES('kcb','09688', 'parklands','0686867');
                """
            )
                # """
                # INSERT INTO users(first_name, middle_name, last_name, id_number, email, pin,  marital_status, number_of_dependants)
                # VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                # (self.first_name, self.middle_name, self.last_name, self.id_number, self.email, self.pin,  self.marital_status, self.number_of_dependants))
         
                       
            return 'personal information updated'
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")

    def delete_personal_data(self):
       
        try:
            cur.execute(
                """ 
                INSERT INTO banks(bank_name, bank_code, branch_name,  branch_code)VALUES('kcb','09688', 'parklands','0686867');
                """
            )
                # """
                # INSERT INTO users(first_name, middle_name, last_name, id_number, email, pin,  marital_status, number_of_dependants)
                # VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                # (self.first_name, self.middle_name, self.last_name, self.id_number, self.email, self.pin,  self.marital_status, self.number_of_dependants))
         
                       
            return 'personal information deleted'
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")


class Bank():

    def __init__(self, *args, **kwargs):
        self.username = username
        self.email = email
        self.password = password 
        self.role = 0
 

    def create_personal_data(self):
       
        try:
            cur.execute(
                """ 
                INSERT INTO banks(bank_name, bank_code, branch_name,  branch_code)VALUES('kcb','09688', 'parklands','0686867');
                """
            )
                # """
                # INSERT INTO users(first_name, middle_name, last_name, id_number, email, pin,  marital_status, number_of_dependants)
                # VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                # (self.first_name, self.middle_name, self.last_name, self.id_number, self.email, self.pin,  self.marital_status, self.number_of_dependants))
         
                       
            return self
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")
            

    def update_personal_data(self):
       
        try:
            cur.execute(
                """ 
                INSERT INTO banks(bank_name, bank_code, branch_name,  branch_code)VALUES('kcb','09688', 'parklands','0686867');
                """
            )
                # """
                # INSERT INTO users(first_name, middle_name, last_name, id_number, email, pin,  marital_status, number_of_dependants)
                # VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                # (self.first_name, self.middle_name, self.last_name, self.id_number, self.email, self.pin,  self.marital_status, self.number_of_dependants))
         
                       
            return 'personal information updated'
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")

    def delete_personal_data(self):
       
        try:
            cur.execute(
                """ 
                INSERT INTO banks(bank_name, bank_code, branch_name,  branch_code)VALUES('kcb','09688', 'parklands','0686867');
                """
            )
                # """
                # INSERT INTO users(first_name, middle_name, last_name, id_number, email, pin,  marital_status, number_of_dependants)
                # VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                # (self.first_name, self.middle_name, self.last_name, self.id_number, self.email, self.pin,  self.marital_status, self.number_of_dependants))
         
                       
            return 'personal information deleted'
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")


class BankDetail(User):

    def __init__(self, *args, **kwargs):
        self.username = username
        self.email = email
        self.password = password 
        self.role = 0
 

    def create_personal_data(self):
       
        try:
            cur.execute(
                """ 
                INSERT INTO banks(bank_name, bank_code, branch_name,  branch_code)VALUES('kcb','09688', 'parklands','0686867');
                """
            )
                # """
                # INSERT INTO users(first_name, middle_name, last_name, id_number, email, pin,  marital_status, number_of_dependants)
                # VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                # (self.first_name, self.middle_name, self.last_name, self.id_number, self.email, self.pin,  self.marital_status, self.number_of_dependants))
         
                       
            return 'personal information saved'
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")
            

    def update_personal_data(self):
       
        try:
            cur.execute(
                """ 
                INSERT INTO banks(bank_name, bank_code, branch_name,  branch_code)VALUES('kcb','09688', 'parklands','0686867');
                """
            )
                # """
                # INSERT INTO users(first_name, middle_name, last_name, id_number, email, pin,  marital_status, number_of_dependants)
                # VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                # (self.first_name, self.middle_name, self.last_name, self.id_number, self.email, self.pin,  self.marital_status, self.number_of_dependants))
         
                       
            return 'personal information updated'
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")

    def delete_personal_data(self):
       
        try:
            cur.execute(
                """ 
                INSERT INTO banks(bank_name, bank_code, branch_name,  branch_code)VALUES('kcb','09688', 'parklands','0686867');
                """
            )
                # """
                # INSERT INTO users(first_name, middle_name, last_name, id_number, email, pin,  marital_status, number_of_dependants)
                # VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                # (self.first_name, self.middle_name, self.last_name, self.id_number, self.email, self.pin,  self.marital_status, self.number_of_dependants))
         
                       
            return 'personal information deleted'
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")


class LoanInOtherBank(User):

    def __init__(self, *args, **kwargs):
        self.username = username
        self.email = email
        self.password = password 
        self.role = 0
 

    def create_personal_data(self):
       
        try:
            cur.execute(
                """ 
                INSERT INTO banks(bank_name, bank_code, branch_name,  branch_code)VALUES('kcb','09688', 'parklands','0686867');
                """
            )
                # """
                # INSERT INTO users(first_name, middle_name, last_name, id_number, email, pin,  marital_status, number_of_dependants)
                # VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                # (self.first_name, self.middle_name, self.last_name, self.id_number, self.email, self.pin,  self.marital_status, self.number_of_dependants))
         
                       
            return 'personal information saved'
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")
            

    def update_personal_data(self):
       
        try:
            cur.execute(
                """ 
                INSERT INTO banks(bank_name, bank_code, branch_name,  branch_code)VALUES('kcb','09688', 'parklands','0686867');
                """
            )
                # """
                # INSERT INTO users(first_name, middle_name, last_name, id_number, email, pin,  marital_status, number_of_dependants)
                # VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                # (self.first_name, self.middle_name, self.last_name, self.id_number, self.email, self.pin,  self.marital_status, self.number_of_dependants))
         
                       
            return 'personal information updated'
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")

    def delete_personal_data(self):
       
        try:
            cur.execute(
                """ 
                INSERT INTO banks(bank_name, bank_code, branch_name,  branch_code)VALUES('kcb','09688', 'parklands','0686867');
                """
            )
                # """
                # INSERT INTO users(first_name, middle_name, last_name, id_number, email, pin,  marital_status, number_of_dependants)
                # VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                # (self.first_name, self.middle_name, self.last_name, self.id_number, self.email, self.pin,  self.marital_status, self.number_of_dependants))
         
                       
            return 'personal information deleted'
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")

class LoanParticular(User):

    def __init__(self, *args, **kwargs):
        self.username = username
        self.email = email
        self.password = password 
        self.role = 0
 

    def create_personal_data(self):
       
        try:
            cur.execute(
                """ 
                INSERT INTO banks(bank_name, bank_code, branch_name,  branch_code)VALUES('kcb','09688', 'parklands','0686867');
                """
            )
                # """
                # INSERT INTO users(first_name, middle_name, last_name, id_number, email, pin,  marital_status, number_of_dependants)
                # VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                # (self.first_name, self.middle_name, self.last_name, self.id_number, self.email, self.pin,  self.marital_status, self.number_of_dependants))
         
                       
            return 'personal information saved'
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")
            

    def update_personal_data(self):
       
        try:
            cur.execute(
                """ 
                INSERT INTO banks(bank_name, bank_code, branch_name,  branch_code)VALUES('kcb','09688', 'parklands','0686867');
                """
            )
                # """
                # INSERT INTO users(first_name, middle_name, last_name, id_number, email, pin,  marital_status, number_of_dependants)
                # VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                # (self.first_name, self.middle_name, self.last_name, self.id_number, self.email, self.pin,  self.marital_status, self.number_of_dependants))
         
                       
            return 'personal information updated'
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")

    def delete_personal_data(self):
       
        try:
            cur.execute(
                """ 
                INSERT INTO banks(bank_name, bank_code, branch_name,  branch_code)VALUES('kcb','09688', 'parklands','0686867');
                """
            )
                # """
                # INSERT INTO users(first_name, middle_name, last_name, id_number, email, pin,  marital_status, number_of_dependants)
                # VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                # (self.first_name, self.middle_name, self.last_name, self.id_number, self.email, self.pin,  self.marital_status, self.number_of_dependants))
         
                       
            return 'personal information deleted'
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")



# class User():

#     def __init__(self, *args, **kwargs):
#         self.username = username
#         self.email = email
#         self.password = password 
#         self.role = 0
 
#     def create_personal_data(self):
       
#         try:
#             cur.execute(
#                 """
#                 INSERT INTO users(username, email, password,role)
#                 VALUES(%s,%s,%s,%s)""",
#                 (self.username, self.email, self.password, self.role))
         
                       
#             return 'personal information saved'
        

#         except Exception as e:
#             print(e)
#             return ("ran into trouble registering you")