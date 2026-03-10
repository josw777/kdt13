written_test = 75
coding_test = True

if written_test >= 80 and coding_test == True:
    print('합격')
else:
    print('불합격')

print("=====")

x = list(map(int,input().split()))
if 0<= x[0] <= 100 and 0<= x[1] <= 100 and 0<= x[2] <= 100 and 0<= x[3] <= 100:
    avg = sum(x) / len(x)
    if avg >= 80:
        print("합격")
    else:
        print("불합격")
else:
    print("잘못된 점수")