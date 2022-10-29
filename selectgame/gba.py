from ast import Lambda
from distutils.command.config import config
import subprocess
from tkinter import *
import tkinter
from tkinter import ttk
from urllib.request import urlopen
from PIL import ImageTk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("retrostock-project-firebase-adminsdk-upta5-aaead3d509.json")
firebase_admin.initialize_app(cred)
db=firestore.client()
doc=db.collection('Game').where('type','==','gba').get()
user=db.collection('currentUser').get()
for users in user :
   userinfo=users.to_dict()

win = Tk()
win.geometry("1080x610")
win.resizable(0, 0)
win.title('Retro Stock')
win.iconbitmap(r'image/logo.ico')
win.option_add('*Font', 'times 20')

main_frame=Frame(win)
main_frame.pack(fill=BOTH,expand=1)
my_canvas=Canvas(main_frame)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
second_frame= Frame(my_canvas,bg='#414a75',)
my_canvas.create_window((0,0),window=second_frame,anchor="nw")

def close():
    db.collection('currentUser').document(users.id).delete()
    win.destroy()

win.protocol("WM_DELETE_WINDOW", close)


bg =  ImageTk.PhotoImage( file = "image/gba.jpg")
Label( second_frame, image = bg).place(x = 0,y = 0)
my_canvas.create_image(0, 0, anchor=NW, image=bg)

def userlibraly():
   win.destroy()
   subprocess.call(["python", "user/libraly.py"])
userlogo =  ImageTk.PhotoImage( file = "image/userlogo.png")
if userinfo['email'] != 'guest':
   Button(second_frame,image=userlogo,bg='#158bdc',command=userlibraly).place(x = 960,y = 20)

def back():
   win.destroy()
   subprocess.call(["python", "homepage.py"])
backlogo =  ImageTk.PhotoImage( file = "image/back.png")
Button(second_frame,image=backlogo,bg='black',command=back).place(x = 40,y = 20)

def pressed(g):
   db.collection('currentGame').add(g)
   subprocess.call(["python", "game.py"])
c=0
r=0
phostolistpos=0
photo=[]
for docs in doc :
   c+=1
   def g (x=docs.to_dict()):
      return pressed(x)
   raw_data = urlopen(docs.to_dict()['image']).read()
   image = ImageTk.PhotoImage(data=raw_data)
   photo.append(image)
   Button(second_frame,image=photo[phostolistpos],bg = "light green",command=g).grid(row=r,column=c,sticky = N, pady = 100,padx = 50)
   if c % 3 == 0:
      c=0
      r+=1
   phostolistpos+=1


win.mainloop()