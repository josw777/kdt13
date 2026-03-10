import math

def input_num():
    num1 = int(input("첫번째 숫자를 입력하세요: "))
    num2 = int(input("두번째 숫자를 입력하세요: "))
    return num1, num2

def min_max_num(num1,num2):
    if num1 > num2:
        num1, num2 = num2, num1
    return num1, num2

def prime_num(num1,num2):
    count = 0
    for i in range(num1, num2 + 1):
        if i < 2:
            continue
        if i % 2 == 0 and i != 2:
            continue
        for j in range(3, int(math.sqrt(i)) + 1, 2):
            if i % j == 0:
                break
        else:
            count += 1
            if count % 10 != 1:
                print(f"{i:4d}", end=" ")
            else:
                print(f"\n{i:4d}", end=" ")
    return count

def totalprime_num(count):
    print(f"\n총 소수의 갯수 = {count}")

if __name__ == "__main__":
    num1, num2 = input_num()
    num1, num2 = min_max_num(num1,num2)
    count = prime_num(num1,num2)
    totalprime_num(count)