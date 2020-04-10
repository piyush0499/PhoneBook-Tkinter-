from Tkinter import *
import sqlite3
from tkMessageBox import *

con=sqlite3.Connection('project')
cur=con.cursor()

def sear():
    
    def sear_1(ev):
        
        h=ev.char
        word=str(ent.get())
        #print word
    
        lisb.delete(0,END)
        cur.execute("select fname,mname,lname,phone from Phonebo where fname like '%{}%' or mname like '%{}%' or lname like '%{}%' or phone like '{}%'".format(word,word,word,word))
        match_it=cur.fetchall()
        count=0
        
        for i in match_it:
            lisb.insert(count,i)
            count+=1

        def sear_2(eve):
            
            def sear_del():
                
                cur.execute("delete from Phonebo where fname = (?) and mname=(?) and lname=(?)",(curr_val1,curr_val2,curr_val3))
                con.commit()
                showinfo('Info','selected contact deleted')
                rok.destroy()
                
            val=lisb.get(lisb.curselection())
            curr_val1=val[0]
            curr_val2=val[1]
            curr_val3=val[2]
            lisb.delete(0,END)
            cur.execute("select * from Phonebo where fname = (?) and mname=(?)and lname=(?)",(curr_val1,curr_val2,curr_val3))
            Info=cur.fetchall()
            
            lisb.insert(END,'First Name : '+str(Info[0][1]))
            lisb.insert(END,'Middle Name : '+str(Info[0][2]))
            lisb.insert(END,'Last Name : '+str(Info[0][3]))
            lisb.insert(END,'Company Name : '+str(Info[0][4]))
            lisb.insert(END,'Address : '+str(Info[0][5]))
            lisb.insert(END,'City : '+str(Info[0][6]))
            lisb.insert(END,'Pin Code : '+str(Info[0][7]))
            lisb.insert(END,'website : '+str(Info[0][8]))
            lisb.insert(END,'DOB : '+str(Info[0][9]))
            lisb.insert(END,'Phone type : '+str(Info[0][10]))
            lisb.insert(END,'Phone no : '+str(Info[0][11]))
            lisb.insert(END,'email type : '+str(Info[0][12]))
            lisb.insert(END,'email : '+str(Info[0][13]))
            
            Button(rok,text="delete",font='Times 15 bold',command=sear_del).grid(row=4,column=3)  
            
        lisb.bind('<<ListboxSelect>>',sear_2)

    rok=Tk()
    rok.title('Search Page')
    rok["bg"]="silver"
    Label(rok,text='Searching from PhoneBook',font='Times 17 bold',bg='pink',fg='red').grid(row=0,column=1)
    Label(rok,text='Enter Name or Phone no:',font='Times 15 bold',bg='pink',fg='blue').grid(row=2,column=0)
    ent=Entry(rok)
    ent.grid(row=2,column=1)
    lisb=Listbox(rok,height=15,width=50,font="Times 15 bold",fg="tan4",selectmode=SINGLE)
    
      
    lisb.grid(row=3,column=1)
    rok.bind('<KeyPress>',sear_1)
    
    def close():
        rok.destroy()
    Button(rok,text='Close',font='Times 15 bold',command=close).grid(row=4,column=1)
    rok.mainloop()
