# Import MySQL Connector/Python 
import mysql.connector as connector

connection=connector.connect(user="your_username",password="your_password")
cursor = connection.cursor()
cursor.execute("CREATE DATABASE little_lemon_db") 
cursor.execute("USE little_lemon_db")

#MenuItems table
create_menuitem_table = """CREATE TABLE MenuItems (
ItemID INT AUTO_INCREMENT,
Name VARCHAR(200),
Type VARCHAR(100),
Price INT,
PRIMARY KEY (ItemID)
);"""

create_menu_table = """CREATE TABLE Menus (
MenuID INT,
ItemID INT,
Cuisine VARCHAR(100),
PRIMARY KEY (MenuID,ItemID)
);"""

Create_booking_table = """CREATE TABLE Bookings (
BookingID INT AUTO_INCREMENT,
TableNo INT,
GuestFirstName VARCHAR(100) NOT NULL,
GuestLastName VARCHAR(100) NOT NULL,
BookingSlot TIME NOT NULL,
EmployeeID INT,
PRIMARY KEY (BookingID)
);"""

create_orders_table = """CREATE TABLE Orders (
OrderID INT,
TableNo INT,
MenuID INT,
BookingID INT,
BillAmount INT,
Quantity INT,
PRIMARY KEY (OrderID,TableNo)
);"""

create_employees_table = """CREATE TABLE Employees (
EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
Name VARCHAR (255),
Role VARCHAR (100),
Address VARCHAR (255),
Contact_Number INT,
Email VARCHAR (255),
Annual_Salary VARCHAR (100)
);"""

# Create MenuItems table
cursor.execute(create_menuitem_table)

# Create Menu table
cursor.execute(create_menu_table)

# Create Bookings table
cursor.execute(create_booking_table)

# Create Orders table
cursor.execute(create_orders_table)

# Create Employees table
cursor.execute(create_employees_table)


#*******************************************************#
# Insert query to populate "MenuItems" table:
#*******************************************************#
insert_menuitems="""
INSERT INTO MenuItems (ItemID, Name, Type, Price)
VALUES
(1, 'Olives','Starters',5),
(2, 'Flatbread','Starters', 5),
(3, 'Minestrone', 'Starters', 8),
(4, 'Tomato bread','Starters', 8),
(5, 'Falafel', 'Starters', 7),
(6, 'Hummus', 'Starters', 5),
(7, 'Greek salad', 'Main Courses', 15),
(8, 'Bean soup', 'Main Courses', 12),
(9, 'Pizza', 'Main Courses', 15),
(10, 'Greek yoghurt','Desserts', 7),
(11, 'Ice cream', 'Desserts', 6),
(12, 'Cheesecake', 'Desserts', 4),
(13, 'Athens White wine', 'Drinks', 25),
(14, 'Corfu Red Wine', 'Drinks', 30),
(15, 'Turkish Coffee', 'Drinks', 10),
(16, 'Turkish Coffee', 'Drinks', 10),
(17, 'Kabasa', 'Main Courses', 17);"""

#*******************************************************#
# Insert query to populate "Menu" table:
#*******************************************************#
insert_menu="""
INSERT INTO Menus (MenuID,ItemID,Cuisine)
VALUES
(1, 1, 'Greek'),
(1, 7, 'Greek'),
(1, 10, 'Greek'),
(1, 13, 'Greek'),
(2, 3, 'Italian'),
(2, 9, 'Italian'),
(2, 12, 'Italian'),
(2, 15, 'Italian'),
(3, 5, 'Turkish'),
(3, 17, 'Turkish'),
(3, 11, 'Turkish'),
(3, 16, 'Turkish');"""

#*******************************************************#
# Insert query to populate "Bookings" table:
#*******************************************************#
insert_bookings="""
INSERT INTO Bookings (BookingID, TableNo, GuestFirstName, 
GuestLastName, BookingSlot, EmployeeID)
VALUES
(1, 12, 'Anna','Iversen','19:00:00',1),
(2, 12, 'Joakim', 'Iversen', '19:00:00', 1),
(3, 19, 'Vanessa', 'McCarthy', '15:00:00', 3),
(4, 15, 'Marcos', 'Romero', '17:30:00', 4),
(5, 5, 'Hiroki', 'Yamane', '18:30:00', 2),
(6, 8, 'Diana', 'Pinto', '20:00:00', 5);"""

