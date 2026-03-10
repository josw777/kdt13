lst = []
while True:
    dct = {}
    dct['hakbun'] = input("학번을 입력하세요:")
    if dct['hakbun'].lower() == 'exit':
        break
    dct['name'] = input("이름을 입력하세요:")
    dct['korean'] = int(input("국어 점수를 입력하세요:"))
    dct['english'] = int(input("영어 점수를 입력하세요:"))
    dct['math'] = int(input("수학 점수를 입력하세요:"))
    dct['total'] = dct['korean'] + dct['english'] + dct['math']
    dct['average'] = dct['total']/3
    lst.append(dct)

print("\t\t\t***성적표***")
print("==========================================")
print("학번   이름   국어  영어  수학  총점  평균")
print("==========================================")
totalavg = 0
for dct in lst:
    totalavg += dct['average']
    print("%4s %4s %4d %4d %4d %4d %5.2f"%(dct['hakbun'], dct['name'], dct['korean'], dct['english'], dct['math'], dct['total'], dct['average']))
print("==========================================")
print(f"\t학생수 : {len(lst)}\t\t전체 평균 : {totalavg/len(lst):.2f}")