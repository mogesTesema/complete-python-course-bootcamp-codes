import json
import os
""""
Concerned with storing and retrieving books form a json file.
"""

book_file = "utils/books.json"

def create_book_table():
    if not os.path.exists(book_file):
        with open(book_file,'w') as file:
            json.dump([],file)

def add_book(name,author):
    books = get_all_books()
    books.append({"name":name,"author":author,"read":False})
    _save_all_books(book_file,books)


def _save_all_books(file_path,books):
    
    with open(file_path,'w') as book_store:
        json.dump(books,book_store)

def get_all_books():
    try:
        with open(book_file,"r") as file:
            return json.load(file)
    except(FileNotFoundError,json.JSONDecodeError):
        return []



def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book["name"] == name:
            book["read"] = True
    _save_all_books(book_file,books)

    


def delete_book(name):
    books = get_all_books()

    for book in books:
        if book["name"] == name:
            books.remove(book)
            break
    _save_all_books(book_file,books)
  






    