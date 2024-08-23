import mysql.connector as connector
connection=connector.connect(
                             user="root", # use your own
                             password="", # use your own
                            )
cursor = connection.cursor()
# Setting little_lemon for use 
cursor.execute("use little_lemon")

# Confirming
print("Database is use is:", connection.database)
print()
print("The existing tables in the little_lemon database are:")
cursor.execute("SHOW TABLES") 
# Print table names 
for table in cursor: 
    print(table) 



#Obj1
insert_menuitmes="""
INSERT INTO MenuItems (ItemID, Name, Type, Price)
VALUES
(1,'Olives','Starters',5),
(2,'Flatbread','Starters', 5),
(3, 'Minestrone', 'Starters', 8),
(4, 'Tomato bread','Starters', 8),
(5, 'Falafel', 'Starters', 7),
(6, 'Hummus', 'Starters', 5),
(7, 'Greek salad', 'Main Courses', 15),
(8, 'Bean soup', 'Main Courses', 12),
(9, 'Pizza', 'Main Courses', 15),
(10,'Greek yoghurt','Desserts', 7),
(11, 'Ice cream', 'Desserts', 6),
(12, 'Cheesecake', 'Desserts', 4),
(13, 'Athens White wine', 'Drinks', 25),
(14, 'Corfu Red Wine', 'Drinks', 30),
(15, 'Turkish Coffee', 'Drinks', 10),
(16, 'Turkish Coffee', 'Drinks', 10),
(17, 'Kabasa', 'Main Courses', 17);"""

print("Inserting data in MenuItems table.")
# Populate MenuItems table
cursor.execute(insert_menuitmes)
print("Total number of rows in MenuItem table: ", cursor.rowcount)
# Once the query is executed, you commit the change into the database 
connection.commit()



#objective 2 query 3 columns
all_bookings = """SELECT GuestFirstName, GuestLastName, 
TableNo FROM bookings;"""

# Eexecute query 
cursor.execute(all_bookings)
# Fetch all results that satisfy the query 
results = cursor.fetchall()

# Retrieve column names
cols = cursor.column_names

# Print column names and records from results using for loop
print("""Data in the "Bookings" table:""")
print(cols)
for result in results:
    print(result)


#Objective 3 Read all records in the table but return first 3 columns
# Query to retrieve all bookings is: 
all_menus = """SELECT * FROM Menus;"""

# Execute query 
cursor.execute(all_menus)

# Fetch fist 3 records in results
results = cursor.fetchmany(size=3)

# Retrieve column names
cols = cursor.column_names

# Print column names and records from results using for loop
print("""Data in the "Menu" table:""")
print(cols)
for result in results:
    print(result)

#alternatively setting leimit of 3 in query. still on obj3
# Query to retrieve only first three records from the bookings table is:
all_menus = """SELECT * FROM Menus LIMIT 3;"""

# Execute query 
cursor.execute(all_menus)

# Fetch fist 3 records in results
results = cursor.fetchall()   

# Retrieve column names
cols = cursor.column_names

# Print column names and records from results using for loop
print("""Data in the "Menu" table:""")
print(cols)
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
