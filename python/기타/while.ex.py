# 1.초기식 i=0
# 2.조건식 i<100
# 3.반복처리할 내용 print()
# 4.증감식 i+=1

# import random    # random 모듈을 가져옴
from random import randint

i = 0
while i != 3:                   # 3이 아닐 때 계속 반복
    i = randint(1,6)      # randint를 사용하여 1과 6 사이의 난수를 생성
    print(i)

#1에서부터 100까지 숫자중 홀수의 합과 짝수의 합을 구해서 출력하시오.
#단 while문을 사용한다.
i = 1 # 초기식
evensum = 0
oddsum = 0
while i<=100: # 조건식
    if i % 2 == 0: # 반복 처리할 내용
        evensum+=i
    else:
        oddsum+=i
    i+=1 # 증감식
else:
    print("홀수의 합: ",oddsum)     #break로 나가지 않았을 때 실행
    print("짝수의 합: ",evensum)