import subprocess
from tkinter import *
from urllib.request import urlopen
import webbrowser
from PIL import ImageTk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("retrostock-project-firebase-adminsdk-upta5-aaead3d509.json")
firebase_admin.initialize_app(cred)
db=firestore.client()
doc=db.collection('currentGame').get()
for games in doc :
   game=games.to_dict()
user=db.collection('currentUser').get()
for users in user :
   userinfo=users.to_dict()

win = Tk()
win.geometry("1080x610")
win.resizable(0, 0)
win.title('Retro Stock')
win.iconbitmap(r'image/logo.ico')
win.option_add('*Font', 'times 20')


def close():
   doc=db.collection('currentGame').get()
   for docs in doc :
      db.collection('currentGame').document(docs.id).delete()
   win.destroy()

win.protocol("WM_DELETE_WINDOW", close)


bg =  ImageTk.PhotoImage( file = "image/play.jpg")
Label( win, image = bg).place(x = 0,y = 0)

def userlibraly():
   doc=db.collection('currentGame').get()
   for docs in doc :
      db.collection('currentGame').document(docs.id).delete()
   win.destroy()
   subprocess.call(["python", "user/libraly.py"])
userlogo =  ImageTk.PhotoImage( file = "image/userlogo.png")
if userinfo['email'] != 'guest':
   Button(win,image=userlogo,bg='#158bdc',command=userlibraly).place(x = 960,y = 20)

backlogo =  ImageTk.PhotoImage( file = "image/back.png")
Button(win,image=backlogo,bg='black',command=close).place(x = 40,y = 20)

def playpress():
   webbrowser.open(games.to_dict()['game'])

def savepress():
   usersavegame=db.collection('User').get()
   for usersavegames in usersavegame :
      if usersavegames.to_dict()['email']==userinfo['email']:
         db.collection('User').document(usersavegames.id).update({'collection':firestore.ArrayUnion([game['id']])})
         db.collection('currentUser').document(users.id).update({'collection':firestore.ArrayUnion([game['id']])})
      close()

def unsavepress():
   usersavegame=db.collection('User').get()
   for usersavegames in usersavegame :
      usersavegamenum=len(usersavegames.to_dict()['collection'])
      if usersavegames.to_dict()['email']==userinfo['email']  :
         for x in range(usersavegamenum):
           if usersavegames.to_dict()['collection'][x]==game['id']:
             db.collection('User').document(usersavegames.id).update({'collection':firestore.ArrayRemove([game['id']])})
             db.collection('currentUser').document(users.id).update({'collection':firestore.ArrayRemove([game['id']])})
             close()
             break

gamename=game['name']
gameplatform=game['type']
raw_data = urlopen(game['image']).read()
image = ImageTk.PhotoImage(data=raw_data)
Label(win,image=image, bg = "red").place(x = 100,y = 150)
Label(win,text=f'Name: {gamename}',font=("Arial", 25)).place(x = 550,y = 150)
Label(win,text=f'Platform: {gameplatform}',font=("Arial", 25)).place(x = 550,y = 250)
Button(win,text='Play', bg = "light blue",height = 2,width = 6,command=playpress).place(x = 550,y = 350)

if users.to_dict()['email']!='guest':
   num=len(users.to_dict()['collection'])
   Savebutton=Button(win,text='Save', bg = "yellow",height = 2,width = 6,command=savepress)
   for user_mains in range(num) :
         if users.to_dict()['collection'][user_mains]==game['id'] :
            Savebutton=Button(win,text='Unsave', bg = "red",height = 2,width = 6,command=unsavepress)
            break
   Savebutton.place(x = 750,y = 350)

def about_us():
   subprocess.call(["python", "about_us.py"])
about_us_logo =  ImageTk.PhotoImage( file = "image/aboutus.png")
Button(win,image=about_us_logo,bg='#147444',command=about_us).place(x = 960,y = 530)

win.mainloop()