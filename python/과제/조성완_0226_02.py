student = []
while True:
    lst = list()
    lst.append(input("학번을 입력하세요:"))
    if lst[0].lower() == 'exit':
        break
    lst.append(input("이름을 입력하세요:"))
    lst.append(int(input("국어 점수를 입력하세요:")))
    lst.append(int(input("영어 점수를 입력하세요:")))
    lst.append(int(input("수학 점수를 입력하세요:")))
    lst.append(lst[2]+lst[3]+lst[4])
    lst.append(lst[5]/3)
    student.append(lst)

print("\t\t\t***성적표***")
print("=====================================")
print("학번   이름   국어  영어  수학  총점  평균")
print("=====================================")
totalavg = 0
for lst in student:
    totalavg += lst[6]
    print("%4s %4s %4d %4d %4d %4d %5.2f"%(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6]))
print("=====================================")
print(f"\t학생수 : {len(student)}\t\t전체 평균 : {totalavg/len(student):.2f}")