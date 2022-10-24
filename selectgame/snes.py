from tkinter import *
from PIL import ImageTk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import webbrowser



cred = credentials.Certificate("retrostock-project-firebase-adminsdk-upta5-aaead3d509.json")
firebase_admin.initialize_app(cred)
   
# Create an instance of Tkinter Frame
win = Tk()

# Set the geometry of Tkinter Frame
win.geometry("1080x610")
win.resizable(0, 0)
win.title('Retro Stock')
win.option_add('*Font', 'times 20')
bg =  ImageTk.PhotoImage( file = "image/10804297.png")
# Show image using label
label1 = Label( win, image = bg)
label1.place(x = 0,y = 0)
#webbrowser.open_new('https://www.retrogames.cc/embed/43388-super-bomberman-5-english-translated.html')
# Open the Image File
db=firestore.client()
   #db.collection('Game').add({'name':name.get(),'game':game.get(),'image':image.get()})
def pressed(g):
   db.collection('currentGame').add(g)
doc=db.collection('Game').where('type','==','snes').get()
m=0
n=0
for docs in doc :
   def g (x=docs.to_dict()):
      return pressed(x)
   n=n+1
   m=m+250
   Button(win,text=docs.to_dict()['name'],command=g).pack(side=LEFT,expand=YES)
   

win.mainloop()