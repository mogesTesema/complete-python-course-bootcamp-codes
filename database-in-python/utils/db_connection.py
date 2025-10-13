import sqlite3
def get_cursor():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    return cursor