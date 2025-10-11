book_file = "utils/books.csv"

def add_book(name,author):
    with open(book_file,'a') as books_file:
        info = f'{name},{author},0'
        books_file.write(info)
    print(f'{name} book written by {author} has been seccussfully stored in database.')


def _save_all_books(file_path,books):
    
    with open(file_path,'w') as book_store:
        for book in books:
            book_store.write(f'{book["name"]},{book["author"]},{book["read"]}\n')


def get_all_books():
    with open(book_file,"r") as books_file:
        books = books_file.readlines()
        books = [book.strip().split(',') for book in books]
    meta_data = ["name","author","read"]
    zipped_book = []
    for book in books:
        zipped_book.append(dict(zip(meta_data,book)))
    return zipped_book



def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book["name"] == name:
            book["read"] = '1'
    _save_all_books(book_file,books)

    


def delete_book(name):
    books = get_all_books()

    for book in books:
        if book["name"] == name:
            books.remove(book)
            break
    _save_all_books(book_file,books)
  






    