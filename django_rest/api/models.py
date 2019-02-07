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
         
                       
            return (" personal details added succesfuly")
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")

    @staticmethod
    def find_by_id(id_number):

        cur.execute(
            """
            SELECT * FROM users WHERE id_number='{}' """.format(id_number))
        conn.commit() 
        rows = cur.fetchone()
        if rows :
            return rows['first_name']
               
        return 0

    @staticmethod
    def find_user_id(id_number):

        cur.execute(
            """
            SELECT * FROM users WHERE id_number='{}' """.format(id_number))
        conn.commit() 
        rows = cur.fetchone()
        if rows :
            return rows['id']
               
        return 0
            

    def update_personal_data(self, user_id):
      
        try:
            cur.execute(
                """
                UPDATE users  SET first_name='{}', middle_name='{}', last_name='{}', id_number='{}', email='{}', pin='{}', marital_status='{}', number_of_dependants='{}'
                WHERE id='{}' """.format(self.first_name, self.middle_name, self.last_name, self.id_number, self.email, self.pin,  self.marital_status, self.number_of_dependants, user_id))
            conn.commit() 
                                
            return 'personal information updated'
        

        except Exception as e:
            print(e)
            return ("ran into trouble updating you")

    @staticmethod
    def delete_personal_data(user_id):
       
        try:
            cur.execute("""DELETE FROM users WHERE id='{}' """.format(user_id))
            conn.commit() 
                    
            return 'personal information deleted'
        

        except Exception as e:
            print(e)
            return ("ran into trouble deleting you")


class Address(User):

    def __init__(self, user_id, town, estate, street_number, status, stayed_from):
        self.user_id = user_id 
        self.town = town
        self.estate = estate
        self.street_number= street_number 
        self.status = status
        self.stayed_from = stayed_from
      
 

    def create_address_data(self):
       
        try:
            cur.execute(   
                """
                INSERT INTO address(user_id, town, estate, street_number, status, stayed_from)
                VALUES(%s,%s,%s,%s,%s,%s)""",
                (self.user_id, self.town, self.estate, self.street_number, self.status, self.stayed_from))
            conn.commit()
         
                       
            return 'address information saved'
        

        except Exception as e:
            print(e)
            return ("ran into trouble registering you")
            

    @staticmethod
    def find_address_id(user_id):

        cur.execute(
            """
            SELECT * FROM address WHERE user_id='{}' """.format(user_id))
        conn.commit() 
        rows = cur.fetchone()
        if rows :
            return rows['estate']
               
        return 0


    def update_address_data(self, address_id):
       
        try:
            cur.execute(
                """
                UPDATE address  SET user_id='{}', town='{}', estate='{}', street_number='{}', status='{}', stayed_from='{}'
                WHERE id='{}' """.format(self.user_id, self.town, self.estate, self.street_number, self.status, self.stayed_from, address_id))
            conn.commit() 
               
            return 'address information updated'
        

        except Exception as e:
            print(e)
            return ("ran into trouble updating you")


    @staticmethod
    def delete_address_data(address_id):
       
       
        try:
            cur.execute("""DELETE FROM address WHERE id='{}' """.format(address_id))
            conn.commit() 
                    
            return 'personal information deleted'
        

        except Exception as e:
            print(e)
            return ("ran into trouble deleting you")


class Employment(User):

    def __init__(self, *args, **kwargs):
        pass
 

    def create_personal_data(self):      
        pass
            

    def update_personal_data(self):
       pass

    def delete_personal_data(self):
       pass


class Bank():

    def __init__(self, *args, **kwargs):
        pass
 

    def create_personal_data(self):
        pass
            

    def update_personal_data(self):
        pass
        


    def delete_personal_data(self):
       pass


class BankDetail(User):

    def __init__(self, *args, **kwargs):
        pass
 

    def create_personal_data(self):
       pass
            

    def update_personal_data(self):
        pass

    def delete_personal_data(self):
       pass


class LoanInOtherBank(User):

    def __init__(self, *args, **kwargs):
        pass
 

    def create_personal_data(self):
       pass
            

    def update_personal_data(self):
       pass

    def delete_personal_data(self):
       pass

class LoanParticular(User):

    def __init__(self, *args, **kwargs):
        pass
 

    def create_personal_data(self):
       pass
            

    def update_personal_data(self):
        pass

    def delete_personal_data(self):
       pass

