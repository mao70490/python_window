import tkinter as tk
from tkinter import END, messagebox

class MyTkWindow(tk.Tk):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback  # callback 回呼函式
        self.title("成績輸入查詢")
        mainFrame = tk.Frame(self, relief="groove", bd=2)
        titleFrame = tk.Frame(mainFrame)
        tk.Label(titleFrame, text="成績輸入及查詢", font=("Arial", 18, 'bold'), fg='#555').pack(padx=10)
        titleFrame.pack()
        tk.Label(mainFrame, text="-----------------------------------").pack()
        # --------------- 建立 inputFrame ---------------
        self.inputFrame = tk.Frame(mainFrame, width=50)
        tk.Label(self.inputFrame, text="輸入姓名:", font=("Arial", 13)).grid(row=0, column=0, sticky=tk.E)
        self.nameEntry = tk.Entry(self.inputFrame, textvariable=tk.StringVar(), bd=5)
        self.nameEntry.grid(row=0, column=1, sticky=tk.E)

        tk.Label(self.inputFrame, text="輸入 英文成績:", font=("Arial", 13)).grid(row=1, column=0, sticky=tk.E)
        self.engEntry = tk.Entry(self.inputFrame, textvariable=tk.StringVar(), bd=5)
        self.engEntry.grid(row=1, column=1, sticky=tk.E)
        self.engEntry.insert(END, '0')

        tk.Label(self.inputFrame, text="輸入 數學成績:", font=("Arial", 13)).grid(row=2, column=0, sticky=tk.E)
        self.mathEntry = tk.Entry(self.inputFrame, textvariable=tk.StringVar(), bd=5)
        self.mathEntry.grid(row=2, column=1, sticky=tk.E)
        self.mathEntry.insert(END, '0')

        submitButton = tk.Button(self.inputFrame, font=("Arial", 14), text="RUN", command=self.button_handler)
        submitButton.grid(row=3, column=1, sticky=tk.W)
        self.inputFrame.pack()

        # ----------  建立顯示畫面 -----------
        self.listFrame = tk.Frame(mainFrame)
        tk.Label(self.listFrame, text='姓名:', font=("Arial", 14)).grid(row=0, column=0, stick=tk.E, padx=10, pady=10)
        self.nameLabel = tk.Label(self.listFrame, text="", font=("Arial", 14))
        self.nameLabel.grid(row=0, column=1, sticky=tk.W, padx=10, pady=10)

        tk.Label(self.listFrame, text='英文分數:', font=("Arial", 14)).grid(row=1, column=0, stick=tk.E, padx=10, pady=10)
        self.engLabel = tk.Label(self.listFrame, text="", font=("Arial", 14))
        self.engLabel.grid(row=1, column=1, sticky=tk.W, padx=10, pady=10)

        tk.Label(self.listFrame, text='數學分數:', font=("Arial", 14)).grid(row=2, column=0, stick=tk.E, padx=10, pady=10)
        self.mathLabel = tk.Label(self.listFrame, text="", font=("Arial", 14))
        self.mathLabel.grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)

        tk.Label(self.listFrame, text='總分:', font=("Arial", 14)).grid(row=3, column=0, stick=tk.E, padx=10, pady=10)
        self.totalLabel = tk.Label(self.listFrame, text="", font=("Arial", 14))
        self.totalLabel.grid(row=3, column=1, sticky=tk.W, padx=10, pady=10)
        self.listFrame.pack()

        mainFrame.pack(pady=30, ipadx=20, ipady=20)


    def input_name(self):
        name = self.nameEntry.get()
        if len(name) < 2 or name is None:
            messagebox.showinfo("錯誤", "名子長度需要大於 2")
        return name


    def input_eng(self):
        eng_str = self.engEntry.get()
        eng = int(eng_str)
        if (eng < 0 or eng > 100) or eng is None:
            messagebox.showinfo("錯誤", "英文成績必須 0 ~ 100 , 請重新輸入")
        return eng


    def input_math(self):
        math_str = self.mathEntry.get()
        math = int(math_str)
        if (math < 0 or math > 100) or math is None:
            messagebox.showinfo("錯誤", "數學成績必須 0 ~ 100 , 請重新輸入")
        return math

    def show_name(self, name):
        self.nameLabel['text'] = name

    def show_eng(self, eng_str):
        self.engLabel['text'] = eng_str

    def show_math(self, math_str):
        self.mathLabel['text'] = math_str

    def show_total(self, total_str):
        self.totalLabel['text'] = total_str

    def button_handler(self):
        self.callback() # 執行 回呼函式



