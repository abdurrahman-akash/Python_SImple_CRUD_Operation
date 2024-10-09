import mysql.connector
from mysql.connector import Error

# Connecting to the MySQL server
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=""
    )

    # Verify connection
    if db.is_connected():
        print("Database is connected.")
    
    # Creating a cursor object
    mycursor = db.cursor()
    
    # Create the database if it doesn't exist
    mycursor.execute("CREATE DATABASE IF NOT EXISTS studentdb")
    print("Database 'studentdb' created or already exists.")
    
    # Connecting to the new database
    db.database = "studentdb"
    
    # Creating a table
    studenttbl_create = """CREATE TABLE IF NOT EXISTS student (
      studentid INT NOT NULL AUTO_INCREMENT,
      studentname VARCHAR(45) NULL,
      department VARCHAR(45) NULL,
      phone VARCHAR(15) NULL,
      PRIMARY KEY (studentid))"""
    
    # Execute the query
    mycursor.execute(studenttbl_create)
    print("Table 'student' created or already exists.")
    
    # Commit the changes
    db.commit()

except Error as e:
    print(f"Error: {e}")

finally:
    if db.is_connected():
        mycursor.close()
        db.close()
        print("Connection closed.")
