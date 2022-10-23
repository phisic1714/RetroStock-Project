# Import the required libraries
from ctypes import resize
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tkhtmlview import HTMLLabel



cred = credentials.Certificate("retrostock-project-firebase-adminsdk-upta5-aaead3d509.json")
firebase_admin.initialize_app(cred)
def pressed():
   db=firestore.client()
   #db.collection('Game').add({'name':name.get(),'game':game.get(),'image':image.get()})
   for widgets in win.winfo_children():
      widgets.destroy()
   doc=db.collection('Game').get()
   m=0
   for docs in doc :
      Label(win, text=docs.to_dict()['name']).place(x=m,y=70)
      my_label = HTMLLabel(win, html=f"""
        <img src="{docs.to_dict()['image']}" alt="Flowers in Chania width="200" height="200">

    """).place(x=m,y=100)
      m=m+50

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

# Open the Image File
win.mainloop()
