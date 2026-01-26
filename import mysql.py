import mysql.connector
connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1001001",
            database="libraryms"
        )
if connection.is_connected():
        print("Connected to MySQL database successfully!")
else:
      print("Failed to connect to MySQL database.")

    # iske baad cursor instance bana lo for things you need to do: cur=connection,cursor()