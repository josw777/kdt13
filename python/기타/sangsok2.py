class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'

class Student(Person):
    def __init__(self):
        super().__init__()  # 다른 언어에서는 super가 제일 위에 파이썬은 상관없음
        print('Student __init__')
        self.school = '파이썬 코딩 도장'

james = Student()
print(james.school)
print(james.hello)

class Student2(Person):
    pass

james = Student2()
print(james.hello)