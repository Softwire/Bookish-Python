import sqlite3
from book import Book

class DbManager():

    def __init__(self):
        # connect to the database
        self.conn = sqlite3.connect('bookish.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        # create a table
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS book(
                title text,
                author text,
                year_published integer
            )
            """
        )
        # Set a unique constraint on title
        self.cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS book_title ON book ( title )")

    # CRUD functions

    # Create
    def add_book(self, book):
        self.cursor.execute(
            "INSERT OR REPLACE INTO book VALUES (?, ?, ?)",
            [book.title, book.author, book.date_published]
        )
        self.conn.commit()

    # Read
    def get_all_books(self):
        self.cursor.execute("SELECT * FROM book")
        dbBooks = self.cursor.fetchall()
        books = map(lambda book: Book(book[0], book[1], book[2]), dbBooks)
        return list(books)

    def print_all_books_to_terminal(self):
        books = self.cursor.execute("SELECT * from book")
        for book in books:
            print(f"{book[0]}, {book [1]}, {book[2]}")

    def get_book_by_title(self, title):
        dbBook = self.cursor.execute("SELECT * FROM book WHERE title = ?", [title])
        book = map(lambda book: Book(book[0], book[1], book[2]), dbBook)
        return list(book)

    # Update
    def update_author(self, title, author):
        self.cursor.execute("UPDATE book SET author = ? WHERE title = ?", [author, title])
        self.conn.commit()

    # Delete
    def delete_book(self, title):
        self.cursor.execute("DELETE FROM book WHERE title = ?", [title])
        self.conn.commit()
