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

currentUser=db.collection('currentUser').get()
for users in currentUser :
   userinfo=users.to_dict()
user=auth.sign_in_with_email_and_password(userinfo['email'],userinfo['password'])
def close():
    db.collection('currentUser').document(users.id).delete()
    win.destroy()

def confirm():
    if userinfo['password'] == current_password.get():
        try:
            user=auth.sign_in_with_email_and_password(userinfo['email'],userinfo['password'])
            auth.delete_user_account(user['idToken'])
            auth.create_user_with_email_and_password(email.get(),New_password.get())
            db=firestore.client()
            Userstore=db.collection('User').get()
            currentUser=db.collection('currentUser').get()
            for Userstores in Userstore :
                if Userstores.to_dict()['email']==userinfo['email']:
                    db.collection('User').document(Userstores.id).update({'email':email.get(),'password':New_password.get()})
                    for CurrentUserstores in currentUser :
                        db.collection('currentUser').document(CurrentUserstores.id).update({'email':email.get(),'password':New_password.get()})
            win.destroy()   
            subprocess.call(["python", "user/libraly.py"])     
        except:
            Label(win, text='Email already Exist! or Your Email and Password incorect.',bg='red',fg='yellow',font=('Times 13')).place(x=130,y=290)
    else :
        Label(win, text='Your Current Password incorect.',bg='red',fg='yellow',font=('Times 13')).place(x=130,y=290)

def del_user():
    try:
        user=auth.sign_in_with_email_and_password(userinfo['email'],userinfo['password'])
        auth.delete_user_account(user['idToken'])
        db=firestore.client()
        Userstore=db.collection('User').get()
        currentUser=db.collection('currentUser').get()
        for Userstores in Userstore :
                if Userstores.to_dict()['email']==userinfo['email']:
                    db.collection('User').document(Userstores.id).delete()
        for CurrentUserstores in currentUser :
            db.collection('currentUser').document(CurrentUserstores.id).delete()
        win.destroy()        
    except:
        Label(win, text='Error Cannot find User and Delete them.',bg='red',fg='yellow',font=('Times 13')).place(x=130,y=290)

def cancle ():
    win.destroy()   
    subprocess.call(["python", "user/libraly.py"]) 

def about_us():
   subprocess.call(["python", "about_us.py"])

win = Tk()
win.geometry("630x600")
win.resizable(0, 0)
win.title('Retro Stock')
win.iconbitmap(r'image/logo.ico')
win.option_add('*Font', 'times 20')
win.protocol("WM_DELETE_WINDOW", close)
img1 = ImageTk.PhotoImage(Image.open("image/logo.png"))  
img2=ImageTk.PhotoImage(Image.open("image/edituser.png"))  
img3=ImageTk.PhotoImage(Image.open("image/aboutus.png"))  
canvas = Canvas(win, width = 650, height = 630)  
canvas.pack()
canvas.create_image(win.winfo_width()/2, 520, anchor=CENTER, image=img1)  
canvas.create_image(win.winfo_width()/2, 50, anchor=CENTER, image=img2)

email =StringVar()
email.set(userinfo['email'])
current_password=StringVar()
New_password=StringVar()
conf_password=StringVar()
Label(win, text='Change Email',bg='light green').place(x=50,y=100)
Label(win, text='Current Password',bg='light green').place(x=50,y=150)
Label(win, text='Change Password',bg='light green').place(x=50,y=200)
Label(win, text='Confirm Password',bg='light green').place(x=50,y=250)
Entry(win,textvariable=email,width=20).place(x=290,y=100)
Entry(win,show="*",textvariable=current_password,width=20).place(x=290,y=150)
Entry(win,show="*",textvariable=New_password,width=20).place(x=290,y=200)
Entry(win,show="*",textvariable=conf_password,width=20).place(x=290,y=250)
Button(win,text='Confirm',command=confirm,bg='green',fg='white').place(x=150,y=313)
Button(win,text='Cancle',command=cancle,bg='yellow',fg='black').place(x=350,y=313)
Button(win,text='Delete User',command=del_user,bg='red',fg='white').place(x=230,y=380)
Button(win,image=img3,command=about_us,bg='#147444',fg='white').place(x=450,y=450)

win.configure(bg='silver')
win.mainloop()
