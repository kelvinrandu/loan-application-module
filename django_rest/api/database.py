import os
from psycopg2 import connect, extras

url ="postgresql://localhost:5432/django?user=postgres&password=1234"
url2 ="postgres://postgres:1234@localhost:5432/rest"
conn = connect(url2)
cur = conn.cursor()
print('connected to test database...')



def create_tables():

        
    try:

        # drop tables if they exist

        cur.execute("DROP TABLE IF EXISTS users, address, employment, business, banks, bank_details, loans_in_other_banks, loan_particulars CASCADE;")

        # define sql queries

        users = """
                CREATE TABLE IF NOT EXISTS users(id serial PRIMARY KEY,
                first_name varchar,
                middle_name varchar,
                last_name varchar,
                id_number int,
                email varchar,
                pin int,
                marital_status varchar,
                number_of_dependants int,
                created_at timestamp default now());
                """

        address = """
                CREATE TABLE IF NOT EXISTS address(id serial PRIMARY KEY,
                user_id integer   not null references users (id) on delete cascade,
                town varchar,
                estate varchar,
                street_number varchar,
                status varchar,
                stayed_from timestamp,
                created_at timestamp default now());
                """

        employment = """
                CREATE TABLE IF NOT EXISTS employment(id serial PRIMARY KEY,
                user_id integer   not null references users (id) on delete cascade,
                employer varchar,
                address varchar,
                staff_number int, 
                physical_address varchar,               
                telephone varchar,                              
                designation varchar,
                employment_terms varchar,
                created_at timestamp default now());
                """

        business = """
                CREATE TABLE IF NOT EXISTS  business(id serial PRIMARY KEY,
                user_id integer   not null references users (id) on delete cascade,
                type_of_business varchar,
                years_of_operation int,
                business_income int,
                rental_income int,
                other_income int,
                created_at timestamp default now());
                """


        banks = """
                CREATE TABLE IF NOT EXISTS banks(id serial PRIMARY KEY,
                bank_name varchar,
                bank_code int,
                branch_name varchar,
                branch_code int,
                created_at timestamp default now());
                """


        bank_details = """
                CREATE TABLE IF NOT EXISTS bank_details(id serial PRIMARY KEY,
                user_id integer   not null references users (id) on delete cascade,
                bank_id integer   not null references banks (id) on delete cascade,
                account_name varchar,
                account_number int,
                created_at timestamp default now());
                """


        loans_in_other_banks = """
                CREATE TABLE IF NOT EXISTS loans_in_other_banks(id serial PRIMARY KEY,
                user_id integer   not null references users (id) on delete cascade,
                bank_id integer   not null references banks (id) on delete cascade,
                date_granted timestamp,
                amount int,
                repayment_period int,
                outstandin_balance int,
                created_at timestamp default now());
 
               """


        loan_particulars  = """
                CREATE TABLE IF NOT EXISTS loan_particulars (id serial PRIMARY KEY,
                user_id integer   not null references users (id) on delete cascade,
                loan_type varchar,
                purpose varchar,
                amount int,
                created_at timestamp default now());
                """


        dummy_personal = """ 
                    INSERT INTO users(first_name, middle_name, last_name, id_number, email, pin , marital_status, number_of_dependants)VALUES('twenty','one', 'savage','0686867','savage@gmail.com','12345','single','3');
                    """
        dummy_banks = """ 
                    INSERT INTO banks(bank_name, bank_code, branch_name,  branch_code)VALUES('barclays','09688', 'parklands','0686867');
                    """


#  execute the sql queries

        cur.execute(users)   
        cur.execute(address)   
        cur.execute(employment)
        cur.execute( business)
        cur.execute(banks)
        cur.execute( bank_details)
        cur.execute(loans_in_other_banks)
        cur.execute(loan_particulars)
        cur.execute(loan_particulars)
        cur.execute(dummy_banks)
        cur.execute(dummy_personal)
        conn.commit()
        # conn.close()
        
        
    except Exception as ex:
        print('error in migration', ex)


