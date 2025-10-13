from .db_connection import DatabaseConnection

""""
Concerned with storing and retrieving books form a sqlite database.
"""

book_store = "data.db"

def create_book_table():
    with DatabaseConnection(book_store) as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key,author text,read integer)")
        
        

def add_book(name,author):
    """
    SQL Injection:
        injection_command = ",0);DROP TABLE books;
        cursor.execute(f'INSERT INTO books VALUES("{name}","{injection_command},"{0}")') # leads to         cursor.execute(f'INSERT INTO books VALUES("{name}","",0)DROP TABLE books;,"{0}")')
    """
    
    with DatabaseConnection(book_store) as connection:
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO books VALUES(?,?,0)",(name,author))
        except Exception as e:
            print(f"{name} is already exist. {e}")
       


def get_all_books():
    books = []
    try:
        with DatabaseConnection(book_store) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()
        zipped_book = []
        meta_data = ["name","author","read"]
        for book in books:
            zipped_book.append(dict(zip(meta_data,book)))
        
        return zipped_book

        
    except():
        return []



def mark_book_as_read(name):
    with DatabaseConnection(book_store) as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE books SET read=1 where name=?",(name,))



    


def delete_book(name):
    with DatabaseConnection(book_store) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM books where name=?",(name,))

  
  






    