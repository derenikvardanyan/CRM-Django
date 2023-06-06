import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'bethebestDev95#',
)

# prepare cursor object

cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE legoholic")

print("Done!")