def LibraryMS():
    bookname = input("enter name of the book: ")
    bookauthor = input("enter book's author: ")
    bookid=input("enter id for ur book:")
    #datebought = input("enter date: ")
    
    import mysql.connector 
    connection = mysql.connector.connect(
        host="localhost",
            user="root",
            password="ur password",
            database="ur database"
    )
    
    if connection.is_connected():
        print("Connected to MySQL database successfully!")
        
    #as learnt from google and deepseek
    
        cur = connection.cursor()
        

        sql = "INSERT INTO table (bookname, bookauthor,bookid) VALUES (%s, %s,%s)"
        values = (bookname, bookauthor,bookid)
        
        cur.execute(sql, values)
        connection.commit()
        print("Data inserted successfully!")
        print("Books in library now are:")
        cur.execute("SELECT * FROM table")
        booksnow = cur.fetchall()
        print(booksnow)
        cur.close()
        connection.close()
    else:
        print("Failed to connect to MySQL database.")


LibraryMS()
# theres something called autoincrement.
