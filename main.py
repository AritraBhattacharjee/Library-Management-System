from tkinter import *
import pymysql
from PIL import ImageTk,Image

from AddBook import *
from ViewBook2 import *
from DeleteBook import *
from IssueBook import *
from ReturnBook import *

from personal import mypass,database
# conn = pymysql.connect(
#     host="localhost",
#     user="root",
#     password=mypass,
#     database=database
# )
# cursor = conn.connect()
class Library(Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Management System")
        self.minsize(width=400,height=400)
        self.geometry("700x650")

        # Issue 1 : cannot set background image with canvas
        same = True
        n = 0.25
        # background_image = Image.open("D:\\Programming\\Python\\Project\\Library-Management-System\\1.jpg")
        # [imageSizeWidth,imageSizeHeight] = background_image.size

        # newImageSizeWidth = int(imageSizeWidth*n)
        # if same:
        #     newImageSizeHeight = int(imageSizeHeight*n)
        # else:
        #     newImageSizeHeight = int(imageSizeHeight/n)

        # background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
        # img = ImageTk.PhotoImage(background_image)
        # # img = PhotoImage(file = "1.jpg")
        canvas1 = Canvas(self,bg="#85d7e6")
        # canvas1 = Canvas(self,width=newImageSizeWidth,height=newImageSizeHeight,bg="#85d7e6")
        
        # canvas1.create_image(10,10,image=img,anchor=NW)
        canvas1.pack(fill=BOTH,expand=TRUE)
        # canvas1.create_oval(3,5,700,300)

        # issue uptill here

        # adding a frame and a heading in that frame
        heading = Frame(self,bg="#FFBB00",bd=5)
        heading.place(relx=0.2,rely=0.1,relheight=0.16,relwidth=0.6)
        
        headinglabel = Label(heading,text="Welcome to \n Library",bg='black',fg='white',font=('Courier',15))
        headinglabel.place(relx=0,rely=0,relwidth=1,relheight=1)

        # Adding Buttons
        btn1 = Button(self,text="Add Book Details",bg='black',fg='white', command=addBook,font=('Courier',15))
        btn1.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.1)

        btn2 = Button(self,text="Delete Book",bg='black',fg='white', command=deleteBook,font=('Courier',15))
        btn2.place(relx=0.28,rely=0.5,relwidth=0.45,relheight=0.1)

        btn3 = Button(self,text="View Book List",bg='black',fg='white', command=view,font=('Courier',15))
        btn3.place(relx=0.28,rely=0.6,relwidth=0.45,relheight=0.1)

        btn4 = Button(self,text="Issue Book to Student",bg='black',fg='white', command=issueBook,font=('Courier',15))
        btn4.place(relx=0.28,rely=0.7,relwidth=0.45,relheight=0.1)

        btn5 = Button(self,text="Return Book",bg='black',fg='white', command=returnBook,font=('Courier',15))
        btn5.place(relx=0.28,rely=0.8,relwidth=0.45,relheight=0.1)

    
    
    def connect(self):
        conn = pymysql.connect(
        host="localhost",
        user="root",
        password=mypass,
        database=database
        )
        curr = conn.cursor()
        # curr.execute("select @@version")
        # curr.execute("show tables")
        output = curr.fetchall()
        # print(output)
        # for i in output:
        #     print(i)
        conn.close()


        
if __name__=='__main__':
    obj = Library()
    # obj.connect()

    obj.mainloop()