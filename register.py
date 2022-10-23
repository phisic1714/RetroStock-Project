from distutils.log import error
import subprocess
import time
from tkinter import *
from tkinter import ttk
from token import EQUAL
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
def confirm():
    try:
        auth.create_user_with_email_and_password(email.get(),password.get())
        win.destroy()
        subprocess.call(["python", "main.py"])
    except:
        error=Label(win, text='Email already Exist! or Your Email and Password incorect',fg='red',font=('Times 13')).place(x=130,y=245)
        error.after(1000, error.master.destroy())



win = Tk()
win.geometry("630x530")
win.resizable(0, 0)
win.title('Retro Stock')
win.iconbitmap(r'image/logo.ico')
win.option_add('*Font', 'times 20')
canvas = Canvas(win, width = 650, height = 530, bg='black')  
canvas.pack()
img = ImageTk.PhotoImage(Image.open("image/logo.png"))  
canvas.create_image(win.winfo_width()/2, 450, anchor=CENTER, image=img)   
email =StringVar()
password=StringVar()
conf_password=StringVar()
p=30
Label(win, text='New Email').place(x=50,y=70+p)
Label(win, text='New Password').place(x=50,y=120+p)
Label(win, text='Confirm Password').place(x=50,y=170+p)
Entry(win,textvariable=email,width=20).place(x=290,y=70+p)
Entry(win,show="*",textvariable=password,width=20).place(x=290,y=120+p)
Entry(win,show="*",textvariable=conf_password,width=20).place(x=290,y=170+p)
Button(win,text='Confirm',command=confirm).place(x=270,y=250+p)
win.configure(bg='black')
win.mainloop()