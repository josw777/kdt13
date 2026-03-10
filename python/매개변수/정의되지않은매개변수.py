# 정의되지 않은 매개변수(형식매개변수)
# - 정의되지 않은 매개변수는 딕셔너리 형식으로 전달되며, 함수에서 정의되지 않은 매개변수를 받을 때는 인자 앞에 **을 붙여서 전달 받는다.
# - 함수를 호출할 때(실매개변수)키워드 형식으로 전달 받는다.
# - 일반인자, 가변인자, 정의되지 않은 인자가 있을 경우 함수에서는 반드시 일반인자, 가변인자, 정의되지 않은 인자 순으로 인자들을 전달하고 받아야 한다.

def add(a, **b): # **b: 정의되지 않은 매개변수
    hap = a
    for val in b:
        hap += b[val]
    return hap

print(add(10,mbc=20,kbs=30)) # 함수 호출문, 키워드 매개변수를 인자로 전달
print(add(10,one=20,two=30,three=40)) # 함수 호출문

print("====")

def add(a, *b, **c):
    hap = a
    for val in b:
        hap += val
    for val in c:
        hap += c[val]
    return hap

print(add(10,20,30, mbc=40,kbs=50)) # 함수 호출문
print(add(10, 20,30,40, one=50,two=60,three=70)) # 함수 호출문