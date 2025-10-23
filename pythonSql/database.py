import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="W#@gvc12G",
    port=3306    
)

if connection.is_connected():
    print("✅ Successfully connected to MySQL")