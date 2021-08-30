class StudentOutputView:
    def show_name(self, name):
        print('name:', name)
    def show_eng(self, eng_str):
        print('eng:', eng_str)
    def show_math(self, math_str):
        print('math:', math_str)
    def show_total(self, total_str):
        print('total:', total_str)

class StudentInputView:
    def input_name(self):
        while True:
            name = input('輸入姓名:')
            if len(name)<2 or not name:
                print('錯誤')
            else:
                break
            return name


    def input_eng(self):
        while True:
            eng_str = input('輸入eng成績:')
            eng = int(eng_str)
            if eng < 0 or eng > 0:
                print('錯誤')
            else:
                break
            return eng_str

    def input_math(self):
        while True:
            math_str = input('輸入eng成績:')
            math = int(math_str)
            if math < 0 or math > 0:
                print('錯誤')
            else:
                break
            return math_str



