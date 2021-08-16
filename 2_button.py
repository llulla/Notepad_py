from tkinter import *

root = Tk()

root.title("llulla GUI") #실행 파일 이름
root.geometry("640x480") #창 크기

btn1 = Button(root, text="btn1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10,text="btn2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5,text="btn3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="btn4")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="btn5")
btn5.pack()

photo = PhotoImage(file="button.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print('click the btn')

btn7 = Button(root, text="동작버튼", command=btncmd)
btn7.pack()


root.mainloop() # 창이 닫히지 않도록

