import math
num1 = int(input("첫번째 숫자를 입력하세요: "))
num2 = int(input("두번째 숫자를 입력하세요: "))
if num1 > num2:
    num1, num2 = num2, num1
count = 0
for i in range(num1, num2+1):
    if i < 2:
        continue
    if i % 2 == 0 and i != 2:
        continue
    for j in range(3,int(math.sqrt(i))+1,2):
        if i % j == 0:
            break
    else:
        count+=1
        if count % 10 != 1:
            print(f"{i:4d}",end=" ")
        else:
            print(f"\n{i:4d}",end=" ")
print(f"\n총 소수의 갯수 = {count}")