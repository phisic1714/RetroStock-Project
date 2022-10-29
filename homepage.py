from tkinter import *
from PIL import ImageTk, Image
import subprocess
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
cred = credentials.Certificate("retrostock-project-firebase-adminsdk-upta5-aaead3d509.json")
firebase_admin.initialize_app(cred)
db=firestore.client()
user=db.collection('currentUser').get()
for users in user :
   userinfo=users.to_dict()


win = Tk()
win.geometry('1080x610')
win.title('Retro Stock')
win.iconbitmap(r'image/logo.ico')
win['bg']='#ccff99'

def close():
    doc=db.collection('currentUser').get()
    for docs in doc :
        db.collection('currentUser').document(docs.id).delete()
    win.destroy()

win.protocol("WM_DELETE_WINDOW", close)

def snes():
    win.destroy()
    subprocess.call(["python","selectgame/snes.py"])    

def nes():
    win.destroy()
    subprocess.call(["python","selectgame/nes.py"])

def gba():
    win.destroy()
    subprocess.call(["python","selectgame/gba.py"])

label1=Label(win,text="HOME",padx=1080,pady=35,font=90,bg="#ff9966")#.grid(row=0,column=0)
label1.pack()

bt1=Button(win,text="SNES",height=2,width=15,command=snes)#.grid(row=4,column=1)
bt1.pack(side=LEFT,expand=YES)

bt2=Button(win,text="NES",height=2,width=15,command=nes)#.grid(row=4,column=2)
bt2.pack(side=LEFT,expand=YES)

bt3=Button(win,text="GBA",height=2,width=15,command=gba)#.grid(row=4,column=3)
bt3.pack(side=LEFT,expand=YES)

def userlibraly():
   win.destroy()
   subprocess.call(["python", "user/libraly.py"])
userlogo =  ImageTk.PhotoImage( file = "image/userlogo.png")
if userinfo['email'] != 'guest':
   Button(win,image=userlogo,bg='#158bdc',command=userlibraly).place(x = 960,y = 20)

def back():
   doc=db.collection('currentUser').get()
   for docs in doc :
      db.collection('currentUser').document(docs.id).delete()
   win.destroy()
   subprocess.call(["python", "main.py"])
backlogo =  ImageTk.PhotoImage( file = "image/back.png")
Button(win,image=backlogo,bg='black',command=back).place(x = 40,y = 20)


win.mainloop()    


    