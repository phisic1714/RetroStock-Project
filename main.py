import subprocess
from tkinter import *
from PIL import ImageTk, Image
import pyrebase
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin

cred = credentials.Certificate("retrostock-project-firebase-adminsdk-upta5-aaead3d509.json")
firebase_admin.initialize_app(cred)
firebaseConfig = {
    "apiKey": "AIzaSyAwtDfLH6G8RLw0jbMMW6msQ3viHrWjV6A",
    "authDomain": "retrostock-project.firebaseapp.com",
    "projectId": "retrostock-project",
    "storageBucket": "retrostock-project.appspot.com",
    "messagingSenderId": "717936259204",
    "appId": "1:717936259204:web:2b33eaee529c4fac09d2d1",
    "measurementId": "G-72PWHSCVVL",
    "databaseURL":""
  }
firebase = pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()
db=firestore.client()

User=db.collection('User').get()

def login ():
   try:
      auth.sign_in_with_email_and_password(email.get(),password.get())
      doc=db.collection('User').where('email','==',email.get()).stream()
      for docs in doc :
         userinfo=docs.to_dict()
      db.collection('currentUser').add(userinfo)
      win.destroy()
      subprocess.call(["python", "homepage.py"])
      
   except:
        Label(win, text='Your Email and Password incorect.',bg='red',fg='yellow',font=('Times 13')).place(x=117,y=235)

def guest():
   db.collection('currentUser').add({'email':'guest'})
   win.destroy()
   subprocess.call(["python", "homepage.py"])

def register ():
   subprocess.call(["python", "user/register.py"])

def about_us():
   subprocess.call(["python", "about_us.py"])
   
def forgot():
   subprocess.call(["python", "user/forgotPassword.py"])

win = Tk()
win.geometry("530x580")
win.resizable(0, 0)
win.title('Retro Stock')
win.iconbitmap(r'image/logo.ico')
win.option_add('*Font', 'times 20')
canvas = Canvas(win, width = 530, height = 580, bg='black')  
canvas.pack()
bg = PhotoImage(file = "image/bg1.png")
img1 = ImageTk.PhotoImage(Image.open("image/logo.png")) 
img2=ImageTk.PhotoImage(Image.open("image/login.png"))  
img3=ImageTk.PhotoImage(Image.open("image/aboutus.png"))  
canvas.create_image( win.winfo_width()/2, win.winfo_height()/2, image = bg, anchor = CENTER)
canvas.create_image(win.winfo_width()/2, 500, anchor=CENTER, image=img1)   
canvas.create_image(win.winfo_width()/2, 50, anchor=CENTER, image=img2)

email =StringVar()
password=StringVar()
if User == None :
   email.set('')
   password.set('')
else:
   for users in User :
      userinfo=users.to_dict()
      email.set(userinfo['email'])
      password.set(userinfo['password'])

Label(win, text='Email').place(x=50,y=100)
Label(win, text='Password').place(x=50,y=150)
Entry(win,textvariable=email,width=20).place(x=200,y=100)
Entry(win,show="*",textvariable=password,width=20).place(x=200,y=150)
Button(win,text='Login',command=login,bg='green',fg='white').place(x=130,y=280)
Button(win,text='Guest',command=guest,bg='yellow').place(x=300,y=280)
Button(win,text='Register',command=register,bg='blue',fg='white').place(x=203,y=350)
Button(win,image=img3,command=about_us,bg='#147444',fg='white').place(x=450,y=500)
forgot=Label(win, text='Forgot Password? Click Me !!',fg='blue',bg='white',font=('Times 13'))
forgot.place(x=240,y=195)
forgot.bind('<Button-1>',lambda e :subprocess.call(["python", "user/forgotPassword.py"]))
forgot.bind('<Enter>',lambda e :forgot.config(bg='black'))
forgot.bind('<Leave>',lambda e :forgot.config(bg='white'))

win.mainloop()