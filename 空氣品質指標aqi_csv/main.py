import data
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        # for county in countyList:
        #     print(county.siteName, county.name, county.AQI, county.status, county.publishTime)

        self.geometry('950x630')
        titleFrame = tk.Frame(self)
        borderFrame = tk.Frame(titleFrame,borderwidth = 1, relief=tk.GROOVE,padx=20, pady=20)
        tk.Label(borderFrame,text="全省空氣品質標準_AQI",font=("Courier", 25, "italic")).pack()
        self.publishTimeLabel = tk.Label(borderFrame,text="發布時間:"+countyList[0].publishTime)
        self.publishTimeLabel.pack()
        tk.Button(borderFrame,text="更新",padx=10, pady=10,command=self.userClickUpdate).pack(pady=(20,0),anchor=tk.E)
        borderFrame.pack()
        titleFrame.pack(padx=20, pady=20)

        # 建立下方的frame
        self.createDisplayFrame()
    def createDisplayFrame(self):

        # 下方的frame
        self.displayFrame = tk.Frame(self) #建立顯示資料的frame
        # 設定分欄
        columnsNum = 5
        rowsNum = len(countyList)//columnsNum+1

        for index, county in enumerate(countyList):
            subIndex = index % rowsNum
            if subIndex == 0:
                tableFrame =tk.Frame(self.displayFrame,bg='#cccccc')
                tableFrame.pack(side=tk.LEFT,padx=(20,0),expand=True,fill=tk.Y)
            tk.Label(tableFrame,text=county.name,bg='#cccccc').grid(row=subIndex,column=0);
            tk.Label(tableFrame, text=county.siteName,bg='#cccccc').grid(row=subIndex, column=1);
            tk.Label(tableFrame, text=county.AQI,bg='#cccccc').grid(row=subIndex, column=2);
            statusLabel = tk.Label(tableFrame, text=county.status,bg='#cccccc');
            if county.status != '良好':
                statusLabel['fg'] = 'red'
            statusLabel.grid(row=subIndex, column=3)
        self.displayFrame.pack()

    def updateWindow(self):
        self.displayFrame.destroy()
        self.createDisplayFrame()
        self.publishTimeLabel['text']="發布時間:"+countyList[0].publishTime

    def userClickUpdate(self):
        data.updateData() # 更新資料
        self.updateWindow() # 更新畫面

if __name__=="__main__":
    countyList=data.aqiData
    window=Window()
    window.title("AQI指標")
    window.mainloop()