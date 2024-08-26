import mysql.connector as connector
connection=connector.connect(user="your_username",password="your_password")
cursor = connection.cursor()
cursor.execute("USE little_lemon")

#obj1: innerjoin of menuitems and menu tables
join_query="""SELECT 
MenuItems.Name AS Item_Name, 
MenuItems.Type AS Item_Type, 
Menus.Cuisine AS Cuisine, 
MenuItems.Price AS Price 
FROM MenuItems 
INNER JOIN Menus ON MenuItems.ItemID=Menus.ItemID;"""
cursor.execute(join_query)
results = cursor.fetchall()
columns = cursor.column_names
print(columns)
for result in results:
    print(result)

#Obj2 left join operation
join_query="""SELECT 
MenuItems.Name AS Item_Name, 
MenuItems.Type AS Item_Type, 
Menus.Cuisine AS Cuisine, 
MenuItems.Price AS Price 
FROM MenuItems 
LEFT JOIN Menus ON MenuItems.ItemID=Menus.ItemID
WHERE Cuisine IS NULL;"""
cursor.execute(join_query)
results = cursor.fetchall()
columns = cursor.column_names
print(columns)
for result in results:
    print(result)

#Obj3 orders and booking table join
join_query="""SELECT 
Bookings.BookingID,
Bookings.TableNo,
Bookings.GuestFirstName,
Bookings.EmployeeID AS ServerID,
Orders.BillAmount
FROM Bookings
LEFT JOIN Orders ON Bookings.BookingID = Orders.BookingID;
"""
cursor.execute(join_query)
results = cursor.fetchall()
columns = cursor.column_names
print(columns)
for result in results:
    print(result)

if connection.is_connected():
    cursor.close()
    print("The cursor is closed.")
    connection.close()
    print("MySQL connection is closed.")
else:
    print("Connection is already closed")
