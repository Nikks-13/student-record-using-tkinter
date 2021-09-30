from tkinter import *
import sqlite3

#conn=sqlite3.connect('SRA.db')
#conn.execute('''CREATE TABLE SRA
#(NAME      TEXT      NOT NULL,
#MAJOR      TEXT      NOT NULL,
#SEX        TEXT      NOT NULL,
#GPA        TEXT      NOT NULL,
#FID        TEXT      NOT NULL,
#AGE        TEXT      NOT NULL,
#ADDRESS    TEXT      NOT NULL);''')
#conn.close()

root = Tk()

root.geometry('500x300')
root.title("Student Record Application")

name = StringVar()
major = StringVar()
sex = StringVar()
gpa = StringVar()
fid = StringVar()
age = StringVar()
address = StringVar()
#----------------------------------------------------------------------


def connect():
    sql_connect = sqlite3.connect("SRA.db")
    mouse_cursor = sql_connect.cursor()
    mouse_cursor.execute(
        "CREATE TABLE IF NOT EXISTS SRA (id INTEGER PRIMARY KEY, name TEXT, major TEXT, age INTEGER, sex TEXT, address TEXT, gpa INTEGER)")
    sql_connect.commit()
    sql_connect.close()


def close():
    root.destroy()


#----------------------------------------------------------------------


def add():
    sql_connect = sqlite3.connect("SRA.db")
    mouse_cursor = sql_connect.cursor()
    mouse_cursor.execute("insert into SRA (NAME,MAJOR,SEX,GPA,FID,AGE,ADDRESS) values ('"+name.get()+"','" +
                         major.get()+"','"+sex.get()+"','"+gpa.get()+"','"+fid.get()+"','"+age.get()+"','"+address.get()+"')")

    sql_connect.commit()
    sql_connect.close()

#----------------------------------------------------------------------


def update():
   sql_connect = sqlite3.connect("SRA.db")
   #text.delete("1.0", "end")
   mouse_cursor = sql_connect.cursor()
   mouse_cursor.execute("update SRA set MAJOR='"+major.get()+"',SEX ='"+sex.get()+"',GPA='"+gpa.get() +
                        "',FID='"+fid.get()+"',AGE='"+age.get()+"',ADDRESS='"+address.get()+"' where NAME='"+name.get()+"'")
   sql_connect.commit()
   sql_connect.close()


#----------------------------------------------------------------------

def view():

    sql_connect = sqlite3.connect("SRA.db")
    text.delete("1.0", "end")
    mouse_cursor = sql_connect.cursor()
    mouse_cursor.execute("SELECT * FROM SRA")
    rows = mouse_cursor.fetchall()
    mouse_cursor.close()
    sql_connect.close()
    res = ''
    for i in rows:
        res = res + str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]) + ' ' + \
            str(i[3]) + ' ' + str(i[4]) + ' ' + \
            str(i[5]) + ' ' + str(i[6]) + "\n"
    return res

#-------------------------------------------------------------------


def delete():

    sql_connect = sqlite3.connect("SRA.db")
    text.delete("1.0", "end")
    mouse_cursor = sql_connect.cursor()
    mouse_cursor.execute("DELETE from SRA WHERE fid = " + fid.get())
    sql_connect.commit()
    sql_connect.close()


#----------------------------------------------------------------------


def search():

    sql_connect = sqlite3.connect("SRA.db")
    text.delete("1.0", "end")
    mouse_cursor = sql_connect.cursor()
    mouse_cursor.execute("SELECT * FROM SRA WHERE fid =" + fid.get())
    rows = mouse_cursor.fetchall()
    mouse_cursor.close()
    sql_connect.close()
    res = ''
    for i in rows:
        res = res + str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]) + ' ' + \
            str(i[3]) + ' ' + str(i[4]) + ' ' + \
            str(i[5]) + ' ' + str(i[6]) + "\n"

    return res
#----------------------------------------------------------------------


label_1 = Label(root, text="Name", width=20, font=("bold", 8))
label_1.place(x=-20, y=20)

entry_1 = Entry(root, textvariable=name)
entry_1.place(x=100, y=20)

label_2 = Label(root, text="Major", width=20, font=("bold", 8))
label_2.place(x=-20, y=42)

entry_2 = Entry(root, textvariable=major)
entry_2.place(x=100, y=42)

label_3 = Label(root, text="Sex", width=16, font=("bold", 8))
label_3.place(x=-10, y=62)

entry_3 = Entry(root, textvariable=sex)
entry_3.place(x=100, y=62)


label_4 = Label(root, text="GPA", width=16, font=("bold", 8))
label_4.place(x=-10, y=82)

entry_4 = Entry(root, textvariable=gpa)
entry_4.place(x=100, y=82)


label_5 = Label(root, text="ID", width=14, font=("bold", 8))
label_5.place(x=240, y=20)

entry_5 = Entry(root, textvariable=fid)
entry_5.place(x=350, y=20)

label_6 = Label(root, text="Age", width=10, font=("bold", 8))
label_6.place(x=250, y=42)

entry_6 = Entry(root, textvariable=age)
entry_6.place(x=350, y=42)

label_7 = Label(root, text="Address", width=10, font=("bold", 8))
label_7.place(x=250, y=62)

entry_7 = Entry(root, textvariable=address)
entry_7.place(x=350, y=62)

#---------------------------------------------------------------------


text = Text(root, height=10, width=24)
text.place(x=17, y=122, height=150, width=250)


#----------------------------------------------------------------------


button_1 = Button(root, text='View All', width=15,
                  command=lambda: text.insert(END, view()))
button_1.place(x=350, y=122)

button_2 = Button(root, text='search entry', width=15,
                  command=lambda: text.insert(END, search()))
button_2.place(x=350, y=152)

button_3 = Button(root, text='Add', width=15, command=add)
button_3.place(x=350, y=182)

button_4 = Button(root, text='Update selected', width=15, command=update)
button_4.place(x=350, y=210)

button_5 = Button(root, text='Deleted selected', width=15, command=delete)
button_5.place(x=350, y=237)

button_6 = Button(root, text='close', width=15, command=close)
button_6.place(x=350, y=265)


#----------------------------------------------------------------------
connect()
root.mainloop()
