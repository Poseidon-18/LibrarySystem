import mysql.connector
#learnt its better to create functions for each block, so pehle mysqlconnect
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="ur password",
        database="ur databse"
    )

def add_book():
    con = connect_db()
    cursor = con.cursor()
    
    bookname = input("Book title: ")
    bookauthor = input("Author: ")
    
    cursor.execute(
        "INSERT INTO your table (bookname, bookauthor) VALUES (%s, %s)",
        (bookname, bookauthor)
    )
    
    con.commit()
    con.close()
    print("Book added!")

def show_books():
    con = connect_db()
    cursor = con.cursor()
    
    cursor.execute("SELECT * FROM ur table")
    books = cursor.fetchall()
    
    for book in books:
        display_parts = []
        if book[0]:  
            display_parts.append(f"Information on the books : {book[0]}")
        if book[1]: 
            display_parts.append(f"'{book[1]}'")
        if book[2]:  
            display_parts.append(f"by {book[2]}")
        
        if len(display_parts) > 1:
            print(", ".join(display_parts))
        elif display_parts:  
            print(display_parts[0])
        else:  
            print("[Empty record]")
    
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
