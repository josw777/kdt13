# 접근제한자
# - 파이썬은 자바나 C++처럼 명시적으로 public, protected, private와 같은 키워드를 사용하지 않는 대신
# 밑줄(_)을 사용해서 접근제한을 구분한다.
# - 밑줄이 없는 경우는 public처럼 객체 생성 후 누구나 외부에서 직접 접근이 가능하다.
# - 밑줄(_)이 하나인 경우는 비공개모드로서 직접적인 접근을 제한하고 있어 객체 생성 후 외부에서 직접 접근을 해서는 안된다.
# 하지만 접근을 시도하면 오류없이 접근은 가능하다.
# - 밑줄(_)이 두개인 경우는 객체 생성 후 외부에서 직접적인 접근을 할 수 없으며 객체 생성 후 직접 접근을 시도하면
# 정의되지 않은 속성이나 메서드라고 오류메시지가 발생한다.
# - 밑줄(_)이 두개인 경우는 객체 내부에서는 접근이 가능하며 자식클래스에게 상속이 되지 않는다.

# get/set 메서드





# class Person:
#     def __init__(self):
#         self.hello = '안녕하세요.'
#
#     def greeting(self):
#         print(self.hello)
#
# james = Person()
# james.greeting()

print("====")

# class Person:
#     def __init__(self, name, age, address,wallet):
#         self.hello = '안녕하세요'
#         self.name = name
#         self.age = age
#         self.address = address
#         self.__wallet = wallet  # 변수 앞에 __를 붙여서 비공개 속성으로 만듦
#
#     def pay(self, amount):
#         self.__wallet -= amount # 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음
#         print('이제 {0}원 남았네요.'.format(self.__wallet))
#
#     def greeting(self):
#         print('{0} 저는 {1}입니다.'.format(self.hello,self.name))
#
# maria = Person('마리아',20,'서울시 서초구 반포동',10000)
# maria.greeting()
# maria.pay(3000)
#
# print('이름:',maria.name)
# print('나이:',maria.age)
# print('주소:',maria.address)
# maria.name = '이기자'
# print('이름:',maria.name)
# maria.greeting()

class Person:
    def __init__(self, name, age, address,wallet):
        self.hello = '안녕하세요'
        self._name = name
        self._age = age
        self._address = address
        self._wallet = wallet  # 변수 앞에 __를 붙여서 비공개 속성으로 만듦

    def get_name(self):
        return self._name
    def set_name(self,name):
        self._name = name
    name = property(get_name,set_name)

    def get_age(self):
        return self._age
    def set_age(self,age):
        self._age = age
    age = property(get_age,set_age)

    def get_address(self):
        return self._address
    def set_address(self,address):
        self._address = address
    address = property(get_address,set_address)

    def get_wallet(self):
        return self._wallet
    def set_wallet(self,wallet):
        self._wallet = wallet
    wallet = property(get_wallet,set_wallet)

    def pay(self, amount):
        self.__wallet -= amount # 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음
        print('이제 {0}원 남았네요.'.format(self._wallet))

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello,self._name))

if __name__ == "__main__":
    maria = Person('마리아',20,'서울시 서초구 반포동',10000)
    maria.greeting()
    print(maria.name)
    maria.name = "이기자"
    print(maria.name)
