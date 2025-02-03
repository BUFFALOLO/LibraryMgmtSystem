# PROJECT REQUIREMENTS
In this project, you will integrate a MySQL database with Python to develop an advanced Library Management System. This command-line-based application is designed to streamline the management of books and resources within a library. Your mission is to create a robust system that allows users to browse, borrow, return, and explore a collection of books while demonstrating your proficiency in database integration, SQL, and Python.

**Integration with the "Library Management System" Project from Module 4 (OOP):**
For this project, you will build upon the foundation laid in "Module 4: Python Object-Oriented Programming (OOP)." The object-oriented structure and classes you developed in that module will serve as the core framework for the Library Management System. You will leverage the classes such as Book, User, Author, and Genre that you previously designed, extending their capabilities to integrate seamlessly with the MySQL database.



**Enhanced User Interface (UI) and Menu:**
- Create an improved, user-friendly command-line interface (CLI) for the Library Management System with separate menus for each class of the system.
        Welcome to the Library Management System!
        
        Main Menu:
        1. Book Operations
        2. User Operations
        3. Author Operations
        4. Quit
  
        Book Operations:
        1. Add a new book
        2. Borrow a book
        3. Return a book
        4. Search for a book
        5. Display all books

        User Operations:
        1. Add a new user
        2. View user details
        3. Display all users
  
        Author Operations:
        1. Add a new author
        2. View author details
        3. Display all authors
  
**Database Integration with MySQL:**
- Integrate a MySQL database into the Library Management System to store and retrieve data related to books, users, authors, and genres.
- Design and create the necessary database tables to represent these entities. You will align these tables with the object-oriented structure from the previous project.
- Establish connections between Python and the MySQL database for data manipulation, enhancing the persistence and scalability of your Library Management System.

**Data Definition Language Scripts:**
- Create the necessary database tables for the Library Management System. For instance:
- 
```
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    isbn VARCHAR(13) NOT NULL,
    publication_date DATE,
    availability BOOLEAN DEFAULT 1,
    FOREIGN KEY (author_id) REFERENCES authors(id),
);
```

