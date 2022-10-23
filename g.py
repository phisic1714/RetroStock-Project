
from secrets import choice
from tkinter import *
from tkinter import ttk

root =Tk()
root.title("โปรแกรมขายเกมส์")
root.geometry( "1080x610" )

Label(text="ชนิดเครื่อง",font=20).grid(row=0,column=0)
choice= StringVar(value="เลือกชนิดเครื่อง")
combo=ttk.Combobox(textvariable=choice)
combo["values"]=('A','B','C')
combo.grid(row=0,column=1)

Label(text="ประเภท",font=20).grid(row=0,column=2)
choice1= StringVar(value="เลือกประเภท")
combo=ttk.Combobox(textvariable=choice1)
combo["values"]=('A','B','C')
combo.grid(row=0,column=3)

def selecttype():
    Label(text="เลือกชนิดเครื่อง"+choice.get()).grid(row=1,column=0)
    Label(text="เลือกประเภท"+choice1.get()).grid(row=1,column=1)


   


btn=Button(text="ค้นหา",command=selecttype)
#btn=Button(text="HOME",command=home)
btn.grid(row=0,column=4)

root.mainloop()
