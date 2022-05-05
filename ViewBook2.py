
from tkinter import *
from tkinter import messagebox as msg
from personal import mypass,database
import pymysql
from tkinter import ttk

conn = pymysql.connect(
        host="localhost",
        user="root",
        password=mypass,
        database=database
        )
cursor = conn.cursor()
bookTable = 'books'



def view():
    root = Tk()
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root,bg="#85d7e6")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame = Frame(root,bg="#FFBB00",bd=4) 
    headingFrame.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame,text="View Books",bg="black",fg="white",font=("Courier",15))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    labelFrame = Frame(root,bg='white')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25

    style = ttk.Style()
    style.theme_use('clam')
    tree = ttk.Treeview(labelFrame,columns=("BID","Title","Author","Status"),show="headings")
    tree.column("#1",anchor=CENTER)
    tree.heading("#1",text="BID")

    tree.column("#2",anchor=CENTER)
    tree.heading("#2",text="Title")

    tree.column("#3",anchor=CENTER)
    tree.heading("#3",text="Author")

    tree.column("#4",anchor=CENTER)
    tree.heading("#4",text="Status")

    # verscrollbar = ttk.Scrollbar(labelFrame,orient="vertical",command=tree.yview)
    # horizscrollbar = ttk.Scrollbar(labelFrame,orient="horizontal",command=tree.xview )

    verscrollbar = Scrollbar(labelFrame,orient="vertical",command=tree.yview)
    horizscrollbar = Scrollbar(labelFrame,orient="horizontal",command=tree.xview)

    verscrollbar.pack(fill=Y,side="right")
    horizscrollbar.pack(fill=X,side="bottom")

    tree.configure(yscrollcommand=verscrollbar.set)
    tree.configure(xscrollcommand=horizscrollbar.set)



    
    try:
        cursor.execute(f"select * from {bookTable}")
        conn.commit()

        for i in cursor:
            tree.insert('','end',text="",values=(i[0],i[1],i[2],i[3]))
            
        # tree.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
        tree.pack(fill=BOTH)

    except:
        msg.showinfo("Failed","Failed to Fetch the files")

    quitBtn = Button(root,text="Quit",bg="#f7f1e3",fg="black",command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9,relwidth=0.18,relheight=0.08)

    root.mainloop()