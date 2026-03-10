# 재정의 = 오버라이딩
# 다중상속일 때 오버라이딩은 정의할때 먼저쓴 클래스가 됨

class Person:
    def __init__(self):
        print("Person Class")
    def greeting(self):
        print('안녕하세요1')

class Student(Person):
    def greeting(self):
        print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')

james = Student()
james.greeting()
person = Person()
person.greeting()

print("====")

lst = []
person1 = Student()
person2 = Person()

lst.append(person1)
lst.append(person2)
for i in lst:
    i.greeting()

print("====")

class University:
    def __init__(self):
        print("University Class")
    def manage_credit(self):
        print("학점관리")
    def greeting(self):
        print('안녕하세요.2')

class Undergraduate(University,Person):
    def study(self):
        print('공부하기')

jamess = Undergraduate()
jamess.greeting()
jamess.manage_credit()
jamess.study()

print("====")

class A:
    def greeting(self):
        print('안녕하세요. A입니다.')

class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')

class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')

class D(B,C):
    pass

x = D()
x.greeting()