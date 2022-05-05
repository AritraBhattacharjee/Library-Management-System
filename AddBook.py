
from tkinter import *

from tkinter import messagebox as msg
import pymysql
from personal import mypass,database

def bookRegister():
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()

    insertBooks = f"insert into {bookTable} values ('{bid}','{title}','{author}','{status}');"
    print (insertBooks)

    try:
        cursor.execute(insertBooks)
        conn.commit()
        msg.showinfo('Success',"Book added Successfully")
    except:
        msg.showinfo("Error","Cannot add Book to the Databases")
    
    root.destroy()

def addBook():
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,conn,cursor,bookTable,root

    root = Tk()
    root.title("Library Management System")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Establishing connection with mysql server
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password=mypass,
        database=database
        )
    cursor = conn.cursor()

    # Enter table names here
    bookTable= "books"

    Canvas1 = Canvas(root,bg="#ff6e40")
    Canvas1.pack(expand=TRUE,fill=BOTH)

    headingFrame = Frame(root,bg="#FFBB00",bd=5)
    headingFrame.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame,text="Add Books",bg = "black",fg="white",font=('Courier',15))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

    labelframe = Label(root,bg="black")
    labelframe.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)


    # BOOK ID
    lb1 = Label(labelframe,text="Book ID : ",bg="black",fg="white")
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)

    bookInfo1 = Entry(labelframe)
    bookInfo1.place(relx=0.3,rely=0.2,relwidth=0.62, relheight=0.08)#,height=15)

    #Title
    lb2 = Label(labelframe,text="Title: ",bg="black",fg="white")
    lb2.place(relx=0.05,rely=0.35,relheight=0.08)

    bookInfo2 = Entry(labelframe)
    bookInfo2.place(relx=0.3,rely=0.35,relwidth=0.62,relheight=0.08)

    #Book Author
    lb3 = Label(labelframe,text="Author : ",bg="black",fg="white")
    lb3.place(relx=0.05,rely=0.50,relheight=0.08)

    bookInfo3 = Entry(labelframe)
    bookInfo3.place(relx=0.3,rely=0.50,relwidth=0.62,relheight=0.08)

    
    # Book Status
    lb4 = Label(labelframe,text="Status(Avail/Issued) : ",bg="black",fg="white")
    lb4.place(relx=0.05,rely=0.65,relheight=0.08)

    bookInfo4 = Entry(labelframe)
    bookInfo4.place(relx=0.3,rely=0.65,relwidth=0.62,relheight=0.08)

    #Submit Button
    submitbtn = Button(root,text="SUBMIT",bg="green",fg="white",command=bookRegister)
    submitbtn.place(relx=0.28,rely=0.9,relwidth=0.18,relheight=0.08)
    quitBtn = Button(root,text="QUIT",bg="#f7f1e3",fg='black',command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9,relwidth=0.18,relheight=0.08)



    root.mainloop()