from tkinter import*
from time import*
from PIL import Image, ImageTk
from tkinter import messagebox
import pyperclip

#전역 변수 선언#
fnameList = ["강의1.png", "강의2.png", "강의3.png", "강의4.png", "강의5.png", "강의6.png", "강의7.png", "강의8.png", "강의9.png", "강의10.png", "강의11.png", "강의12.png"]
photoList = [None]*9
num = 0

def Next(): # 다음버튼 클릭시
    global num
    num += 1
    if num > 11:
        num = 0
    photo = PhotoImage(file = "gif/" + fnameList[num])
    if num == 0:
        photo = photo.subsample(4) # 사진 크기 조절
    if num == 8:
        photo = photo.subsample(2)
    if num == 9:
        photo = photo.subsample(4)
    if num == 10:
        photo = photo.subsample(2)
    pLabel.configure(image = photo)
    pLabel.image = photo
    
def Back(): # 이전버튼 클릭시
    global num
    num -= 1
    if num < 0:
        num = 11
    photo = PhotoImage(file = "gif/" + fnameList[num])
    if num == 0:
        photo = photo.subsample(4)
    if num == 8:
        photo = photo.subsample(2)
    if num == 9:
        photo = photo.subsample(4)
    if num == 10:
        photo = photo.subsample(2)
    pLabel.configure(image = photo)
    pLabel.image = photo
    
def Follow(): # 링크복사된뒤 출력
    return messagebox.showinfo("링크", "링크가 클립보드에 복사되었습니다.")

def Click(event): # 클릭하면 각 이미지들에 맞는 링크를 복사
    if num == 0:
        message = "https://nomadcoders.co/noom?gad_source=1&gclid=CjwKCAiA04arBhAkEiwAuNOsIr4FN6N44dSWyOWPNQ0f_feKNipE_9N909fb_XWTC-JjRUCfZzobBBoCTiQQAvD_BwE"
        pyperclip.copy(message) # 클립보드에 message복사
        Follow()
    elif num == 1:
        message = "https://www.inflearn.com/course/%ED%98%84%EC%A7%81%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%95%88%EB%93%9C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%95%B1"
        pyperclip.copy(message)
        Follow()
    elif num == 2:
        message = "https://www.inflearn.com/course/%EC%9E%90%EB%B0%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4-%EC%BD%94%ED%85%8C%EB%8C%80%EB%B9%84"
        pyperclip.copy(message)
        Follow()
    elif num == 3:
        message = "https://www.inflearn.com/course/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%AC%B8-%EC%9D%B8%ED%94%84%EB%9F%B0-%EC%98%A4%EB%A6%AC%EC%A7%80%EB%84%90"
        pyperclip.copy(message)
        Follow()
    elif num == 4:
        message = "https://www.udemy.com/course/best-react/"
        pyperclip.copy(message)
        Follow()
    elif num == 5:
        message = "https://www.inflearn.com/course/%ED%94%BC%EA%B7%B8%EB%A7%88-%EC%9E%85%EB%AC%B8-%EC%9D%B8%ED%94%84%EB%9F%B0-%EC%98%A4%EB%A6%AC%EC%A7%80%EB%84%90"
        pyperclip.copy(message)
        Follow()
    elif num == 7:
        message = "https://nomadcoders.co/javascript-for-beginners"
        pyperclip.copy(message)
        Follow()
    elif num == 8:
        message = "https://www.youtube.com/watch?v=xlvtnoKKl68"
        pyperclip.copy(message)
        Follow()
    elif num == 9:
        message = "https://nomadcoders.co/react-for-beginners"
        pyperclip.copy(message)
        Follow()
    elif num == 10:
        message = "https://www.inflearn.com/course/database-2-mysql-%EA%B0%95%EC%A2%8C"
        pyperclip.copy(message)
        Follow()
    elif num == 11:
        message = "https://www.udemy.com/course/best-ai-17-hours/#instructor-5"
        pyperclip.copy(message)
        Follow()

window = Tk()
window.geometry("520x350") # 윈도우 창 크기
window.title("MODUM")

btnNext = Button(window, text = ">>>", command=Next) # 다음버튼, 이전버튼
btnBack = Button(window, text = "<<<", command=Back)

photo = PhotoImage(file = "gif/" + fnameList[0]) # 사진 확인
photo = photo.subsample(4) # 처음 사진 크기조절
pLabel = Label(window, image = photo)
pLabel.bind("<Button-1>", Click)

btnNext.place(x = 300, y =10) # 다음버튼, 이전버튼, 사진 좌표 
btnBack.place(x = 180, y =10)
pLabel.place(x = 15, y =50)

button1 = Button(window, text = "종료", fg = "blue", command = quit) # 종료버튼
button1.pack()

window.mainloop()