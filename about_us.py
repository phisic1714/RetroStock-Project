from tkinter import *
from PIL import ImageTk, Image
import webbrowser

win = Tk()
win.geometry("1080x610")
win.resizable(0, 0)
win.title('Retro Stock')
win.iconbitmap(r'image/logo.ico')
win.option_add('*Font', 'times 20')

def git():
    webbrowser.open('https://github.com/phisic1714')
def git1():
    webbrowser.open('https://github.com/pphisit')
def git2():
    webbrowser.open('https://github.com/phisic1714/RetroStock-Project.git')   
     
canvas=Canvas(win,width=1080,height=610)
canvas.pack()
bg =  ImageTk.PhotoImage( file ="image/bgA.jpg")
Label(win,image = bg).place(x = 0,y = 0)
canvas.create_image(0, 0, anchor=NW, image=bg)

def close():
    win.destroy()
backlogo =  ImageTk.PhotoImage( file = "image/back.png")
Button(win,image=backlogo,bg='black',command=close).place(x = 40,y = 20)

img1 =Image.open("image/Peera.jpg")
img1 =img1.resize((int(img1.width*.4),int(img1.height*.4)))
photo = ImageTk.PhotoImage(img1)
label2=Label(image=photo)
label2.place(x=150,y=70)
Label(win,text='นาย พีรพัฒน์ สาริมาน',bg="#943126",fg='#ffffff').place(x=150,y=300)
Label(win,text='116310462018-7',bg="#943126",fg='#ffffff').place(x=150,y=350)
Label(win,text='Sec 2',bg="#943126",fg='#ffffff').place(x=150,y=400)


img2 =Image.open("image/P.jpg")
img2 =img2.resize((int(img2.width*.1),int(img2.height*.1)))
photo1 = ImageTk.PhotoImage(img2)
label3=Label(image=photo1)
label3.place(x=700,y=70)
Label(win,text='นาย พิสิษฐ์ กองแก้ว',bg='#633974',fg='#ffffff').place(x=700,y=300)
Label(win,text='116310462030-2',bg='#633974',fg='#ffffff').place(x=700,y=350)
Label(win,text='Sec 2',bg='#633974',fg='#ffffff').place(x=700,y=400)


Button(win,text="Git",font=40,width=6,command=git,bg="#943126",fg='#ffffff').place(x=230,y=450)
Button(win,text="Git",font=40,width=6,command=git1,bg='#633974',fg='#ffffff').place(x=780,y=450)
Button(win,text="Source Code",width=13,height=1,command=git2,bg='#F5B7B1').place(x=450,y=500)


win.mainloop()