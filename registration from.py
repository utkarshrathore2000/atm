import sqlite3
from tkinter import *
db=sqlite3.connect('registration')
obj=db.cursor()
root = Tk()
root.geometry("432x235")
root.title("utkarsh GYM")
class tt:
    Label(root, text="Name",padx=20,font='lusida 12 bold').grid(row=0)
    Label(root, text="Age",padx=20,font='lusida 12 bold').grid(row=1)
    Label(root, text="mobile",padx=20,font='lusida 12 bold').grid(row=2)
    Label(root, text="join",font='lusida 12 bold').grid(row=3)

    def values():
          global name,age,mob,join
          n=name.get()
          a=age.get()
          m=mob.get()
          j=join.get()
          obj.execute('create table if not exists gym(name TEXT,age INTEGER,mobile INTEGER,joining_date TEXT)')
          sql='insert into gym values(?,?,?,?)'
          val=[n,a,m,j]
          db.commit()
          obj.execute('select *from gym')
          obj.execute(sql,val)
          i=obj.fetchall()
          print(i)
    global name,age,mob,join
    name = StringVar()
    age = StringVar()
    mob = StringVar()
    join = StringVar()
    foodservice=IntVar()
    nameentry = Entry(root,textvariable=name)
    ageentry = Entry(root,textvariable=age)
    mobentry = Entry(root,textvariable=mob)
    joinentry = Entry(root,textvariable=join)
    nameentry.grid(row=0,column=1)
    ageentry.grid(row=1,column=1)
    mobentry.grid(row=2,column=1)
    joinentry.grid(row=3,column=1)
    s=Checkbutton(text='are you sure',variable=foodservice)
    s.grid(row=3,column=2)
    Button(text="Submit",bg='red',font='lusida 15 bold',padx=20,command=values).grid(column=1)
    root.mainloop()
db.close()
    



