import re
from mysql.connector import Error
from database_connection import connect_database
from BookClass import Book
from UserClass import User
from AuthorClass import Author

books = []
users = []
authors = []

def main_menu():
    while True:
        print("\nWelcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")

        choice = input("Select an option: ")
        if choice == '1':
            book_menu()
        elif choice == '2':
            user_menu()
        elif choice == '3':
            author_menu()
        elif choice == '4':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def book_menu():
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to Main Menu")

        choice = input("Select an option: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            search_book()
        elif choice == '5':
            display_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please select a valid option.")

def user_menu():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to Main Menu")

        choice = input("Select an option: ")
        if choice == '1':
            add_user()
        elif choice == '2':
            view_user()
        elif choice == '3':
            display_users()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

def author_menu():
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to Main Menu")

        choice = input("Select an option: ")
        if choice == '1':
            add_author()
        elif choice == '2':
            view_author()
        elif choice == '3':
            display_authors()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    genre = input("Enter genre: ")
    pub_date = input("Enter publication date (MM-DD-YYYY): ")

    if not re.match(r"\d{2}-\d{2}-\d{4}", pub_date):
        print("Invalid date format. Please use MM-DD-YYYY.")
        return

    books.append(Book(title, author, genre, pub_date))
    print(f"Book '{title}' added successfully!")

def borrow_book():
    title = input("Enter the title of the book to borrow: ")
    for book in books:
        if book.get_title() == title:
            if book.borrow_book():
                print(f"You've successfully borrowed '{title}'.")
            else:
                print(f"'{title}' is already borrowed.")
            return
    print(f"Book '{title}' not found.")

def return_book():
    title = input("Enter the title of the book to return: ")
    for book in books:
        if book.get_title() == title:
            if book.return_book():
                print(f"'{title}' has been successfully returned.")
            else:
                print(f"'{title}' wasn't borrowed.")
            return
    print(f"Book '{title}' not found.")

def search_book():
    title = input("Enter the title of the book to search for: ")
    for book in books:
        if book.get_title() == title:
            print(book.display_details())
            return
    print(f"Book '{title}' not found.")

def display_books():
    if not books:
        print("No books available.")
    else:
        for book in books:
            print(book.display_details())

def add_user():
    name = input("Enter user name: ")
    library_id = input("Enter library ID: ")

    if not library_id.isdigit():
        print("Library ID should be numeric.")
        return

    users.append(User(name, library_id))
    print(f"User '{name}' added successfully!")

def view_user():
    library_id = input("Enter library ID to view details: ")
    for user in users:
        if user.get_library_id() == library_id:
            print(user.display_details())
            return
    print(f"User with ID '{library_id}' not found.")

def display_users():
    if not users:
        print("No users available.")
    else:
        for user in users:
            print(user.display_details())

def add_author():
    name = input("Enter author name: ")
    bio = input("Enter author bio: ")
    authors.append(Author(name, bio))
    print(f"Author '{name}' added successfully!")

def view_author():
    name = input("Enter the name of the author to view: ")
    for author in authors:
        if author.display_details().startswith(f"Author Name: {name}"):
            print(author.display_details())
            return
    print(f"Author '{name}' not found.")

def display_authors():
    if not authors:
        print("No authors available.")
    else:
        for author in authors:
            print(author.display_details())

if __name__ == "__main__":
    main_menu()
