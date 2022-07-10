from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
import backend
"""
    A function that is used to register a book.
"""
def bookRegister():
   
  # Getting the values from the entry boxes.
    #bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    #status = bookInfo4.get()
    #status = status.lower()
    
    # insertBooks = "insert into "+bookTable+" values('"+bid+"','"+title+"','"+author+"','"+status+"')"
    # Trying to insert the data into the database. If it fails, it will show an error message.
    try:
        backend.insert(title,author)
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    #print(bid)
    print(title)
    print(author)
    #print(status)


    root.destroy()
    
def addBook(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
   
    # Connecting to the database and creating a cursor.
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    
    # Enter Table Names here
    bookTable = "books" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

# Creating a frame and placing it in the window.

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.3)
        
    # Book ID
    # Creating a label and an entry box.
    #lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    #lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    """bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)"""
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white',font=(10))
    lb2.place(relx=0.05,rely=0.35, relheight=0.12)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.25,rely=0.35, relwidth=0.62, relheight=0.12)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white', font=(10))
    lb3.place(relx=0.05,rely=0.60, relheight=0.12)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.25,rely=0.60, relwidth=0.62, relheight=0.12)
        
    # Book Status
    """lb4 = Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)"""
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
