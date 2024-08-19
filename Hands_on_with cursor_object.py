!pip install mysql-connector-python

# Import the MySQL Connector/Python
import mysql.connector as connector

# Establish connection between Python and MySQL database via connector API
connection=connector.connect(
                             user="root", # use your own
                             password="", # use your own
                            )

# Create cursor object to communicate with entire MySQL database
cursor = connection.cursor()
cursor.execute("CREATE DATABASE little_lemon")
cursor . execute ( "USE little lemon")
cursor . execute ("SHOW TABLES")
# Retrieve tables in a variable 'results'
results = cursor.fetchall()
for table in results:
print (table)

#buffered cursor approach
#Establish connection between Python and MySQL database via connector API
cursor = connection. cursor (buffered = True)
# Set the "little lemon" database for use
Cursor . execute ("""USE little lemon; """)
cursor . execute ("""SELECT * FROM Bookings; """"")
cursor. execute ("""SELECT * FROM Orders; """)

# Create a cursor object with dictionary=True
dic_cursor=connection. cursor (dictionary=True)
dic_cursor. execute ("use little lemon")
dic_cursor . execute ("show tables;")
results = dic_cursor. fetchall ()
for table in results:
  print (table)
 
