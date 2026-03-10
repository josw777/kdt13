class Sangpum:
    def __init__(self):
        self._code = ""
        self._irum = ""
        self._su = 0
        self._price = 0
        self._kumack = 0

    def get_code(self):
        return self._code
    def set_code(self, code):
        self._code = code
    code = property(get_code, set_code)

    def get_irum(self):
        return self._irum
    def set_irum(self, irum):
        self._irum = irum
    irum = property(get_irum, set_irum)

    def get_su(self):
        return self._su
    def set_su(self, su):
        self._su = su
    su = property(get_su, set_su)

    def get_price(self):
        return self._price
    def set_price(self, price):
        self._price = price
    price = property(get_price, set_price)

    def get_kumack(self):
        return self._kumack
    def set_kumack(self, kumack):
        self._kumack = kumack
    kumack = property(get_kumack, set_kumack)

    def input_sangpum(self,lst):
        while True:
            try:
                self._code = input("상품코드 입력 => ")
                if self._code == '-1':
                    return False
                elif self._code == '':
                    raise Exception('입력하지 않았습니다')
                else:
                    for item in lst:
                        if self._code == item.code:
                            raise Exception('코드가 중복됩니다. 다시 확인하세요')
            except Exception as e:
                print(e)
            else:
                break

        while True:
            try:
                self._irum = input("상품이름 입력 => ")
                if self._irum == '-1':
                    return False
                elif self._irum == '':
                    raise Exception('입력하지 않았습니다')
            except Exception as e:
                print(e)
            else:
                break

        stop = self.update_sangpum()
        return stop

    # self._su = int(input("국어 점수 입력 => "))
    # self._price = int(input("영어 점수 입력 => "))
    # self._kumack = int(input("수학 점수 입력 => "))

    # 추가 수정
    def update_sangpum(self):
        while True:
            try:
                su = int(input("상품갯수 입력 => "))
                if su == -1:
                    return False
                elif 0 > su:
                    raise Exception('갯수는 -가 될 수 없습니다 다시 입력하세요')
            except ValueError:
                print("정수로 다시 입력하세요")
            except Exception as e:
                print(e)
            else:
                break

        while True:
            try:
                price = int(input("상품단가 입력 => "))
                if price == -1:
                    return False
                elif 0 > price:
                    raise Exception('단가는 -가 될 수 없습니다 다시 입력하세요')
            except ValueError:
                print("정수로 다시 입력하세요")
            except Exception as e:
                print(e)
            else:
                break
        self._su = su
        self._price = price
        return True

    def process_sangpum(self):
        self._kumack = self._su * self._price

    def output_sangpum(self):
        print("%4s   %4s   %4d   %4d   %6d" %
              (self._code, self._irum, self._su,
               self._price, self._kumack))

if __name__ == "__main__":
    lst = []
    obj = Sangpum()
    obj.input_sangpum(lst)
    obj.process_sangpum()
    print("\n\t\t\t *** 상품관리 ***")
    print("=======================================")
    print("제품코드  제품명    수량    단가   판매금액")
    print("=======================================")
    obj.output_sangpum()
    print("=======================================")