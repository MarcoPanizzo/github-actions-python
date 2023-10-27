import unittest
import library  # Import the module with your CRUD functions

class TestLibraryFunctions(unittest.TestCase):

    def setUp(self):
        # Set up a test database in memory
        self.conn = library.create_test_db()
        self.cursor = self.conn.cursor()

    def tearDown(self):
        # Close the test database connection
        self.conn.close()

    def test_create_book(self):
        # Test the create_book function
        library.create_book(self.cursor, "Test Book", "Test Author", 2023)
        self.conn.commit()

        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0], (1, "Test Book", "Test Author", 2023))

    def test_read_books(self):
        # Test the read_books function
        books = library.read_books(self.cursor)
        self.assertEqual(len(books), 0)

        library.create_book(self.cursor, "Book 1", "Author 1", 2000)
        library.create_book(self.cursor, "Book 2", "Author 2", 2010)
        self.conn.commit()

        books = library.read_books(self.cursor)
        self.assertEqual(len(books), 2)

    def test_update_book(self):
        # Test the update_book function
        library.create_book(self.cursor, "Book 1", "Author 1", 2000)
        self.conn.commit()

        library.update_book(self.cursor, 1, "Updated Book", "Updated Author", 2022)
        self.conn.commit()

        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0], (1, "Updated Book", "Updated Author", 2022))

    def test_delete_book(self):
        # Test the delete_book function
        library.create_book(self.cursor, "Book 1", "Author 1", 2000)
        self.conn.commit()

        library.delete_book(self.cursor, 1)
        self.conn.commit()

        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()
        self.assertEqual(len(books), 0)

if __name__ == '__main__':
    unittest.main()
