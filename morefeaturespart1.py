import mysql.connector
#learnt its better to create functions for each block, so pehle mysqlconnect
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1001001",
        database="libraryms"
    )

def add_book():
    con = connect_db()
    cursor = con.cursor()
    
    bookname = input("Book title: ")
    bookauthor = input("Author: ")
    
    cursor.execute(
        "INSERT INTO mylibrary (bookname, bookauthor) VALUES (%s, %s)",
        (bookname, bookauthor)
    )
    
    con.commit()
    con.close()
    print("Book added!")

def show_books():
    con = connect_db()
    cursor = con.cursor()
    
    cursor.execute("SELECT * FROM mylibrary")
    mylibrary = cursor.fetchall()
    
    for book in mylibrary:
        print(book)
    
    con.close()

# User wishes
def main():
    
    while True:
        print("Hello, So what do you want to do today ?")
        print("\n1. Do you want to add a new book, enter 1 if so:")
        print("2. Do you want to view books, enter 2 if so:")
        print("3. If you want exit this space")
        
        choice = input(" Enter your Choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            break

if __name__ == "__main__":
     main()