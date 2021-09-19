import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import code2
import random

class aaa():

    def __init__(self):

        window = tk.Tk()
        window.title("終極密碼")
        window.geometry('600x480')

        nb = ttk.Notebook(window)

        p1 = tk.Frame(nb, bg='gray')

        nb.add(p1, text="終極密碼")
        nb.pack(fill="both", expand="yes")

        self.low = 1
        self.high = 100
        self.num1 = int(random.randint(2, 99))

        self.xf = tk.Frame(p1)
        self.xf.pack(side=tk.TOP)
        self.x_e = tk.Entry(p1)
        self.x_e.pack(side=tk.LEFT)
        self.x_e.place(x=230, y=50)

        self.lab = tk.Label(p1, text='請猜數字介於')
        self.lab.pack()
        self.lab.place(x=270)

        self.result_label = tk.Label(p1)
        self.result_label.pack()
        self.result_label.place(x=300, y=150)

        self.result_label2 = tk.Label(p1, text='1')
        self.result_label2.pack()
        self.result_label2.place(x=280, y=20)

        self.label = tk.Label(p1,  text='-')
        self.label.pack()
        self.label.place(x=300, y=20)

        self.result_label3 = tk.Label(p1, text='100')
        self.result_label3.pack()
        self.result_label3.place(x=320, y=20)

        self.calculate = tk.Button(p1, text='猜', command=self.btnclick1, fg='Red')
        self.calculate.pack()
        self.calculate.place(x=290, y=100)

        window.mainloop()

    def btnclick1(self):
            try:
                self.x1 = self.x_e.get()
                self.a1 = code2.num(self.x1, self.num1, self.low, self.high)

                self.low = self.a1.oo()
                self.high = self.a1.hh()
                self.num1 = self.a1.www()
                self.result_label.configure(text=self.a1.www())
                self.result_label2.configure(text=self.a1.oo())
                self.result_label3.configure(text=self.a1.hh())
            except:
                tk.messagebox.showwarning(title='嘿', message='輸入數字好不')

main = aaa()






