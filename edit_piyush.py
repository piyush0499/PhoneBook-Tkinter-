#importing libraries
from Tkinter import *
import sqlite3
from tkMessageBox import *

#Linking the database
con=sqlite3.Connection('project')
cur=con.cursor()
#root=Tk()

def edit():
    ro=Tk()
    ro.title('Editing..')
    Label(ro,text="Enter name to edit",font='Arial20',fg='blue').grid(row=0,column=0)
    c=Entry(ro)
    c.grid(row=1,column=0)
    
    def edit_1():
        roi=Tk()
        roi.title('Editing Page')
        ans=(c.get()).split(' ')
        print ans
        
        cur.execute('select * from Phonebo where fname=(?) and mname=(?) and lname=(?)',(ans[0],ans[1],ans[2]))
        a=cur.fetchall()
        
        Label(roi,text='Edit the details',font='Times 17 bold',bg='pink',fg='red').grid(row=0,column=2)
        
        Label(roi,text='First Name',font='Times 17 bold',fg='black').grid(row=4,column=0)
        ent1=Entry(roi)
        ent1.grid(row=4,column=3)

        Label(roi,text='Middle Name',font='Times 17 bold',fg='black').grid(row=5,column=0)
        ent2=Entry(roi)
        ent2.grid(row=5,column=3)

        Label(roi,text='Last Name',font='Times 17 bold',fg='black').grid(row=6,column=0)
        ent3=Entry(roi)
        ent3.grid(row=6,column=3)

        Label(roi,text='Company Name',font='Times 17 bold',fg='black').grid(row=7,column=0)
        ent4=Entry(roi)
        ent4.grid(row=7,column=3)

        Label(roi,text='Address',font='Times 17 bold',fg='black').grid(row=8,column=0)
        ent5=Entry(roi)
        ent5.grid(row=8,column=3)

        Label(roi,text='City',font='Times 17 bold',fg='black').grid(row=9,column=0)
        ent6=Entry(roi)
        ent6.grid(row=9,column=3)

        Label(roi,text='Pin Code',font='Times 17 bold',fg='black').grid(row=10,column=0)
        ent7=Entry(roi)
        ent7.grid(row=10,column=3)

        Label(roi,text='Website URL',font='Times 17 bold',fg='black').grid(row=11,column=0)
        ent8=Entry(roi)
        ent8.grid(row=11,column=3)

        Label(roi,text='Date of Birth',font='Times 17 bold',fg='black').grid(row=12,column=0)
        ent9=Entry(roi)
        ent9.grid(row=12,column=3)

        Label(roi,text='Phone type',font='Times 17 bold',fg='red').grid(row=13,column=0)
        ent10=Entry(roi)
        ent10.grid(row=13,column=3)

        Label(roi,text='Phone Number',font='Times 17 bold',fg='black').grid(row=14,column=0)
        ent11=Entry(roi)
        ent11.grid(row=14,column=3)

        Label(roi,text='Email type',font='Times 17 bold',fg='red').grid(row=15,column=0)
        ent12=Entry(roi)
        ent12.grid(row=15,column=3)

        Label(roi,text='Email Id',font='Times 17 bold',fg='black').grid(row=16,column=0)
        ent13=Entry(roi)
        ent13.grid(row=16,column=3)

        ent1.insert(0,a[0][1])
        ent2.insert(0,a[0][2])
        ent3.insert(0,a[0][3])
        ent4.insert(0,a[0][4])
        ent5.insert(0,a[0][5])
        ent6.insert(0,a[0][6])
        ent7.insert(0,a[0][7])
        ent8.insert(0,a[0][8])
        ent9.insert(0,a[0][9])
        ent10.insert(0,a[0][10])
        ent11.insert(0,a[0][11])
        ent12.insert(0,a[0][12])
        ent13.insert(0,a[0][13])

        def ed_sav():

            #cur.execute("select cid from Phonebo where fname=(?) and mname=(?) and lname=(?)",(ans[0],ans[1],ans[2]))
            #s=cur.fetchall()
            #print s
            cur.execute("delete from Phonebo where fname=(?) and mname=(?) and lname=(?)",(ans[0],ans[1],ans[2]))
            con.commit()


    
            
            
            try:
                #cur.execute("Update Phonebo set fname=(?),mname=(?),lname=(?),comp_name=(?),address=(?),city=(?),pin=(?),webs=(?),dob=(?),phone_type=(?),phone=(?),email_type=(?),email=(?) where cid=(?)",(a,b,c,d,e,f,g,h,i,j,k,l,m,s))
                cur.execute("insert into Phonebo(fname,mname,lname,comp_name,address,city,pin,webs,dob,phone_type,phone,email_type,email) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(ent1.get(),ent2.get(),ent3.get(),ent4.get(),ent5.get(),ent6.get(),ent7.get(),ent8.get(),ent9.get(),ent10.get(),int(ent11.get()),ent12.get(),ent13.get()))
                con.commit()
                #cur.execute("select * from abc")
                #print cur.fetchall()
                showinfo('info','edited contact saved')
                roi.destroy()
                ro.destroy()
                
            except(error):
                showerror('error',error)

            
        Button(roi,text="Save",font='Times 15 bold',command=ed_sav).grid(row=18,column=2)
        roi.mainloop()
        
    Button(ro,text="next",font='Times 15 bold',command=edit_1).grid(row=2,column=0)
    ro.mainloop()
