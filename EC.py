import tkinter
import tkinter.ttk as tk
window = tkinter.Tk()

window.title('환율 계산기')
window.geometry('300x200+100+100')
exchange_data = {'엔화':{'rate':0.11, 'symbol': '¥'},
                 '달러':{'rate':0.00076, 'symbol': '$'},
                 '유로':{'rate':0.00057, 'symbol': '£'}}

def calculate_exchange():
    try:
        amount = float(text_box.get())
        currency = combobox.get()
        rate = exchange_data[currency]['rate']
        symbol = exchange_data[currency]['symbol']
        converted_amount = amount * rate
        label_result.config(text=f"환전 결과: {converted_amount:.2f} {symbol}")
    except ValueError:
        label_result.config(text="유효한 금액을 입력하세요")
        

label1 = tkinter.Label(text = '금액 (원):')
label2 = tkinter.Label(text = '환전할 나라:')
button = tkinter.Button(text = '계산하기', command = calculate_exchange)
label_result = tkinter.Label(text= '환전 결과:')

label1.grid(row=0, column=0, padx=10, pady=10)
label2.grid(row=1, column=0, padx=10, pady=10)

text_box = tkinter.Entry(window)
combobox = tk.Combobox(window, values=list(exchange_data.keys()))

text_box.grid(row=0, column=1, padx=10, pady=10)
combobox.grid(row=1, column=1, padx=10, pady=10)
button.grid(row=2, column=1)
label_result.grid(row=3, columnspan=2, pady=10)

window.mainloop()