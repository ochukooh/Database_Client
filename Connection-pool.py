#Obj1 Creating a database connection pool
from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector import Error
dbconfig = {
    "database":"little_lemon",
    "user" : "root",
    "password" : ""
}
try:
    pool = MySQLConnectionPool(pool_name = "ll_pool_a",
                           pool_size = 3, #default is 5
                           **dbconfig)
    print("The connection pool is created with a name: ",pool.pool_name)
    print("The pool size is:",pool.pool_size)

except Error as er:
    print("Error code:", er.errno)
    print("Error message:", er.msg)


#Obj2 Connecting to a pool
from mysql.connector.pooling import MySQLConnectionPool

dbconfig = {
    "database":"little_lemon",
    "user" : "root",
    "password" : ""
}

pool = MySQLConnectionPool(pool_name = "ll_pool_a",
                           pool_size = 3, #default is 5
                           **dbconfig)
print("Getting a connection from the pool.")
connection1 = pool.get_connection()
print("Creating a cursor object.")
cursor = connection1.cursor()

sql_query = "SELECT BookingId, GuestFirstName, GuestLastName FROM Bookings;"
print("Executing the SQL query.")
cursor.execute(sql_query)
print("Fetching the query results.")
results = cursor.fetchall()

# Retrieve column names
print("Retrieving the column names.")
cols = cursor.column_names

# Print column names and records in "results" using for loop
print("Printing the results.\n")
print("""Upcoming Bookings are:\n""")
print(cols)
for result in results:
    print(result)



#Obj3 connecting new users to the pool
# Create a connection pool
from mysql.connector.pooling import MySQLConnectionPool
dbconfig = {
    "database":"little_lemon",
    "user" : "root",
    "password" : ""
}

pool = MySQLConnectionPool(pool_name = "ll_pool_a",
                           pool_size = 3, #default is 5
                           **dbconfig)

# List of the guests who want to connect to the database
guests = ["Anna", "Marcos", "Diana", "Joakim", "Hiroki"]

import mysql.connector as connector
for guest in guests:
    try:
        guest_connected = pool.get_connection()
        print("[{}] is connected.\n".format(guest))
    except:
        print("No more connections are available.")
        print("Adding new connection in the pool.")
         # Create a connection
        connection=connector.connect(user="root",password="")
        
          # Add the connection into the pool
        pool.add_connection(cnx=connection)
        print("A new connection is added in the pool.\n")
        
        user_connected = pool.get_connection()
        print("[{}] is connected.\n".format(guest))
  
