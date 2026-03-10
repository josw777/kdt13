# 제품코드, 제품명, 수량, 단가를 입력받아 금액을 계산하여 출력하는 프로그램
# 입력 받은 데이터는 sangpum_data.txt에 csv(,로 구분)형식으로 저장

fp = open("sangpum_data.txt",'w',encoding='utf8')   # w(write), r(read), a(append) + t(text), b(binary)
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

    fp.write(dct['code'] + ',' + dct['irum'] + ',' + str(dct['su'])
             + ',' + str(dct['price']) + '\n')
    print()

fp.close()

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