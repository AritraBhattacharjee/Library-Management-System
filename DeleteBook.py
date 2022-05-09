from logging import root
from tkinter import * 
from tkinter import messagebox as msg
from personal import mypass,database
import pymysql

conn = pymysql.connect(
        host="localhost",
        user="root",
        password=mypass,
        database=database
    )

cursor = conn.cursor()
issueTable = "books_issued"
bookTable = "books"



def delete():
    bid = bookInfo1.get()
    deleteSql = f"delete from {bookTable} where bid = {bid};"

    deleteIssue = f"delete from {issueTable} where bid = {bid}"

    try:
        cursor.execute(deleteSql)
        conn.commit()
        cursor.execute(deleteIssue)
        conn.commit()

        msg.showinfo("Success","Book Record Deleted")
    except:
        msg.showinfo("Error","Please check Book ID")

    print(bid)
    bookInfo1.delete(0,END)
    root.destroy

def deleteBook():
    global bookInfo1,bookInfo2,bookInfo3,bookInfo3, Canvas1,conn,cursor,bookTable,root

    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root,bg = "#006B38")
    Canvas1.pack(expand=TRUE,fill=BOTH)

    headingFrame = Frame(root,bg="#FFBB00",bd=5)
    headingFrame.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame,text="Delete Book",bg="black",fg="white",font=("Courier",15))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

    labelFrame = Frame(root,bg="black")
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

    lb2 = Label(labelFrame,text="BOOK ID : ",bg="black",fg="white")
    lb2.place(relx=0.05,rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5,relwidth=0.62)

    submitBtn = Button(root,text="Submit",bg="#d1ccc0",fg="black",command=delete)
    submitBtn.place(relx=0.28,rely=0.9,relwidth=0.18,relheight=0.08)

    quitBtn = Button(root,text="QUIT",bg="#f7f1e3",fg="black",command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9,relwidth=0.18,relheight=0.08)

    root.mainloop()
