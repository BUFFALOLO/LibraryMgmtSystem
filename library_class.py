from mysql.connector import Error
from database_connection import connect_database
from datetime import date, timedelta
from book_class import Book 
from user_class import User


class Library:
    def add_book(self, book: object): 
        conn = connect_database() 
        if conn is not None: 
            try:
                cursor = conn.cursor() 
                book_to_add = (book.get_title(), book.get_author_id(), book.get_isbn(), book.get_publish_date()) 
                query = "INSERT INTO books (title, author_id, isbn, publication_date) VALUES (%s, %s, %s, %s)" 
                cursor.execute(query, book_to_add) 
                conn.commit() 
                print(f"{book.get_title()} has been added to the library database.") 
            except Exception as ge: 
                print(f"General Error Occurred: {ge}")
            except Error as dbe: 
                print(f"Database Error Occurred: {dbe}")
            finally: 
                cursor.close()
                conn.close()

    def borrow_book(self, book_id, user_id): 
        conn = connect_database() 
        if conn is not None: 
            try:
                cursor = conn.cursor()
                availability = False 
                borrow_date = date.today() 
                return_date = borrow_date + timedelta(days=7) 
                borrowed_book = (user_id, book_id, borrow_date, return_date, availability, book_id) 
                query = """
                    INSERT INTO borrowed_books (user_id, book_id, borrow_date, return_date) VALUES (%s, %s, %s, %s);
                    UPDATE books SET availability = %s WHERE id = %s;
                """
                cursor.execute(query, borrowed_book) 
                conn.commit() 
                print(f"Book ID '{book_id}' has been borrowed by '{user_id}'.") 
            except Exception as ge: 
                print(f"General Error Occurred: {ge}")
            except Error as dbe: 
                print(f"Database Error Occurred: {dbe}")
            finally: #
                cursor.close()
                conn.close()

    def return_book(self, book_id, user_id): 
        conn = connect_database() 
        if conn is not None: 
            try:
                cursor = conn.cursor() 
                availability = True 
                returned_book = (user_id, book_id) 
                availability = (availability, book_id)
                query1 = "DELETE FROM borrowed_books WHERE user_id = %s AND book_id = %s;"
                query2 = "UPDATE books SET availability = %s WHERE id = %s;"  
                cursor.execute(query1, returned_book) 
                cursor.execute(query2, availability) 
                conn.commit() 
                print(f"Book ID '{book_id}' has been returned by '{user_id}'.")
            except Exception as ge: #
                print(f"General Error Occurred: {ge}")
            except Error as dbe: 
                print(f"Database Error Occurred: {dbe}")
            finally: 
                cursor.close()
                conn.close()

    def view_books(self): 
        conn = connect_database() 
        if conn is not None: 
            try:
                cursor = conn.cursor() 
                query = "SELECT * FROM books" 
                cursor.execute(query) 
                for book in cursor.fetchall(): 
                    print(book) 
            except Exception as ge: 
                print(f"General Error Occurred: {ge}")
            except Error as dbe: 
                print(f"Database Error Occurred: {dbe}")
            finally: 
                cursor.close()
                conn.close()

    def search_book(self, book_id):
        conn = connect_database() 
        if conn is not None: 
            try:
                cursor = conn.cursor() 
                search_book = (book_id,)
                query = "SELECT * FROM books WHERE id = %s" 
                cursor.execute(query, search_book) 
                for book in cursor.fetchall(): 
                    print(book) 
            except Exception as ge: 
                print(f"General Error Occurred: {ge}")
            except Error as dbe: 
                print(f"Database Error Occurred: {dbe}")
            finally: 
                cursor.close()
                conn.close()

    def add_author(self, author: object): 
        conn = connect_database() 
        if conn is not None: 
            try:
                cursor = conn.cursor() 
                author_to_add = (author.get_author_name(), author.get_author_biography()) 
                query = "INSERT INTO authors (name, biography) VALUES (%s, %s)" 
                cursor.execute(query, author_to_add) 
                conn.commit() 
                print(f"New author: {author.get_author_name()} was successfully added to the library database.") 
            except Exception as ge: 
                print(f"General Error Occurred: {ge}")
            except Error as dbe: 
                print(f"Database Error Occurred: {dbe}")
            finally: 
                cursor.close()
                conn.close()

    def view_authors(self): 
        conn = connect_database() 
        if conn is not None: 
            try:
                cursor = conn.cursor() 
                query = "SELECT * FROM authors" 
                cursor.execute(query) 
                for author in cursor.fetchall(): 
                    print(author) 
            except Exception as ge: 
                print(f"General Error Occurred: {ge}")
            except Error as dbe: 
                print(f"Database Error Occurred: {dbe}")
            finally: 
                cursor.close()
                conn.close()

    def search_author(self, author_id):
        conn = connect_database() 
        if conn is not None: 
            try:
                cursor = conn.cursor() 
                search_author = (author_id,)
                query = "SELECT * FROM authors WHERE id = %s" 
                cursor.execute(query, search_author) 
                for author in cursor.fetchall(): 
                    print(author) 
            except Exception as ge: 
                print(f"General Error Occurred: {ge}")
            except Error as dbe: 
                print(f"Database Error Occurred: {dbe}")
            finally: 
                cursor.close()
                conn.close()

    def add_user(self, user: object):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor() 
                user_to_add = (user.get_user_name(), user.get_user_id())
                query = "INSERT INTO users (name, library_id) VALUES (%s, %s)" 
                cursor.execute(query, user_to_add) 
                conn.commit() 
                print(f"New user: {user.get_user_name()} was successfully added to the library database.") 
            except Exception as ge: 
                print(f"General Error Occurred: {ge}")
            except Error as dbe: 
                print(f"Database Error Occurred: {dbe}")
            finally: 
                cursor.close()
                conn.close()

    def view_users(self): 
        conn = connect_database() 
        if conn is not None: 
            try:
                cursor = conn.cursor() 
                query = "SELECT * FROM users"
                cursor.execute(query)
                for user in cursor.fetchall(): 
                    print(user) 
            except Exception as ge: 
                print(f"General Error Occurred: {ge}")
            except Error as dbe: 
                print(f"Database Error Occurred: {dbe}")
            finally: 
                cursor.close()
                conn.close()

    def search_user(self, user_id):
        conn = connect_database() 
        if conn is not None: 
            try:
                cursor = conn.cursor() 
                search_user = (user_id,)
                query = "SELECT * FROM users WHERE id = %s"
                cursor.execute(query, search_user) 
                for user in cursor.fetchall():
                    print(user)
            finally: 
                cursor.close()
                conn.close()