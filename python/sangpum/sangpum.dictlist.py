lst = []

while True:
    dct = {}
    dct['code'] = input("제품코드 입력 => ")
    if dct['code'].lower() == 'exit':
        break
    dct['irum'] = input("제품명 입력 => ")
    dct['su'] = int(input("수량 입력 => "))
    dct['price'] = int(input("단가 입력 => "))
    dct['kumack'] = dct['su'] * dct['price']
    lst.append(dct)
    print()

print("\n\t\t\t *** 제품관리 ***")
print("=======================================")
print("제품코드  제품명    수량    단가   판매금액")
print("=======================================")
hap = 0
for dct in lst:
    hap += dct['kumack']
    print("%4s   %4s   %4d   %4d   %6d" % (dct['code'], dct['irum'], dct['su'], dct['price'], dct['kumack']))
print("=======================================")
print("\t\t\t\t 총 판매금액: %7d"%hap)