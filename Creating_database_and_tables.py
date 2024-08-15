import mysql.connector as connector
connection=connector.connect(user="your_username",password="your_password")
cursor = connection.cursor()
Create_Database_little_lemon = """CREATE DATABAE little_lemon"""
cursor.execute(Create_Database_little_lemon)

#correction on create database and show database
# If exist, drop the database first 
cursor.execute("drop database little_lemon")

# Create database and checking all that we have!

cursor.execute("CREATE DATABASE little_lemon")
cursor.execute("SHOW DATABASES")
for database in cursor:
    print(database)
# Set little_lemon database for use 
cursor.execute("USE little_lemon")

# Confirm the database in use
connection.database

cursor.execute("SHOW DATABASES")
for database in cursor:
    print(database)

# The SQL query for MenuItems table is: 
create_menuitem_table="""
CREATE TABLE MenuItems (
ItemID INT AUTO_INCREMENT,
Name VARCHAR(200),
Type VARCHAR(100),
Price INT,
PRIMARY KEY (ItemID)
);"""

# Create MenuItems table
cursor.execute(create_menuitem_table)

# Confirm if the table is created
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

# The SQL query for Menu table is:
create_menu_table="""
CREATE TABLE Menus (
MenuID INT,
ItemID INT,
Cuisine VARCHAR(100),
PRIMARY KEY (MenuID,ItemID)
);"""

# Create Menu table
cursor.execute(create_menu_table)

# Confirm if the table is created
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

# The SQL query for Bookings table is:
create_booking_table="""
CREATE TABLE Bookings (
BookingID INT AUTO_INCREMENT,
TableNo INT,
GuestFirstName VARCHAR(100) NOT NULL,
GuestLastName VARCHAR(100) NOT NULL,
BookingSlot TIME NOT NULL,
EmployeeID INT,
PRIMARY KEY (BookingID)
);"""

# Create Bookings table
cursor.execute(create_booking_table)

# Confirm if the table is created
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

# The SQL query for Orders table is:
create_orders_table="""
CREATE TABLE Orders (
OrderID INT,
TableNo INT,
MenuID INT,
BookingID INT,
BillAmount INT,
Quantity INT,
PRIMARY KEY (OrderID,TableNo)
);"""

# Create Orders table
cursor.execute(create_orders_table)

# Confirm if the table is created
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

# Let's close the cursor and the connection
if connection.is_connected():
    cursor.close()
    print("The cursor is closed.")
    connection.close()
    print("MySQL connection is closed.")
else:
    print("Connection is already closed")
