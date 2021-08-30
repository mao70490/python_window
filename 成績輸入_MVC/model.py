class Student:
    def __init__(self, name, eng, math):
        if len(name) < 2 or not name:
            raise Exception('name 長度至少2')
        self.name = name
        if (eng < 0 or eng > 100) or not eng:
            raise Exception('eng為0~100')
        self.eng = eng
        if (math < 0 or math > 100) or not math:
            raise Exception('math為0~100')
        self.math = math

    def __str__(self):
        return self.name

    @property
    def 總分(self):
        return self.eng+self.math