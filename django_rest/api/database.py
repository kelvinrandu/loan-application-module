import os
from psycopg2 import connect, extras

url ="postgresql://localhost/telco?user=postgres&password=1234"
conn = connect(url)
cur = conn.cursor()
print('connected to test database...')
print(conn)