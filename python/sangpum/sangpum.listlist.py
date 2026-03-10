product=[]

while True:
    lst = list()

    lst.append(input("제품코드 입력 => "))
    if lst[0].lower() == 'exit':
        break
    lst.append(input("제품명 입력 => "))
    lst.append(int(input("수량 입력 => ")))
    lst.append(int(input("단가 입력 => ")))
    lst.append(lst[2] * lst[3])
    product.append(lst)
    print()

print("\n\t\t\t *** 제품관리 ***")
print("=======================================")
print("제품코드  제품명    수량    단가   판매금액")
print("=======================================")
hap = 0
for lst in product:
    hap += lst[4]
    print("%4s   %4s   %4d   %4d   %6d" % (lst[0], lst[1], lst[2], lst[3], lst[4]))
print("=======================================")
print("\t\t\t\t 총 판매금액: %7d"%hap)