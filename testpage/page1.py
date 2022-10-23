from tkinter import *
import subprocess
win = Tk()
win.geometry('1080x610')
win.title('SNES')
win['bg']='#5d8a82'

f = ("Times bold", 14)

def back():
    win.destroy()
    subprocess.call(["python","testpage/homepage.py"])
    #import testpage.page2 as page2


    
Label(
    win,
    text="This is First page",
    padx=20,
    pady=20,
    bg='#5d8a82',
    font=f
).pack(expand=True, fill=BOTH)



Button(
    win, 
    text="back", 
    font=f,
    command=back
    ).pack(fill=X, expand=NO, side=LEFT)



win.mainloop()