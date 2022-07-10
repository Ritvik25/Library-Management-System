# Library Management System

In this project we have developed a library database system using Tkinter and sqlite3 that allows users to view booklist, add/remove books, issue and return books.

## Libraries Used

- Tkinter
- sqlite3
- Pillow

## Features

1. Once we run the code, we see a Tkinter window which is the frontend section (home page) of our project.
2. A simple home page is designed allowing the user to select from the menu choices whether they want to add a book, view a book, return a book, remove a book, or issue a book.
Description of files:
    - main.py: file which does function calling to all other functions and it is our home page of  the project.
    - AddBook.py: a program that performs the task of adding new books to the library.   
    - ViewBooks.py: To view the complete list of books in a library
    - DeleteBook.py: To Delete a book from the library.
    - IssueBook.py: To Issue a book from the library.
    - ReturnBook.py: To Return a book to a library.
    - backend.py: Our sqlite3 database system.
3. We have used a server-side database purely using sqlite3, so that all the records we create can be properly saved and a large database can also be created without a lot of hassle.
4. In this project, we have divided the various task into different files which we have imported into our main file, to make things easy to understand and build.

