import sqlite3

# Function to create a test database in memory
def create_test_db():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            year INTEGER
        )
    ''')
    return conn

# Function to create a new book
def create_book(cursor, title, author, year):
    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))

# Function to read all books
def read_books(cursor):
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    return books

# Function to update a book
def update_book(cursor, book_id, title, author, year):
    cursor.execute("UPDATE books SET title=?, author=?, year=? WHERE id=?", (title, author, year, book_id))

# Function to delete a book
def delete_book(cursor, book_id):
    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
