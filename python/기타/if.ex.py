grade = float(input("총 평점을 입력해 주세요: "))
if grade >= 4.3:
    print("당신은 장학금 수여 대상자 입니다.")
    print("축하합니다.")
print("공부 열심히 하세요.")
print("=========")

data = int(input("숫자를 입력하세요: "))
if data % 2 == 0:
    print("입력된 값은 짝수입니다.")
    if data % 4 == 0:
        print("입력된 값은 4의 배수입니다.")
    else:
        print("입력된 값은 4의 배수가 아닙니다.")
else:
    print("입력된 값은 홀수입니다.")
    if data % 3 == 0:
        print("입력된 값은 3의 배수입니다.")
    else:
        print("입력된 값은 3의 배수가 아닙니다.")
print("The End...")

score = int(input("총점을 입력해 주세요: "))
if score >= 90:
    print("수")
elif 80 <= score < 90:
    print("우")
elif 70 <= score < 80:
    print("미")
elif 60 <= score < 70:
    print("양")
else:
    print("가")
