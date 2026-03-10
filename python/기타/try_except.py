# def ten_div(x):
#     return 10 / x
#
# print(ten_div(10))
# print(ten_div(0))

try:
    #x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
    print(y)
except: # 예외가 발생했을 때 실행됨
    print('예외가 발생했습니다.')

print("====")

y = [10, 20, 30]

try:
   # index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index]/ x)
except ZeroDivisionError as e:   # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.', e.args[0])
except IndexError as e:  # 범위를 벗어난 인덱스에 접근하여 에러가 발생했을 때 실행됨
    print('잘못된 인덱스입니다.', e.args)
except Exception as e:        # 남은 예외를 모두 처리해야하므로 제일 뒤에 와야한다. # Exception class가 부모 클래스이므로 제일 뒤에 온다.
    print("나머지 예외 처리",e)

print("====")

try:
    x = int(input("나눌 숫자를 입력하세요: "))
    y = 10 / x
except ZeroDivisionError:   # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print("숫자를 0으로 나눌 수 없습니다.")
except: # 앞에서 기술된 예외를 제외한 나머지 모든 예외 처리
    print("모든 예외 처리")
else:   # try의 코드에서 예외가 발생하지 않았을 때 실행됨
    print(y)
finally:    # 예외 발생 여부와 상관없이 항상 실행됨
    print('코드 실행이 끝났습니다')

print("====")

try:
   # x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:
        raise Exception('3의 배수가 아닙니다.')
    print(x)
except Exception as e:
    print('예외가 발생했습니다.',e)

print("====")

def three_multiple():
    #x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:
        raise Exception('3의 배수가 아닙니다.')
    print(x)

try:
    three_multiple()
except Exception as e:
    print('예외가 발생했습니다.',e)

print("====")

def three_multiple():
    try:
        #x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:
            raise Exception('3의 배수가 아닙니다.')
        print(x)
    except Exception as e:
        print('three_multiple 함수에서 예외가 발생했습니다.',e)
        raise

try:
    three_multiple()
except Exception as e:
    print('스크립트 파일에서 예외가 발생했습니다.',e)

print("====")

class NotThreeMultipleError(Exception):
    def __init__(self):
        super().__init__("3의 배수가 아닙니다.")

def three_multiple():
    try:
        x = int(input("3의 배수를 입력하세요: "))
        if x % 3 != 0:
            raise NotThreeMultipleError
        print(x)
    except NotThreeMultipleError as e:
        print('예외가 발생했습니다.1',e)
    except Exception as e:
        print('예외가 발생했습니다.2',e)

three_multiple()