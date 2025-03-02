# import mysql.connector

# dataBase = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = 'Aqsa@1029'
# )

# # prepare a cursor object
# cursorObject = dataBase.cursor()

# # create a database
# cursorObject.execute("CREATE DATABASE elderco")

# print("ALL Done")
import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aqsa@1029"
    )
    print("Connected successfully!")
except mysql.connector.Error as err:
    print("Error:", err)

