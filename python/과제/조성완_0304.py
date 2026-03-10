import csv, os

def menu_title():
    print("*** 성적관리 ***")
    print("1. 성적정보 입력")
    print("2. 성적정보 출력")
    print("3. 성적정보 조회")
    print("4. 성적정보 수정")
    print("5. 성적정보 삭제")
    print("6. 프로그램 종료")
    print()

def grade_calculate(avg):
    if avg >= 90:
        grade = '수'
    elif avg >= 80:
        grade = '우'
    elif avg >= 70:
        grade = '미'
    elif avg >= 60:
        grade = '양'
    else:
        grade = '가'
    return grade

def input_sungjuk():
    fileexist = os.path.exists("sungjuk_data.csv")
    fp = open('sungjuk_data.csv','a',encoding='utf-8',newline='')
    fieldnames = ['hakbun','name','korean','english','math','total','avg','grade']
    writer = csv.DictWriter(fp,fieldnames=fieldnames)
    if not fileexist:
        writer.writeheader()
    dct = {}
    dct['hakbun'] = input("학번을 입력하세요 ==> ")
    dct['name'] = input("이름을 입력하세요 ==> ")
    dct['korean'] = int(input("국어 점수를 입력하세요 ==> "))
    dct['english'] = int(input("영어 점수를 입력하세요 ==> "))
    dct['math'] = int(input("수학 점수를 입력하세요 ==> "))
    dct['total'] = dct['korean'] + dct['english'] + dct['math']
    dct['avg'] = dct['total'] / 3
    # 등급(수,우,미,양,가)
    dct['grade'] = grade_calculate(dct['avg'])
    writer.writerow(dct)
    fp.close()
    print("\n성적 입력 성공\n")

def print_sungjuk():
    if os.path.exists('sungjuk_data.csv'):
        fp = open('sungjuk_data.csv','r',encoding='utf-8',newline='')
        lst = list(csv.DictReader(fp))
        print("\t\t\t***성적표***")
        print("==========================================")
        print("학번   이름   국어  영어  수학  총점  평균  등급")
        print("==========================================")
        total = 0
        for dct in lst:
            total += float(dct['avg'])
            print("%4s %4s %4d %4d %4d %4d %5.2f %3s" % (dct['hakbun'], dct['name'], int(dct['korean']),
                int(dct['english']), int(dct['math']), int(dct['total']), float(dct['avg']), dct['grade']))
        print("==========================================")
        print("\t\t\t학생수: %2d, 전체 평균: %3.2f\n" % (len(lst) , total/len(lst)))
        fp.close()
    else:
        print("\n파일이 존재하지 않습니다\n")

def search_sungjuk():
    if os.path.exists('sungjuk_data.csv'):
        fp = open('sungjuk_data.csv','r',encoding='utf-8',newline='')
        lst = list(csv.DictReader(fp))
        num = input("조회하고 싶은 학생의 학번을 입력하세요 ==> ")
        for dct in lst:
            if dct['hakbun'] == num:
                print("\n==========================================")
                print("학번   이름   국어  영어  수학  총점  평균  등급")
                print("==========================================")
                print("%4s %4s %4d %4d %4d %4d %5.2f %3s" % (dct['hakbun'], dct['name'], int(dct['korean']),
                    int(dct['english']), int(dct['math']), int(dct['total']), float(dct['avg']), dct['grade']))
                print("==========================================\n")
                break
        else:
            print("\n학생이 존재하지 않습니다\n")
        fp.close()
    else:
        print("\n파일이 존재하지 않습니다\n")

def update_sungjuk():
    if os.path.exists('sungjuk_data.csv'):
        fp = open('sungjuk_data.csv','r',encoding='utf-8',newline='')
        lst = list(csv.DictReader(fp))
        num = input("수정할 학생의 학번을 입력하세요 ==> ")
        numexist = False
        for dct in lst:
            if num == dct['hakbun']:
                dct['korean'] = int(input("국어 점수를 입력하세요 ==> "))
                dct['english'] = int(input("영어 점수를 입력하세요 ==> "))
                dct['math'] = int(input("수학 점수를 입력하세요 ==> "))
                dct['total'] = dct['korean'] + dct['english'] + dct['math']
                dct['avg'] = dct['total'] / 3
                # 등급(수,우,미,양,가)
                dct['grade'] = grade_calculate(dct['avg'])
                numexist = True
                break
        else:
            print("\n학생이 존재하지 않습니다\n")
        fp.close()
        if numexist:
            fp2 = open('sungjuk_data.csv','w',encoding='utf-8',newline='')
            fieldnames = ['hakbun','name','korean','english','math','total','avg','grade']
            writer = csv.DictWriter(fp2,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lst)
            fp2.close()
            print("\n성적을 수정하였습니다\n")
    else:
        print("\n파일이 존재하지 않습니다\n")

def delete_sungjuk():
    if os.path.exists('sungjuk_data.csv'):
        fp = open('sungjuk_data.csv','r',encoding='utf-8',newline='')
        lst = list(csv.DictReader(fp))
        num = input("삭제할 학생의 학번을 입력하세요 ==> ")
        numexist = False
        for dct in lst:
            if dct['hakbun'] == num:
                lst.remove(dct)
                numexist = True
                break
        else:
            print("\n학생이 존재하지 않습니다\n")
        fp.close()
        if numexist:
            fp2 = open('sungjuk_data.csv','w',encoding='utf-8',newline='')
            fieldnames = ['hakbun','name','korean','english','math','total','avg','grade']
            writer = csv.DictWriter(fp2,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lst)
            fp2.close()
            print("\n학생 정보를 삭제하였습니다\n")
    else:
        print("\n파일이 존재하지 않습니다\n")


if __name__ == "__main__":
    while True:
        menu_title()
        menu = input("메뉴를 선택하세요(1~6) ==> ")
        print()
        if menu == '1':
            input_sungjuk()
        elif menu == '2':
            print_sungjuk()
        elif menu == '3':
            search_sungjuk()
        elif menu == '4':
            update_sungjuk()
        elif menu == '5':
            delete_sungjuk()
        elif menu == '6':
            print("\n프로그램 종료\n")
            break
        else:
            print("\n메뉴를 다시 입력하세요!!\n")







