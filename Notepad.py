"""Quiz) tkinter를 이용한 메모장 프로그램 만들기

[GUI 조건]
1. title : 제목 없음 - Windows 메모장
2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
3. 실제 메뉴 구현 : 파일메뉴 내에서 열시, 저장, 끝내기 3개만 처리
3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기
3-2. 저장 : mynote.txt 파일에 현재 내용 저장하기
3-3. 끝내기 : 프로그램 종료
4. 프로그램 시작 시 본문은 비어있는 상태
5. 하단 status 바는 필요 없음
6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정은 가능해야 함
7. 본문 우측에 상하 스크롤 바 넣기"""
import os
from tkinter import *

root = Tk()



filename = "mynote.txt"

root.title("제목없음 - Windows 메모장") #실행 파일 이름
root.geometry("640x480") #창 크기

#메뉴
menu = Menu(root)

def open_file():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf=8")as file:
            txt.delete("1.0",END)
            txt.insert(END, file.read())

def save_file():
    with open(filename, "w", encoding="utf=8")as file:
        file.write(txt.get("1.0",END))


#메뉴 - 파일
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="Open File", command=open_file)
menu_file.add_command(label="Save All", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

menu.add_cascade(label="파일", menu=menu_file)

#메뉴 - 편집
menu.add_cascade(label="편집", menu=menu_file)
#메뉴 - 서식
menu.add_cascade(label="서식", menu=menu_file)

#메뉴 - 보기
menu.add_cascade(label="보기", menu=menu_file)

#메뉴 - 도움말
menu.add_cascade(label="도움말", menu=menu_file)

root.config(menu=menu)

#스크롤바

scrollbar=Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 문자입력
txt = Text(root)
txt.pack(side="left",fill="both", expand=True)

scrollbar.config(command=txt.yview)
root.mainloop() # 창이 닫히지 않도록
