import sqlite3


def connect():
    """
    It creates a database called books.db and creates a table called books.
    """
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (bid INTEGER PRIMARY KEY AUTOINCREMENT, title text,author text,status text,issuedto text)")
    # cur.execute("CREATE TABLE IF NOT EXISTS books_issued (bid INTEGER PRIMARY KEY AUTOINCREMENT, issuedto text)")
    conn.commit()
    conn.close()

def insert(title,author):
    """
    It takes in 4 parameters (bid,title, author, status) and inserts them into the database
    """
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    status="avail"
    issuedto=""
    cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(title,author,status,issuedto))
    print("Book inserted successfully")
    conn.commit()
    conn.close()

def view():
    """
    It connects to the database, fetches all the items in db, closes the connection, and
    returns the results.
    """
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",price=""):
    """
    It requires atleast one parameter to be passed in. It connects to the database, fetches all the items in db with particular search criteria, closes the connection, and returns the results.
    """
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR price=?",(title,author,year,price))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(bid):
    """
    It takes the id of the book as an argument and deletes the book from the database
    """
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM books WHERE bid=?",(bid,))
    conn.commit()
    conn.close()

def issuedTo(bid,user):
    """
    It updates the status of the book to "issued" and the issuedto column to the user who issued the
    book
    """
    
    status="issued"
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE books SET status=?,issuedto=? WHERE bid=?",(status,user,bid))
    conn.commit()
    conn.close()

def returnBook(bid):
    """
    It updates the status of the book to "available" and the issuedto column to ""
    """
    status="avail"
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE books SET status=?,issuedto=? WHERE bid=?",(status,"",bid))
    conn.commit()
    conn.close()

connect()

