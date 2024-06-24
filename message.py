import tkinter
window = tkinter.Tk()
window.title("SMD")
window.geometry("300x200+100+100")
m = tkinter.Message(window, text = "메세지입니다.", width = 100, relief = "solid")
m.pack()

window.mainloop()