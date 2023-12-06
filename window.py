from tkinter import*
from time import*
from PIL import Image, ImageTk

#전역 변수 선언 부분#
fnameList = ["강의1.png", "강의2.png", "강의3.png", "강의4.png", "강의5.png", "강의6.png", "강의7.png", "강의8.png", "강의9.png", "강의10.png"]
photoList = [None]*9
num = 0

#함수 선언 부분#
def Next():
    global num
    num += 1
    if num > 9:
        num = 0
    
    photo = PhotoImage(file = "gif/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    
def Back():
    global num
    num -= 1
    if num < 0:
        num = 9
    photo = PhotoImage(file = "gif/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    
#메인 코드 부분#
window = Tk()
window.geometry("700x500")
window.title("asdlfkjasdfl;ajlf;")

btnNext = Button(window, text = ">>>", command=Next)
btnBack = Button(window, text = "<<<", command=Back)

photo = PhotoImage(file = "gif/" + fnameList[0])
pLabel = Label(window, image = photo)

btnNext.place(x = 400, y =10)
btnBack.place(x = 250, y =10)
pLabel.place(x = 15, y =50)

window.mainloop()