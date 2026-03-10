class Person:
    bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)

class Calc:
    @staticmethod
    def add(a,b):
        print(a+b)

    @staticmethod
    def mul(a,b):
        print(a*b)

Calc.add(10,20) # 클래스에서 바로 메서드 호출
Calc.mul(10,20) # 클래스에서 바로 메서드 호출

obj1 = Calc()   # 객체 만드는거 가능은 한데 쓰지 않는게 좋음
obj1.add(10,20)
obj2 = Calc()
obj2.add(100,200)