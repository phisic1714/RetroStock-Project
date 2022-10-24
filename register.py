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
def confirm():
    try:
        auth.create_user_with_email_and_password(email.get(),password.get())
        db=firestore.client()
        db.collection('User').add({'email':email.get(),'password':password.get(),'type':'normal'})
        win.destroy()
        subprocess.call(["python", "main.py"])
        
    except:
        Label(win, text='Email already Exist! or Your Email and Password incorect',bg='red',fg='yellow',font=('Times 13')).place(x=130,y=245)

def cancle ():
    win.destroy()

win = Tk()
win.geometry("630x530")
win.resizable(0, 0)
win.title('Retro Stock')
win.iconbitmap(r'image/logo.ico')
win.option_add('*Font', 'times 20')
bg = PhotoImage(file = "image/bg2.png")
img1 = ImageTk.PhotoImage(Image.open("image/logo.png"))  
img2=ImageTk.PhotoImage(Image.open("image/register.png"))  
canvas = Canvas(win, width = 650, height = 530)  
canvas.pack()
canvas.create_image( win.winfo_width()/2, win.winfo_height()/2, image = bg, anchor = CENTER)
canvas.create_image(win.winfo_width()/2, 450, anchor=CENTER, image=img1)  

canvas.create_image(win.winfo_width()/2, 50, anchor=CENTER, image=img2)
email =StringVar()
password=StringVar()
conf_password=StringVar()
p=30
Label(win, text='New Email',bg='light green').place(x=50,y=70+p)
Label(win, text='New Password',bg='light green').place(x=50,y=120+p)
Label(win, text='Confirm Password',bg='light green').place(x=50,y=170+p)
Entry(win,textvariable=email,width=20).place(x=290,y=70+p)
Entry(win,show="*",textvariable=password,width=20).place(x=290,y=120+p)
Entry(win,show="*",textvariable=conf_password,width=20).place(x=290,y=170+p)
Button(win,text='Confirm',command=confirm).place(x=150,y=250+p)
Button(win,text='Cancle',command=cancle).place(x=350,y=250+p)
win.configure(bg='black')
win.mainloop()