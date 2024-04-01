from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import pymysql as mysql

win=Tk()
win.geometry("500x500")

label_font=font.Font(weight="bold",family="Times New Roman",size=30)
f1=Label(win,text="STUDENT REGISTRATION",font=label_font,bg="sky blue",fg="white")
f1.place(relx=0.40,rely=0.5)
f1.pack()
f=Frame(win,width=800,height=630,bg="pink")
f.place(relx=0.20,rely=0.10)
label_font=font.Font(weight="bold",family="Times New Roman",size=20)
l=Label(win,text="sid",font=label_font)
l.place(relx=0.25,rely=0.1)
l1=Label(win,text="Name",font=label_font)
l1.place(relx=0.25,rely=0.2)
l2=Label(win,text="Father Name",font=label_font)
l2.place(relx=0.25,rely=0.3)
l3=Label(win,text="contact",font=label_font)
l3.place(relx=0.25,rely=0.4)
l4=Label(win,text="Email-Id",font=label_font)
l4.place(relx=0.25,rely=0.5)
l5=Label(win,text="address",font=label_font)
l5.place(relx=0.25,rely=0.6)

e1=Entry(win)
e1.place(relx=0.55,rely=0.1,width=150,height=30)
e2=Entry(win)
e2.place(relx=0.55,rely=0.2,width=150,height=30)
e3=Entry(win)
e3.place(relx=0.55,rely=0.3,width=150,height=30)
e4=Entry(win)
e4.place(relx=0.55,rely=0.4,width=150,height=30)
e5=Entry(win)
e5.place(relx=0.55,rely=0.5,width=150,height=30)
e6=Entry(win)
e6.place(relx=0.55,rely=0.6,width=150,height=30)

r=Label(win,text="Gender",font=label_font)
r.place(relx=0.25,rely=0.7)
var=IntVar()
label_font=font.Font(weight="bold",family="Times New Roman",size=16)
r1=Radiobutton(win,text="Male",font=label_font,variable=var,value=1)
r1.place(relx=0.55,rely=0.7)
r2=Radiobutton(win,text="Female",font=label_font,variable=var,value=2)
r2.place(relx=0.65,rely=0.7)

label_font=font.Font(weight="bold",family="Times New Roman",size=20)
c=Label(win,text="country",font=label_font)
c.place(relx=0.25,rely=0.8)
c1=ttk.Combobox(win,values=["India","USA","Australia","Europe","Island"])
c1.place(relx=0.55,rely=0.8,width=150,height=30)


def insert():
    connection=mysql.connect(host="localhost",password="livewire",database="studentregdb",user="root")
    cursor=connection.cursor()
    s="insert into t1(name,fathername,contact,emailid,address,gender,country) values (%s,%s,%s,%s,%s,%s,%s)"
    t=(e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),var.get(),c1.get())
    cursor.execute(s,t)
    connection.commit()
    messagebox.showinfo("student registration","insert successfully")
    
def update():
    connection=mysql.connect(host="localhost",password="livewire",database="studentregdb",user="root")
    cursor=connection.cursor()
    sql="update t1 set name='"+str(e2.get())+"',fathername='"+str(e3.get())+"',contact='"+str(e4.get())+"',emailid='"+str(e5.get())+"',address='"+str(e6.get())+"',gender='"+str(var.get())+"',country='"+str(c1.get())+"' where sid={}".format(int(e1.get()))
    cursor.execute(sql)
    connection.commit()
    messagebox.showinfo("student registration","update successfully")

def delete():
    connection=mysql.connect(host="localhost",password="livewire",database="studentregdb",user="root")
    cursor=connection.cursor()
    sql="delete from t1 where sid={}".format(int(e1.get()))
    cursor.execute(sql)
    connection.commit()
    messagebox.showinfo("student registration","Delete successfully")

label_font=font.Font(weight="bold",family="Times New Roman",size=15)

b=Button(win,text="Insert",command=lambda:insert(),font=label_font,bg="green")
b.place(relx=0.30,rely=0.9)
b1=Button(win,text="UPDATE",command=lambda:update(),font=label_font,bg="red")
b1.place(relx=0.40,rely=0.9)
b2=Button(win,text="DELETE",command=lambda:delete(),font=label_font,bg="sky blue")
b2.place(relx=0.53,rely=0.9)

win.mainloop()