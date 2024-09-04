import mysql.connector as connector
connection=connector.connect(user="your_username",password="your_password")
cursor = connection.cursor()
cursor.execute("USE little_lemon")
# confirm the database in use
connection.database

#Obj1 using stored procedure to access the discount of top spender
stored_procedure_query="""
CREATE PROCEDURE TopSpender()

BEGIN

SELECT bookings.BookingID, 
CONCAT(
bookings.GuestFirstname,
' ',
bookings.GuestLastname
) AS CustomerName,
Orders.BillAmount 
FROM Bookings
INNER JOIN
Orders ON bookings.BookingID=Orders.BookingID
ORDER BY BillAmount DESC LIMIT 1;

END

"""
# Execute the query
cursor.execute(stored_procedure_query)
# Call the stored procedure with its name
cursor.callproc("TopSpender")
results = next(cursor.stored_results() )
dataset = results.fetchall()

# Retrieve column names using list comprehension in a 'for' loop 
for column_id in cursor.stored_results():
    columns = [ column[0] for column in column_id.description ]

# Print column names
print(columns)

# Print data 
for data in dataset:
    print(data)

#obj2 procedure to check for information not apearing in the table
stored_procedure_query="""
CREATE PROCEDURE NoArrival()

BEGIN

SELECT bookings.BookingID, 
Orders.BillAmount 
FROM Bookings
LEFT JOIN
Orders ON Bookings.BookingID=Orders.BookingID
WHERE BillAmount IS NULL;

END

"""

# Execute the query 
cursor.execute(stored_procedure_query)
cursor.callproc("NoArrival")

# Retrieve column names using list comprehension in a 'for' loop 
for column_id in cursor.stored_results():
    columns = [ column[0] for column in column_id.description ]

# Print column names
print(columns)

# Print data 
for data in dataset:
    print(data)



# Task 3
# Stored procedure name >> OrderStatus
# Our stored procedure query is
stored_procedure_query="""
CREATE PROCEDURE OrderStatus()

BEGIN

SELECT bookingID, 
CASE
WHEN employeeID IN (1,2,3) THEN "Order Served" 
WHEN employeeID IN (4,5) THEN "Preparing Order" 
ELSE "In Queue" 
END AS Status
FROM Bookings;

END

"""
cursor.execute(stored_procedure_query)
results = next( cursor.stored_results() )
dataset = results.fetchall()
for column_id in cursor.stored_results():
    columns = [ column[0] for column in column_id.description ]
print(columns)
for data in dataset:
    print(data)
