import mysql.connector as connector
connection=connector.connect(user="your_username",password="your_password")
cursor = connection.cursor()
cursor.execute("USE little_lemon")

#Obj 1 return the fullname of guest from bookings table in uppercase
sql_query="""
SELECT 
BookingID AS ID,
UPPER(CONCAT(GuestFirstName,' ',GuestLastName)) 
AS GuestFullName 
FROM bookings;"""

cursor.execute(sql_query)
result=cursor.fetchall()
columns=cursor.column_names
print(columns)
for x in result:
  print(x)

#Obj2 performing statistics on the bookingID and Billamoount from the orders table
sql_query="""
SELECT 
COUNT(BookingID) AS n_bookings,
SUM(BillAmount) AS Total_sale,
AVG(BillAmount) AS Avg_sale
FROM Orders;"""
cursor.execute(sql_query)
result = cursor.fetchall()

print("Today's statistics:")
for result in results:
    print("Number of bookings:",result[0])
    print("Total sale:",result[1])
    print("Average sale:",result[2])

#Obj 3 grouping and sorting data
sql_query="""SELECT 
TableNo AS 'Table number', 
COUNT(TableNo) AS n_booking
FROM Bookings 
GROUP BY TableNo 
ORDER BY n_booking DESC;"""
cursor.execute(sql_query)
results = cursor.fetchall()
columns = cursor.column_names
print(columns)
for result in results:
    print(result)

#obj3 using case and time function
sql_query="""
SELECT
BookingID,
CONCAT(GuestFirstName,' ',GuestLastName) AS Guest_Name,

CASE
WHEN HOUR(BookingSlot) IN (15,16) THEN "Late afternoon" 
WHEN HOUR(BookingSlot) IN (17,18) THEN "Evening" 
WHEN HOUR(BookingSlot) IN (19,20) THEN "Night"
ELSE "Time not available" 
END AS Arrival_slot

FROM Bookings;"""
cursor.execute(sql_query)
results = cursor.fetchall()
columns = cursor.column_names
print(columns)
or result in results:
    print(result)

    print("Connection is already closed")

