from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import AddBook
import DeleteBook
import ViewBooks
import IssueBook 
import ReturnBook 

# Creating a window with title "KJ SOMAIYA LIBRARY" and setting the minimum size of the window to
# 400x510 and the geometry to 600x450.
root = Tk()
root.title("KJ SOMAIYA LIBRARY")
root.minsize(width=400,height=510)
root.geometry("600x450")

# Take n greater than 0.25 and less than 5

same=True
n=0.25

# Adding a background image
background_image =Image.open("library.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

# Resizing the image.
newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

# Creating a canvas and adding the image to it.
Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

# Creating a frame and placing it in the window.
headingFrame1 = Frame(root,bg="#fff",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n KJ SOMAIYA Library", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

# Creating buttons and placing them in the window.
btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=AddBook.addBook)
btn1.place(relx=0.28,rely=0.35, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=DeleteBook.delete)
btn2.place(relx=0.28,rely=0.45, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Book List",bg='black', fg='white', command=ViewBooks.View)
btn3.place(relx=0.28,rely=0.55, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = IssueBook.issueBook)
btn4.place(relx=0.28,rely=0.65, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Return Book",bg='black', fg='white', command =ReturnBook.returnBook)
btn5.place(relx=0.28,rely=0.75, relwidth=0.45,relheight=0.1)

#Creating Quit button
quitBtn = Button(root,text="Quit",bg='#000000', fg='white', command=root.destroy)
quitBtn.place(relx=0.42,rely=0.91, relwidth=0.18,relheight=0.08)

root.mainloop()
