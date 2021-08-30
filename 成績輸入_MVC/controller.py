from lab09_MVC.model import Student
from lab09_MVC.view import StudentInputView, StudentOutputView


class StudentController:
    def __init__(self):
        self.student_model = None
        self.student_input_view = StudentInputView()
        self.student_output_view = StudentOutputView()

    def run(self):
        name = self.student_input_view.input_name()
        eng_str = self.student_input_view.input_eng()
        eng = int(eng_str)
        math_str = self.student_input_view.input_math()
        math = int(math_str)

        self.student_model = Student(name, eng, math)

        name = self.student_model.name
        self.student_output_view.show_name(name)
        eng_str = str(self.student_model.eng)
        self.student_output_view.show(eng_str)
        math_str = str(self.student_model.math)
        self.student_output_view.show(math_str)
        total_str = str(self.student_model.總分)
        self.student_output_view.show(total_str)