import mysql.connector as connector
# Establish connection b/w Python and MySQL database via connector API
connection=connector.connect(
                             user="root", # use your own
                             password="", # use your own
                            )

cursor = connection.cursor()
# Set the little_lemon database for use 
cursor.execute("use little_lemon")

# Confirm the database in use
connection.database


#Obj1
# The update query is:
update_bookings="""UPDATE Bookings
SET TableNo=10
WHERE BookingID = 6;"""

# Execute the query to update the table
print("Executing update query")
cursor.execute(update_bookings)

# Commit change 
print("Comitting change to the table")
connection.commit()
print("Record is updated in the table")

# The query to retrieve all bookings is: 
all_bookings = """SELECT * FROM Bookings;"""

# Execute query 
cursor.execute(all_bookings)

# Fetch all results that satisfy the query 
results = cursor.fetchall()

# Retrieve the column names
cols = cursor.column_names

# print column names and the records from results using for loop
print("Data in the 'Bookings' table")
print(cols)
for result in results:  
    print(result)


#OBJ2
# The update query is:
update_bookings="""UPDATE Bookings
SET TableNo=11, EmployeeID=6
WHERE BookingID = 2;"""

# Execute the query to update the table
print("Executing update query")
cursor.execute(update_bookings)

# Commit change 
print("Comitting change to the table")
connection.commit()
print("Record is updated in the table")

slct_statement = """select * from Bookings""""
cursor.execute(slct_statements)
results = cursor.fetchall()
col = cursor.Column_name
print("updated list")
print(col)

#OBJ3 delete operations
# The SQL query is:
delete_query_greek="""DELETE FROM Menus WHERE Cuisine = 'Greek'"""

# Execute the query
print("Executing 'DELETE' query")
cursor.execute(delete_query_greek)

# Commit change 
print("Comitting change to the table")
connection.commit()
print("The table is updated after deletion of the requested records")
# The query to retrieve records from Menus table is: 
all_menus = """SELECT * FROM Menus;"""

# Execute query 
cursor.execute(all_menus)

# Fetch all results that satisfy the query 
results = cursor.fetchall()

# Retrieve column names
cols = cursor.column_names

# Print column names and records from results using for loop
print("""Data in the "Menu" table:""")
print(cols)
for result in results:
    print(result)


for result in results:
  print(result)
