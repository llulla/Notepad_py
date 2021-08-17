from tkinter import *

root = Tk()

root.title("llulla GUI") #실행 파일 이름
root.geometry("640x480") #창 크기

chkvar = IntVar() #chkvar에 int 형으로 값을 저장한다.
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select() #자동 선택 처리
# chkbox.deselect() #자동 선택 해제
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) #0 : 체크해제, 1 : 체크
    print(chkvar2.get())
btn = Button(root, text="click", command=btncmd)
btn.pack()
root.mainloop() # 창이 닫히지 않도록

