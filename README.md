# PROJECT REQUIREMENTS
In this project, you will integrate a MySQL database with Python to develop an advanced Library Management System. This command-line-based application is designed to streamline the management of books and resources within a library. Your mission is to create a robust system that allows users to browse, borrow, return, and explore a collection of books while demonstrating your proficiency in database integration, SQL, and Python.

**Integration with the "Library Management System" Project from Module 4 (OOP):**
For this project, you will build upon the foundation laid in "Module 4: Python Object-Oriented Programming (OOP)." The object-oriented structure and classes you developed in that module will serve as the core framework for the Library Management System. You will leverage the classes such as Book, User, Author, and Genre that you previously designed, extending their capabilities to integrate seamlessly with the MySQL database.



**1. Enhanced User Interface (UI) and Menu:**
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
        
        Books Table:
        """CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    isbn VARCHAR(13) NOT NULL,
    publication_date DATE,
    availability BOOLEAN DEFAULT 1,
    FOREIGN KEY (author_id) REFERENCES authors(id),
        );"""
  
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

**6. User Interaction:**
- Utilize the input() function within the appropriate menus to enable users to interact with the CLI and select menu options.
- Implement input validation using regular expressions (regex) to ensure the correct formatting of user input. (Bonus)

**7. Error Handling:**
Implement error handling where applicable using try, except, else, and finally blocks to manage potential issues gracefully, such as incorrect user input or file operations.

**7. GitHub Repository:**
- Create a GitHub repository for your project and commit code regularly.
- Maintain a clean and interactive README.md file in your GitHub repository, providing clear instructions on how to run the application and explanations of its features.
- Include a link to your GitHub repository in your project documentation.

**7. Optional Bonus Points:**
- Text File Handling (Bonus): Implement text file handling to load and save data for various entities in the library management system, such as books, users, authors, and genres. Create dedicated text files for each entity type and develop methods to read data from these files during system startup and save data to them when changes occur. Ensure data integrity and error handling during file operations.
- Reservation System (Bonus): Enhance the system by implementing a reservation system. Users can reserve books that are currently unavailable, and the system will notify them when the book becomes available. Develop methods to handle reservations, check availability, and notify users of reservation status changes.
- Fine Calculation (Bonus): Implement a fine calculation system for overdue books. Assign due dates to borrowed books, and calculate fines for users who exceed the due date. Develop a mechanism for users to pay fines and update their accounts accordingly.
