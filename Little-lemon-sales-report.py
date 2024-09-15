#Obj1 Creating a database connection pool
from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector import Error
dbconfig = {
    "database":"little_lemon",
    "user" : "root",
    "password" : ""
}
try:
    pool = MySQLConnectionPool(pool_name = "pool_b",
                           pool_size = 2, #default is 5
                           **dbconfig)
    print("The connection pool is created with a name: ",pool.pool_name)
    print("The pool size is:",pool.pool_size)

except Error as er:
    print("Error code:", er.errno)
    print("Error message:", er.msg)

# getting connections Obj2
connection1 = pool.get_connection()
print("Creating a cursor object.")
cursor = connection1.cursor()

sql_query = "SELECT TableNo, GuestFirstName, GuestLastName, BookingSlot FROM Bookings where TableNo= 8;"

connection2 = pool.get_connection()
print("Creating a cursor object.")
cursor = connection2.cursor()

sql_query = "SELECT TableNo, GuestFirstName, GuestLastName, BookingSlot FROM Bookings where TableNo= 5;"
print("Executing the SQL query.")

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

