from tkinter import *
from plyer import notification
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin

cred = credentials.Certificate(
    "retrostock-project-firebase-adminsdk-upta5-aaead3d509.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def ok():

    User = db.collection('User').where('email', '==', email.get()).get()
    for users in User:
        user = users.to_dict()
    try:
        password = user['password']
        mail = user['email']
        win.destroy()
        notification.notify(
            title=f'Hello {mail}', message=f'Your password is {password}', app_icon='image/logo.ico')
    except:
        Label(win, text='Your Email does not Exist',
              bg='red', fg='yellow').place(x=50, y=100)


win = Tk()
win.geometry("530x230")
win.resizable(0, 0)
win.title('Retro Stock')
win.iconbitmap(r'image/logo.ico')
win.option_add('*Font', 'times 20')
email = StringVar()

Label(win, text='Email', bg='light blue').place(x=50, y=50)
Entry(win, textvariable=email, width=20).place(x=190, y=50)
Button(win, text='OK', bg='light green', command=ok).place(x=220, y=150)
win['bg'] = 'light blue'

win.mainloop()
