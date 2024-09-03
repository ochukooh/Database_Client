import mysql.connector as connector
connection=connector.connect(user="your_username",password="your_password")
cursor = connection.cursor()
import datetime as dt


#obj1 sort and group by time
sql_query = """SELECT 
COUNT(BookingID) AS n_bookings,
HOUR(BookingSlot) AS Hour 
FROM Bookings
GROUP BY Hour
ORDER BY Hour ASC;"""
cursor.execute(sql_query)
result = cursor.fetchall()

print("""Upcoming Bookings:\n""")
#print(cols)
for result in results:
    print("Hour: ",result[1],"<<>>", result[0], "Booking/s")


#Obj2 using python time function
sql_query = """SELECT 
TableNo, 
GuestFirstName, 
GuestLastName, 
BookingSlot 
FROM Bookings 
ORDER BY BookingSlot;"""
cursor.execute(sql_query)
results = cursor.fetchall()

print("The guests and their booking slots are:\n")
for result in results: 
    time = str(result[3])
    hour = dt.datetime.strptime(time,'%H:%M:%S').hour
    minute = dt.datetime.strptime(time,'%H:%M:%S').minute
    print("[Table no:]",result[0],">>",result[1],result[2], "is expected to arrive at:", 
          hour,"hrs and", minute, "mins")

#obj3 sorting and filtering sql command, python edit
sql_query = """SELECT 
BookingID, 
TableNo, 
BookingSlot, 
ADDTIME(BookingSlot,"1:00:00") as NewTime 
FROM Bookings
WHERE TableNo = 12 AND BookingID = 2;"""
cursor.execute(sql_query)
results = cursor.fetchall()

# Print time change alert.
print("Booking time change ALERT!!")
for result in results:  
    print("Booking ID:",result[0])
    print("Table number:",result[1])
    print("Booked slot:",result[2])
    print("New arrival time:",result[3])




# Let's close the cursor and the connection
if connection.is_connected():
    cursor.close()
    print("The cursor is closed.")
    connection.close()
    print("MySQL connection is closed.")
else:
    print("Connection is already closed")
