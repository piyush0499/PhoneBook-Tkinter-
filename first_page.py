from Tkinter import *
wid=Tk()
wid.geometry('550x300')
Label(wid,text='PROJECT TITLE : PhoneBook',font='Times 20 bold',fg='black').grid(row=2,column=1)
Label(wid,text='PYTHON DATABASE PROJECT',font='Times 20 bold',fg='tan1').grid(row=6,column=1)
Label(wid,text='DEVELOPED BY : PIYUSH DIKSHIT',font='Times 20 bold',fg='red').grid(row=10,column=1)
Label(wid,text='En No : 181B143',font='Times 20 bold',fg='red').grid(row=14,column=1)
Label(wid,text='Batch : B5',font='Times 20 bold',fg='red').grid(row=18,column=1)
Label(wid,text='press key to close',font='Times 20 bold',fg='black').grid(row=22,column=1)

def close1(e=1):
    wid.destroy()

wid.bind('<KeyPress>',close1)
wid.mainloop()
