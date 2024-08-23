import mysql.connector as connector
# Establish connection b/w Python and MySQL database via connector API
connection=connector.connect(
                             user="root", # use your own
                             password="", # use your own
                            )
cursor = connection.cursor()
cursor.execute("use little_lemon")
# Confirm the database in use
connection.database


#OBJ1 filtering task
# The SQL query is:
filtering_and_sorting = """SELECT TableNo, 
GuestFirstName, GuestLastName, EmployeeID  
FROM Bookings 
WHERE TableNo= 12;"""

# Execute query
cursor.execute(filtering_and_sorting)

# Fetch records 
results = cursor.fetchall()

# Retrieve column names
columns = cursor.column_names

# Print column names
print(columns)

# Print query results
for result in results:
    print(result)


#OBJ 2 
filtering_and_sorting = """SELECT BookingID, BillAmount
FROM
Orders ORDER BY BillAmount DESC;"""

# Execute query
cursor.execute(filtering_and_sorting)

# Fetch records 
results = cursor.fetchmany(size=2)#fetchall()

# Retrieve column names
columns = cursor.column_names

# Print column names
print(columns)

# Print query results
for result in results:
    print(result)
#alternative option
# Resetting cursor
cursor.fetchall()

# Task 2 Option 2

# The SQL query is:
filtering_and_sorting = """SELECT BookingID, BillAmount
FROM
Orders ORDER BY BillAmount DESC LIMIT 2;"""

# Execute query
cursor.execute(filtering_and_sorting)

# Fetch records 
results = cursor.fetchall()

# Retrieve column names
columns = cursor.column_names

# Print column names
print(columns)

# Print query results
for result in results:
    print(result)


#OBJ 3
# Task 3

# The SQL query is:
filtering_and_sorting = """SELECT * 
FROM MenuItems 
WHERE (Type = 'Starters' OR Type = 'Desserts')
ORDER BY Price ASC;"""

# Execute query
cursor.execute(filtering_and_sorting)

# Fetch records 
results = cursor.fetchall()

# Retrieve column names
columns = cursor.column_names

# Print column names
print(columns)

# Print query results
for result in results:
    print(result)

# Let's close the cursor and the connection
if connection.is_connected():
    cursor.close()
    print("The cursor is closed.")
    connection.close()
    print("MySQL connection is closed.")
else:
    print("Connection is already closed")
