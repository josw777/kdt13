total = 0
eventotal = 0
oddtotal = 0
for item in range(1, 101, 1):
    total = total + item
    if item % 2 == 0:
        eventotal += item
    else:
        oddtotal += item
else:
    print("정상으로 실행되고 마지막에 실행") #break로 나오면 실행안됨

print("1부터 100까지 합은", total, "입니다.")
print("1부터 100까지 홀수합은", oddtotal, "입니다.")
print("1부터 100까지 짝수합은", eventotal, "입니다.")

print("======")

message = "Hello!"
messages = ["Hello World", "강릉원주대학교 정보기술공학과"]
numbers = (1,2,3)
polygon = {"triangle":2, "rectangle": 1, "line": 0}
color = {"red","green","blue"}
for item in message:
    print(item)
print('1.--------------')
for item in messages:
    print(item)
print('2.--------------')
for item in numbers:
    print(item)
print('3.--------------')
for item in polygon:
    print(item)
    print(polygon.get(item))
print('4.--------------')
for item in color:
    print(item)

# 리스트 내 for의 일반 문법
# 형식)[표현식 for 항목 in 반복가능객체 if 조건문]

a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

