import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()

root.title("llulla GUI") #실행 파일 이름
root.geometry("640x480") #창 크기

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) #10ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop()

# btn = Button(root, text="stop", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150,variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(0, 101):
        time.sleep(0.01)

        p_var2.set(i)
        progressbar2.update()
        print(p_var2.get())

btn = Button(root, text="start", command=btncmd2)
btn.pack()


root.mainloop() # 창이 닫히지 않도록

