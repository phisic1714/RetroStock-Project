import subprocess
from tkinter import *
from PIL import ImageTk, Image
from plyer import notification
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin

cred = credentials.Certificate(
    "retrostock-project-firebase-adminsdk-upta5-aaead3d509.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def ok():

    User = db.collection('User').where('email', '==', email.get()).stream()
    for users in User:
        user = users.to_dict()
    try:
        password = user['password']
        mail = user['email']
        for widgets in win.winfo_children():
            widgets.destroy()
        Label(win, text='Complete!! \nPlease Check Your PC Notification',
              bg='green', fg='yellow').place(x=40, y=100)
        notification.notify(
            title=f'Hello {mail}', message=f'Your password is {password}', app_icon='image/logo.ico',ticker='Retro Stock',timeout=30)
        win.after(3000,lambda:close())
        
    except:
        Label(win, text='Your Email does not Exist',
              bg='red', fg='yellow').place(x=50, y=120)

win = Tk()
win.geometry("530x260")
win.resizable(0, 0)
win.title('Retro Stock')
win.iconbitmap(r'image/logo.ico')
win.option_add('*Font', 'times 20')
canvas = Canvas(win, width = 1080, height = 610, bg='light blue')  
canvas.pack()

fgpass=ImageTk.PhotoImage(Image.open("image/fgpass.png"))  
canvas.create_image(win.winfo_width()/2, 50, anchor=CENTER, image=fgpass)

def close():
    win.destroy()
    subprocess.call(["python", "main.py"])
    
win.protocol("WM_DELETE_WINDOW", close)

email = StringVar()
Label(win, text='Email', bg='light blue').place(x=50, y=70)
Entry(win, textvariable=email, width=20).place(x=190, y=70)
Button(win, text='OK', bg='light green', command=ok).place(x=220, y=170)

win['bg'] = 'light blue'

win.mainloop()
