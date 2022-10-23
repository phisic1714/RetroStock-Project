from tkinter import *
import subprocess

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
bt1.pack(side=LEFT,expand=YES)

bt2=Button(win,text="NES",height=2,width=15,command=page2)#.grid(row=4,column=2)
bt2.pack(side=LEFT,expand=YES)

bt3=Button(win,text="GBC",height=2,width=15,command=page3)#.grid(row=4,column=3)
bt3.pack(side=LEFT,expand=YES)



win.mainloop()    


    