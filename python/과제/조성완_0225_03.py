dan1 = int(input("첫번째 숫자를 입력하시오 => "))
dan2 = int(input("두번째 숫자를 입력하시오 => "))
if dan1 > dan2:
    dan1, dan2 = dan2, dan1

for i in range(dan1,dan2+1):
    print(f" ** {i}단 **",end="   ")
print()
for i in range(1,10):
    for j in range(dan1,dan2+1):
       print(f"{j} * {i} = {j*i:2d}",end="   ")
    print()