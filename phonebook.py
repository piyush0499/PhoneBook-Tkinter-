try:
    from Tkinter import *
except:
    from tkinter import *
from datetime import date
from tkMessageBox import *
import sqlite3
from edit_piyush import *
from search_piyush import *
from first_page import *



con=sqlite3.Connection('project')
cur=con.cursor()
root=Tk()
root.title('Phone Directory')
root["bg"]="purple"

cur.execute("create table if not exists Phonebo(cid integer primary key autoincrement,fname varchar(40),mname varchar(40),lname varchar(40),comp_name varchar(40) ,address varchar(40),city varchar(40),pin number(6),webs varchar(40),dob date,phone_type varchar(10),phone number(10),email_type varchar(10),email varchar(40))")
            

imag=PhotoImage(file='piyush_im_gif.gif')
Label(root,image=imag).grid(row=0,column=2)


i=3 
j=0
Label(root,text='First Name',font='Times 17 bold',fg='black',bg='purple').grid(row=i,column=j)
ent1=Entry(root)
ent1.grid(row=i,column=j+2)

i=i+1
j=0
Label(root,text='Middle Name',font='Times 17 bold',fg='black',bg='purple').grid(row=i,column=j)
ent2=Entry(root)
ent2.grid(row=i,column=j+2)

i=i+1
j=0
Label(root,text='Last Name',font='Times 17 bold',fg='black',bg='purple').grid(row=i,column=j)
ent3=Entry(root)
ent3.grid(row=i,column=j+2)

i=i+1
j=0
Label(root,text='Company Name',font='Times 17 bold',fg='black',bg='purple').grid(row=i,column=j)
ent4=Entry(root)
ent4.grid(row=i,column=j+2)

i=i+1
j=0
Label(root,text='Address',font='Times 17 bold',fg='black',bg='purple').grid(row=i,column=j)
ent5=Entry(root)
ent5.grid(row=i,column=j+2)

i=i+1
j=0
Label(root,text='City',font='Times 17 bold',fg='black',bg='purple').grid(row=i,column=j)
ent6=Entry(root)
ent6.grid(row=i,column=j+2)

i=i+1
j=0
Label(root,text='Pin Code',font='Times 17 bold',fg='black',bg='purple').grid(row=i,column=j)
ent7=Entry(root)
ent7.grid(row=i,column=j+2)

i=i+1
j=0
Label(root,text='Website URL',font='Times 17 bold',fg='black',bg='purple').grid(row=i,column=j)
ent8=Entry(root)
ent8.grid(row=i,column=j+2)

i=i+1
j=0
Label(root,text='Date of Birth',font='Times 17 bold',fg='black',bg='purple').grid(row=i,column=j)
ent9=Entry(root)
ent9.grid(row=i,column=j+2)

i=i+1
j=0
Label(root,text='Select PhoneType',font='Times 17 bold',fg='dark green',bg='purple').grid(row=i,column=j)
val1=IntVar()
Radiobutton(root,text='Office',font='Times 17 bold',variable=val1,value=1,fg='dark green',bg='purple').grid(row=i,column=j+2)
Radiobutton(root,text='Home',font='Times 17 bold',variable=val1,value=2,fg='dark green',bg='purple').grid(row=i,column=j+3)
Radiobutton(root,text='Mobile',font='Times 17 bold',variable=val1,value=3,fg='dark green',bg='purple').grid(row=i,column=j+5)

i=i+1
j=0
Label(root,text='Phone Number',font='Times 17 bold',fg='black',bg='purple').grid(row=i,column=j)
ent10=Entry(root)
ent10.grid(row=i,column=j+2)

Button(root,text='+').grid(row=i,column=j+4)

i=i+1
j=0
Label(root,text='Select Email Type',font='Times 17 bold',fg='dark green',bg='purple').grid(row=i,column=j)
val2=IntVar()
Radiobutton(root,text='Office',font='Times 17 bold',variable=val2,value=1,fg='dark green',bg='purple').grid(row=i,column=j+2)
Radiobutton(root,text='Personal',font='Times 17 bold',variable=val2,value=2,fg='dark green',bg='purple').grid(row=i,column=j+3)

i=i+1
j=0
Label(root,text='Email Id',font='Times 17 bold',fg='black',bg='purple').grid(row=i,column=j)
ent11=Entry(root)
ent11.grid(row=i,column=j+2)

Button(root,text='+').grid(row=i,column=j+4)

l=['0','1','2','3','4','5','6','7','8','9']

def save():
    qa=0
    qa1=0
    qa2=0
    qa3=0
    qa4=0
    e1=ent1.get()
    e2=ent2.get()
    e3=ent3.get()
##    if e1==e2 and e2==e3:
##        qa=1
##        showerror('error','fname,mname and lname all cannot be same')
        #showerror('error','same')
    try:
        assert (not(e1==e2 and e2==e3)),"fname,mname and lname all cannot be same"
    except AssertionError as error:
        showerror('error',error)
        
    e4=ent4.get()
    e5=ent5.get()
    e6=ent6.get()
    va=0
    for v in ent7.get():
        if v not in l:
            va=1
            break
    if va==1 or len(ent7.get())!=6:
        qa1=1
        showerror('error','pin must be a no of 6 digits')
    if qa1==0:
        e7=int(ent7.get())
    e8=ent8.get()
    e9=ent9.get()
    to = date.today()
    #cur.execute(select substr(e9,7)
    u=e9[6:]
    ye=to.year
    if int(ye)-int(u)<18:
        qa2=1
        showerror('error','Check required age,either you are below 18 or your dob cannot be tracked.')
    e10=int(val1.get())
    if e10==1:
        j='Office'
    elif e10==2:
        j='Home'
    elif e10==3:
        j='Mobile'
    ta=0
    for t in ent10.get():
        if t not in l:
            ta=1
            break
    if ta==1 or len(ent10.get())!=10:
        qa3=1
        showerror('error','phone must be a no of 10 digits')
    if qa3==0:
        e11=int(ent10.get())
    e12=int(val2.get())
    if e12==1:
        m='Office'
    elif e12==2:
        m='Personal'
    e13=ent11.get()
    rt=0
    for r in ent11.get():
        if r=='@':
            rt=rt+1
    if rt==0 or rt>1:
        qa4=1
        showerror('error','@ shall occur once in email')
    

    if qa==0 and qa1==0 and qa2==0 and qa3==0 and qa4==0:
        ent1.delete(0,END)
        ent2.delete(0,END)
        ent3.delete(0,END)
        ent4.delete(0,END)
        ent5.delete(0,END)
        ent6.delete(0,END)
        ent7.delete(0,END)
        ent8.delete(0,END)
        ent9.delete(0,END)
        ent10.delete(0,END)
        ent11.delete(0,END)
        cur.execute("insert into Phonebo(fname,mname,lname,comp_name,address,city,pin,webs,dob,phone_type,phone,email_type,email) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(e1,e2,e3,e4,e5,e6,e7,e8,e9,j,e11,m,e13))
        con.commit()
        showinfo('info','Contact Saved')
            
    
            
                
                
            
                
        
        
    

def Close():
    #cur.execute("select * from Phonebo")
    #print(cur.fetchall())
    root.destroy()


Button(root,text='Save',font='Times 14 bold',command=save).grid(row=17,column=1)
Button(root,text='Search',font='Times 14 bold',command=sear).grid(row=17,column=2)
Button(root,text='Close',font='Times 14 bold',command=Close).grid(row=17,column=3)
Button(root,text='Edit',font='Times 14 bold',command=edit).grid(row=17,column=5)

root.mainloop()
