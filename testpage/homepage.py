from tkinter import *
import subprocess
from PIL import ImageTk, Image

win = Tk()
win.geometry('1080x610')
win.title('PythonGuides')
win['bg']='#ccff99'


def page1():
    win.destroy()
    subprocess.call(["python","testpage/page1.py"])    

def page2():
    win.destroy()
    subprocess.call(["python","testpage/page2.py"])

def page3():
    win.destroy()
    subprocess.call(["python","testpage/page3.py"])

label1=Label(win,text="HOME",padx=1080,pady=15,font=90,bg="#ff9966")#.grid(row=0,column=0)
label1.pack()

bt1=Button(win,text="SNES",height=2,width=15,command=page1)#.grid(row=4,column=1)
bt1.place(x=150,y=400)

bt2=Button(win,text="NES",height=2,width=15,command=page2)#.grid(row=4,column=2)
bt2.place(x=500,y=400)

bt3=Button(win,text="GBC",height=2,width=15,command=page3)#.grid(row=4,column=3)
bt3.place(x=850,y=400)


img = Image.open("photo/SNES.png")
img =img.resize((int(img.width*.4),int(img.height*.4)))
photo = ImageTk.PhotoImage(img)
label2=Label(image=photo)
label2.place(x=50,y=70)

img1 = Image.open("photo/NES.png")
img1 =img1.resize((int(img1.width*.4),int(img1.height*.4)))
photo1 = ImageTk.PhotoImage(img1)
label3=Label(image=photo1)
label3.place(x=420,y=70)

img2 = Image.open("photo/GBC.png")
img2 =img2.resize((int(img2.width*1),int(img2.height*1)))
photo2 = ImageTk.PhotoImage(img2)
label4=Label(image=photo2)
label4.place(x=810,y=80)



win.mainloop()    


    