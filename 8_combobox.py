import tkinter.ttk as ttk
from tkinter import *

root = Tk()

root.title("llulla GUI") #실행 파일 이름
root.geometry("640x480") #창 크기

values = [str(i)+"일" for i in range(1,32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일")

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0) #0번째 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text="choice", command=btncmd)
btn.pack()
root.mainloop() # 창이 닫히지 않도록

