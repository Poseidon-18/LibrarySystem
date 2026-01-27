def LibraryMS():
    bookname= input("enter name of the book:")
    bookauthor= input("enter book's author:")
    datebought= input("enter date") #ya toh import date time ya fir int karke?
    import mysql.connector 
    connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ur password",
            database="ur database"
        )
if connection.is_connected():
        print("Connected to MySQL database successfully!")
else:
      print("Failed to connect to MySQL database.")
cur = database.cursor()

# Use all the SQL you like
cur.execute("INSERT INTO table(bookname,bookauthor) VALUES
    ("Mahagatha"),("Farheniet 415")
    ("Satyarath Nayak"),("Ray Bradbury"))"
cur.execute("Select * from table")
print("books updated!")

database.close()

