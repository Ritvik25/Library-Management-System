from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import backend
import sqlite3

con = sqlite3.connect("books.db")
cur = con.cursor()
# Enter Table Names here
issueTable = "books_issued" 
bookTable = "books" #Book Table

def deleteBook():
    bid=bookInfo1.get()
    backend.delete(bid)
    
def delete(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#bd7b02")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#fad796",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Courier',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.45,relwidth=0.8,relheight=0.2)

    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID : ", bg='black', fg='white',font=(10))
    lb2.place(relx=0.05,rely=0.40)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.45, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteBook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
