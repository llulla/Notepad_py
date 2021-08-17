import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("llulla GUI") #실행 파일 이름
root.geometry("640x480") #창 크기

def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")

def error():
    msgbox.showerror("에러", "오류가 발생하였습니다.")

def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

def retrycancel():
    response = msgbox.askokcancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")
    print("응답:", response)
    if response ==1:
        print("재시도")
    elif response ==0:
        print("취소")
def yesno():
    msgbox.askokcancel("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다.\n. 저장 하시겠습니까?")
    print("응답:", response)
    if response ==1:
        print("예")
    elif response ==0:
        print("아니오")
    else:
        print("취소")
Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()


root.mainloop() # 창이 닫히지 않도록
