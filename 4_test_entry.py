from tkinter import *

root = Tk()

root.title("llulla GUI") #실행 파일 이름
root.geometry("640x480") #창 크기

txt = Text(root, width=30, height=3)
txt.pack()
txt.insert(END, "Write")

e= Entry(root, width=30) #한줄로 입력 받을때
e.pack()
e.insert(0, "one line")

def btncmd():
    print(txt.get("1.0",END)) # 1 : 첫번째 라인, 0 : 0번째 column 위치
    print(e.get())

    txt.delete("1.0",END)
    e.delete(0,END)

btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop() # 창이 닫히지 않도록

