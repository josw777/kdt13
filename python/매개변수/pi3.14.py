pi = 3.14

def circle_area(r):
    global pi   # 전역 변수 pi를 참조한다는 선언문
    pi = pi + 0.0015
    result = pi * (r ** 2)
    return result

if __name__ == "__main__":
    print("PI:", pi)
    print("반지름:", 3, "면적:", circle_area(3))
    print("PI:", pi)

# 스코프(Scope, 영역)란?
# - 변수나 객체 이름이 가지는 범위를 말한다.
# - 스코프를 벗어난 변수의 접근은 오류를 발생시킨다.
# - 이름을 찾는 순서는 Local(지역) -> Global(전역) -> Built-in(내장) 순이다.
# - Local은 이름이 만들어진 함수나 클래스 내부를 의미한다.
# - Global은 함수나 클래스 외부를 의미한다.
# - Built-in은 파이썬이 특별히 예약해둔 이름들을 말한다.
# - 이름을 찾는 순서는 Local 영역에서 찾고 없으면 Global 영역에서 찾는다. 거기에도 없으면 Built-in 영역에서 찾고 거기에도 없으면 NameError 오류를 발생시킨다.

# 함수의 종류
# - 내장(built-in) 함수(기본 함수)
# - 라이브러리 or 패키지 함수
# - 사용자 정의 함수
