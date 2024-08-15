# Print a message to guide the user
# Import MySQL Connector/Python 
print("Importing MySQL Connector/Python API")
import mysql.connector as connector
print("MySQL Connector/Python API is imported successfully.\n")

# Establis connection with authorized user/password
print("Establishing a new connection between MySQL and Python.")
#connection=connector.connect(user="your_username",password="your_password")

connection=connector.connect(user="root",password="")
print("A connection between MySQL and Python is successfully established")

# ensure that there are no connection issues when connecting with MySQL database
import mysql.connector as connector

try:
    connection=connector.connect(
        user="wrong_user",
        password='wrong_password'
    )
except:
    print("""
    There was a problem connecting to the database.
    Please check your username or the password.
    """)
  
  # know the reason for any issues that might occur when connecting to the database.
  import mysql.connector as connector

try:
    connection=connector.connect(
        user="ameta",
        password="password",
        database = "no_database")

except connector.Error as er:
    print("Error code:", er.errno)
    print("Error message:", er.msg)
#Error code: 1045
#Error message: Access denied for user 'ameta'@'localhost' (using password: YES)

# Let's close the cursor and the connection
if connection.is_connected():
    connection.close()
    print("MySQL connection is closed.")
else:
    print("Connection is already closed")
