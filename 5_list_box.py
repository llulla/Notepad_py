from tkinter import *

root = Tk()

root.title("llulla GUI") #실행 파일 이름
root.geometry("640x480") #창 크기

listbox = Listbox(root, selectmode = "extended", height=0)#height 보여줄 목록 수
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    listbox.delete(END)#맨뒤에 항목을 삭제 0은 맨앞에 항목 삭제

    #갯수 확인
    print("리스트에는 ",listbox.size(),"개가 있어요")

    #항목 확인 (시작 idx, 끝 idx)
    print("1~3 까지의 항목 : ", listbox.get(0,2))

    #선택 항목 확인 (위치로 반환 ex) 1,2,3 
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="click", command=btncmd)
btn.pack()
root.resizable(False, False) # 창 크기 변경 불가

root.mainloop() # 창이 닫히지 않도록

