# 기반클래스, 부모클래스, 슈퍼클래스, 상위클래스
# 파생클래스, 자식클래스, 하위클래스, 서브클래스

# 단일 상속
# 다중 상속

# 재정의 = 오버라이딩

class Person:
    def greeting(self):
        print('안녕하세요')

class Student(Person):
    def study(self):
        print('공부하기')

james = Student()
james.greeting()
james.study()

print("====")

class PersonList:
    def __init__(self):
        self.person_list = []

    def append_person(self,person):
        self.person_list.append(person)

if __name__ == '__main__':
    person = Person()
    person.greeting()
    pl = PersonList()
    pl.append_person(person)
    print(pl.person_list)
    pl.person_list[0].greeting()
