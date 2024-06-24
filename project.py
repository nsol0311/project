import tkinter
import tkinter.font
def func1():
    price = 0
    if cv1.get() == 1:
        price += 2000
    if cv2.get() == 1:
        price += 1800
    if cv3.get() == 1:
        price += 1800
    if cv4.get() == 1:
        price += 2100
    if 0 < price < 5000:
        price+=2000
        text.config(text = '(배달료:2000원)')
    else:
        text.config(text = '')
    result.config(text = '가격 : '+str(price)+'원')

window = tkinter.Tk()
window.title("음식계산기")
window.geometry("420x230+100+100")
title_font = tkinter.font.Font(family = "휴먼둥근헤드라인", size = 20)
title = tkinter.Label(window, text = "음식계산기", font = title_font)

title.grid(row = 0, column = 0, columnspan = 4)
text_font = tkinter.font.Font(family = '맑은 고딕', size = 20)
text = tkinter.Label(window, text = '(배달비:2000원)', fg = 'red')
text.grid(row = 4, column = 0, columnspan = 4)
image1 = tkinter.PhotoImage(file = "고기.png")
image2 = tkinter.PhotoImage(file = "씨푸드.png")
image3 = tkinter.PhotoImage(file = "일반.png")
image4 = tkinter.PhotoImage(file = "카레.png")

label1 = tkinter.Label(window, image = image1)
label2 = tkinter.Label(window, image = image2)
label3 = tkinter.Label(window, image = image3)
label4 = tkinter.Label(window, image = image4)


cv1 = tkinter.IntVar()
ckb1 = tkinter.Checkbutton(window, text = '2,000', variable = cv1, command = func1)
cv2 = tkinter.IntVar()
ckb2 = tkinter.Checkbutton(window, text = '1,800', variable = cv2, command = func1)
cv3 = tkinter.IntVar()
ckb3 = tkinter.Checkbutton(window, text = '1,800', variable = cv3, command = func1)
cv4 = tkinter.IntVar()
ckb4 = tkinter.Checkbutton(window, text = '2,100', variable = cv4, command = func1)

label1.grid(row = 1, column = 0)
label2.grid(row = 1, column = 1)
label3.grid(row = 1, column = 2)
label4.grid(row = 1, column = 3)

ckb1.grid(row = 2, column = 0)
ckb2.grid(row = 2, column = 1)
ckb3.grid(row = 2, column = 2)
ckb4.grid(row = 2, column = 3)

result = tkinter.Label(window, text = "가격:0", font = title_font)

result.grid(row = 3, column = 0, columnspan = 4)


window.mainloop()
