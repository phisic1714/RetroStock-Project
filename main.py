import tkinter as tk
window = tk.Tk()
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.title("Retro Stock")
#หน้ารอง
def f():
    #Reflesh หน้าทั้งหมด เพื่อไม่ให้ Widget ซ้อนกัน เหมือน จอ LCD I2C ที่ใช้ LCD.clear() 
    for widgets in window.winfo_children():
      widgets.destroy()
    #ตั้งตัวหนังสือ
    label = tk.Label(window, text="flutter หัวขวด")
    #ตั้งปุ่ม
    tk.Button(window, text= "Click Here", command= main).pack(pady= 20)
    label.pack()
#หน้าหลัก
def main():
    #Reflesh หน้าทั้งหมด เพื่อไม่ให้ Widget ซ้อนกัน เหมือน จอ LCD I2C ที่ใช้ LCD.clear() อ่ะ
    for widgets in window.winfo_children():
      widgets.destroy()
    #ตั้งตัวหนังสือ
    label = tk.Label(window, text="Hello Tkinter!")
    #ตั้งปุ่ม
    tk.Button(window, text= "Click Here", command= f).pack(pady= 20)
    label.pack()
    window.mainloop()
    
main()
