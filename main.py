# Import the required libraries

import subprocess
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import pyrebase
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

def login ():
   auth.sign_in_with_email_and_password(email.get(),password.get())
   win.destroy()
   subprocess.call(["python", "game.py"])
def register ():
   win.destroy()
   subprocess.call(["python", "register.py"])

win = Tk()
win.geometry("530x450")
win.resizable(0, 0)
win.title('Retro Stock')
win.iconbitmap(r'image/logo.ico')
win.option_add('*Font', 'times 20')
canvas = Canvas(win, width = 530, height = 450, bg='black')  
canvas.pack()
img = ImageTk.PhotoImage(Image.open("image/logo.png"))  
canvas.create_image(win.winfo_width()/2, 370, anchor=CENTER, image=img)   
email =StringVar()
password=StringVar()
p=30
Label(win, text='Email').place(x=50,y=70+p)
Label(win, text='Password').place(x=50,y=120+p)
Entry(win,textvariable=email,width=20).place(x=200,y=70+p)
Entry(win,show="*",textvariable=password,width=20).place(x=200,y=120+p)
Button(win,text='Login',command=login).place(x=130,y=200+p)
Button(win,text='Register',command=register).place(x=300,y=200+p)
win.mainloop()