#*******************************************************#
# Insert query to populate "Orders" table:
#*******************************************************#
insert_orders="""
INSERT INTO Orders (OrderID, TableNo, MenuID, BookingID, Quantity, BillAmount)
VALUES
(1, 12, 1, 1, 2, 86),
(2, 19, 2, 2, 1, 37),
(3, 15, 2, 3, 1, 37),
(4, 5, 3, 4, 1, 40),
(5, 8, 1, 5, 1, 43);"""

#*******************************************************#
# Insert query to populate "Employees" table:
#*******************************************************#
insert_employees = """
INSERT INTO employees VALUES(EmployeeID, Name, Role, Address, Contact_Number, Email, Annual_Salary)
(01,'Mario Gollini','Manager','724, Parsley Lane, Old Town, Chicago, IL',351258074,'Mario.g@littlelemon.com','$70,000'),
(02,'Adrian Gollini','Assistant Manager','334, Dill Square, Lincoln Park, Chicago, IL',351474048,'Adrian.g@littlelemon.com','$65,000'),
(03,'Giorgos Dioudis','Head Chef','879 Sage Street, West Loop, Chicago, IL',351970582,'Giorgos.d@littlelemon.com','$50,000'),
(04,'Fatma Kaya','Assistant Chef','132  Bay Lane, Chicago, IL',351963569,'Fatma.k@littlelemon.com','$45,000'),
(05,'Elena Salvai','Head Waiter','989 Thyme Square, EdgeWater, Chicago, IL',351074198,'Elena.s@littlelemon.com','$40,000'),
(06,'John Millar','Receptionist','245 Dill Square, Lincoln Park, Chicago, IL',351584508,'John.m@littlelemon.com','$35,000');"""

# Populate MenuItems table
cursor.execute(insert_menuitems)
connection.commit()

# Populate MenuItems table
cursor.execute(insert_menu)
connection.commit()

# Populate Bookings table
cursor.execute(insert_bookings)
connection.commit()

# Populate Orders table
cursor.execute(insert_orders)
connection.commit()

# Populate Employees table
cursor.execute(insert_employees)
connection.commit()


#Obj1 Establishing connection
from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector import Error
dbconfig={"database":"little_lemon_db", "user":"your_username", "password":"your_password"}
try:
    pool = MySQLConnectionPool(pool_name = "pool_a",
                           pool_size = 2, #default is 5
                           **dbconfig)
    print("The connection pool is created with a name: ",pool.pool_name)
    print("The pool size is:",pool.pool_size)

except Error as er:
    print("Error code:", er.errno)
    print("Error message:", er.msg)
print("Getting a connection from the pool.")
connection1 = pool.get_connection()
print("Creating a cursor object.")
cursor = connection1.cursor()

#objective 2 using stored procedure
stored_procedure_query="""
CREATE PROCEDURE PeakHours()

BEGIN

SELECT Hour(BookingSlot), Count(Hour(BookingSlot)) 
FROM Bookings
Groub by Hour(BookingSlot)
ORDER BY Count(Hour(BookingSlot)) DESC LIMIT 1;

END

"""
# Execute the query
cursor.execute(stored_procedure_query)
# Call the stored procedure with its name
cursor.callproc("PeakHours")
results = next(cursor.stored_results() )
dataset = results.fetchall()
for column_id in cursor.stored_results():
    columns = [ column[0] for column in column_id.description ]

# Print column names
print(columns)

# Print data 
for data in dataset:
    print(data)



#Obj3
stored_procedure_query="""
CREATE PROCEDURE GuestStatus()

BEGIN

SELECT  
CONCAT(
Bookings.GuestFirstname,
' ',
bookings.GuestLastname
) AS CustomerName,
CASE
WHEN Role IN ("Manager") or ("Assistant Manager") THEN "Ready to pay" 
WHEN Role IN ("Head Chef") THEN "Ready to serve" 
WHEN Role IN ("Assistant Chef") THEN "Preparing Order"
WHEN Role IN ("Head Waiter") THEN "Order served"
ELSE "In Queue" 
END AS Status
FROM employees LEFT JOIN Bookings ON employees.EmployeeID = Bookings.EmployeeID;

END

"""
cursor.execute(stored_procedure_query)
results = next( cursor.stored_results() )
dataset = results.fetchall()
for column_id in cursor.stored_results():
    columns = [ column[0] for column in column_id.description ]

# Print column names
print(columns)

# Print data 
for data in dataset:
    print(data)
