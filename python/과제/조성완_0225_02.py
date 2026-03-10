dan1 = int(input("첫번째 숫자를 입력하시오 => "))
dan2 = int(input("두번째 숫자를 입력하시오 => "))
if dan1 >= dan2:
    dan11 = dan1
    dan22 = dan2
else:
    dan11 = dan2
    dan22 = dan1
for i in range(dan22,dan11+1):
    print(f"\n ** {i}단 **")
    for j in range(1,10):
        print(f"{i} * {j} = {i * j}")
