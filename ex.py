import subprocess
from tkinter import *
from PIL import ImageTk, Image
import pyrebase
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin

cred = credentials.Certificate("retrostock-project-firebase-adminsdk-upta5-aaead3d509.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

def ok() :
    try:
        User=db.collection('User').where('email','==',email.get()).stream()
        for users in User:
            trueuser=users.to_dict()
    except:
        Label(win, text='Your Email does not Exist',bg='red',fg='yellow',font=('Times 13')).place(x=50,y=100)


win = Tk()
win.geometry("530x530")
win.resizable(0, 0)
win.title('Retro Stock')
win.iconbitmap(r'image/logo.ico')
win.option_add('*Font', 'times 20')
email =StringVar()

Label(win, text='Email').place(x=50,y=100)
Entry(win,textvariable=email,width=20).place(x=200,y=100)
Button(win,text='OK',bg='light green',command=ok).place(x=220,y=200)

win.mainloop()