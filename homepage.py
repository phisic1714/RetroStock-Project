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
win.resizable(0, 0)
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
canvas = Canvas(win, width = 1080, height = 610, bg='black')  
canvas.pack()

homebg =  ImageTk.PhotoImage( file = "image/homebg.jpg")
canvas.create_image( win.winfo_width()/2, win.winfo_height()/2, image = homebg, anchor = CENTER)


home=ImageTk.PhotoImage(Image.open("image/home.png"))  
canvas.create_image(win.winfo_width()/2, 50, anchor=CENTER, image=home)

bt1=Button(win,text="SNES",height=2,width=15,bg='#9495cb',command=snes)#.grid(row=4,column=1)
bt1.place(x=150,y=450)

bt2=Button(win,text="NES",height=2,width=15,bg='#921b1b',fg='yellow',command=nes)#.grid(row=4,column=2)
bt2.place(x=500,y=450)

bt3=Button(win,text="GBA",height=2,width=15,bg='#414a75',fg='white',command=gba)#.grid(row=4,column=3)
bt3.place(x=850,y=450)

img = Image.open("image/SNES.png")
img =img.resize((int(img.width*.4),int(img.height*.4)))
photo = ImageTk.PhotoImage(img)
label2=Label(image=photo,bg='#ccff99')
label2.place(x=40,y=150)

img1 = Image.open("image/NESBG.png")
img1 =img1.resize((int(img1.width*.4),int(img1.height*.4)))
photo1 = ImageTk.PhotoImage(img1)
label3=Label(image=photo1,bg='#ccff99')
label3.place(x=400,y=150)

img2 = Image.open("image/GBC.png")
img2 =img2.resize((int(img2.width*1),int(img2.height*1)))
photo2 = ImageTk.PhotoImage(img2)
label4=Label(image=photo2,bg='#ccff99')
label4.place(x=800,y=150)

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

def about_us():
   subprocess.call(["python", "about_us.py"])
about_us_logo =  ImageTk.PhotoImage( file = "image/aboutus.png")
Button(win,image=about_us_logo,bg='#147444',command=about_us).place(x = 960,y = 530)

win.mainloop()    


    