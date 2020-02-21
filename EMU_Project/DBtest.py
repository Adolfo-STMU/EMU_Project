import pyodbc
from django.db import connection
cursor = connection.cursor()
cursor.execute("Select * FROM Items")
cursor.fetchall()

cursor.close()