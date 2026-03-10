def add_sub(a,b):
    return a+b, a-b

print(add_sub(10,20))

x,y = add_sub(10,20)
print(x,y)

print("====")

def mul(a,b):    # a,b: 지역 변수
    c = a*b      # c: 지역 변수
    return c

def add(a,b):    # a,b: 지역 변수
    c = a+b      # c: 지역 변수
    print(c)
    d = mul(a,b) # d: 지역 변수
    print(d)
    #return

x=10 # 전역 변수
y=20 # 전역 변수
add(x,y)

print("====")

def circle_area(r): # r: 지역 변수
    result = 3.14 * (r ** 2) # result: 지역 변수
    return result

if __name__ == "__main__":
    radius = 3 # 전역 변수, 다른 모듈에서 import해서 사용 불가능
    area = circle_area(radius) # 전역 변수
    print("반지름: %d, 면적: %.2f" % (radius,area))
    #print(r)

print("====")

pi = 3.1415 # 다른 모듈에서 import해서 이 전역변수를 사용 가능

def circle_area_with_pi(r):
    # circle_area_with_pi의 local 영역
    pi = 3.14
    result = pi * (r ** 2)
    return result

def circle_area_without_pi(r):
    # circle_area_without_pi의 local 영역
    result = pi * (r ** 2)
    return result

def sum_areas():
    results = [circle_area_with_pi(3), circle_area_without_pi(3)]
    return sum(results) # built-in의 sum 함수를 호출

if __name__ == "__main__":
    print("PI:", pi)
    print("반지름:", 3, "면적:", circle_area_with_pi(3))
    print("반지름:", 3, "면적:", circle_area_without_pi(3))
    print(sum_areas())

