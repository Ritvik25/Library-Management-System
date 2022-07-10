from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from backend import*

# Connecting to the database and creating a cursor.
con = sqlite3.connect("books.db")
cur = con.cursor()

# Enter Table Names here
bookTable = "books"
    
def View(): 
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Creating a canvas and setting the background color to blue.
    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#fcba9f")
    Canvas1.pack(expand=True,fill=BOTH)
               
    # Creating a frame and placing it at the top of the window.
    headingFrame1 = Frame(root,bg="#823212",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier',24))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    # Creating a frame and placing it at the bottom of the window.
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    # This is creating a label with the text "BID Title Author Status" and placing it at the top of the labelFrame.
    Label(labelFrame, text="%-10s%-50s%-40s%-20s"%('BID','Title','Author','Status'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    
    # Fetching the data from the database and displaying it in the GUI.
    getBooks = "select * from "+bookTable
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-40s%-40s%-20s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
   
    # Creating a button that will close the window.
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()