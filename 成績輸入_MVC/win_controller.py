# 控制 Model 與 View
from lab09_MVC.model import Student
from lab09_MVC.win import MyTkWindow


class StudentWindowController:
    def __init__(self):
        #組合零件
        self.student_mode = None
        self.window = MyTkWindow(callback=self.callback)
        self.student_input_view = self.window
        self.student_output_view = self.window

    def run(self):
        self.window.mainloop()

    def callback(self):  # 給視窗執行的回呼
        # 輸入資料 input_view
        name = self.student_input_view.input_name()
        eng_str = self.student_input_view.input_eng()
        eng = int(eng_str)
        math_str = self.student_input_view.input_math()
        math = int(math_str)
        # 建立 資料模型 model
        self.student_mode = Student(name, eng, math)
        # 輸出結果 output_view
        # controller 協調工作 將 model_eng整數 轉換字串於 view 顯示
        name = self.student_mode.name
        self.student_output_view.show_name(name)
        eng_str = str(self.student_mode.eng)
        self.student_output_view.show_eng(eng_str)
        math_str = str(self.student_mode.math)
        self.student_output_view.show_math(math_str)
        total_str = str(self.student_mode.總分)
        self.student_output_view.show_total(total_str)


