from tkinter import *

root = Tk()
root.title("llulla GUI") #실행 파일 이름
root.geometry("640x480") #창 크기


frame = Frame(root)
frame.pack()

scrollbar=Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = Listbox(frame, selectmode="extended", height=10,yscrollcommand = scrollbar.set)

for i in range(1,32):
    listbox.insert(END,str(i)+"일")
listbox.pack()

scrollbar.config(command=listbox.yview)

root.mainloop() # 창이 닫히지 않도록

