# import os.sys
# print(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "
# sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))
from python.과제.sungjuk_class import Sungjuk

lst = []

def menu_title():
    print("*** 성적관리 ***")
    print("1. 성적정보 입력")
    print("2. 성적정보 출력")
    print("3. 성적정보 조회")
    print("4. 성적정보 수정")
    print("5. 성적정보 삭제")
    print("6. 프로그램 종료")
    print()

def input_sungjuk():
    obj = Sungjuk()
    obj.input_sungjuk()
    obj.process_sungjuk()
    lst.append(obj)
    print("\n성적 입력 성공!!!\n")

def print_sungjuk():
    if len(lst) == 0:
        print("\n출력할 데이터가 없음!!\n")
        return
    else:
        print("\t\t\t***성적표***")
        print("==========================================")
        print("학번   이름   국어  영어  수학  총점  평균  등급")
        print("==========================================")
        tot_avg = 0
        for obj in lst:
            obj.output_sungjuk()
            tot_avg += obj.avg  # obj.avg => obj.get_avg()
        print("==========================================")
        print("\t\t\t학생수: %2d, 전체 평균: %3.2f\n" % (len(lst), tot_avg / len(lst)))

def search_sungjuk():
    if len(lst) == 0:
        print("\n출력할 데이터가 없음!!\n")
        return
    else:
        num = input("조회하고 싶은 학생의 학번을 입력하세요 ==> ")
        for obj in lst:
            if obj.hakbun == num:
                print("\n==========================================")
                print("학번   이름   국어  영어  수학  총점  평균  등급")
                print("==========================================")
                obj.output_sungjuk()
                print("==========================================\n")
                break
        else:
            print("\n학생이 존재하지 않습니다\n")

def update_sungjuk():
    if len(lst) == 0:
        print("\n출력할 데이터가 없음!!\n")
        return
    else:
        num = input("수정할 학생의 학번을 입력하세요 ==> ")
        for obj in lst:
            if obj.hakbun == num:
                obj.update_sungjuk()
                obj.process_sungjuk()
                print("\n성적을 수정하였습니다\n")
                break
        else:
            print("\n학생이 존재하지 않습니다\n")

def delete_sungjuk():
    if len(lst) == 0:
        print("\n출력할 데이터가 없음!!\n")
        return
    else:
        num = input("삭제할 학생의 학번을 입력하세요 ==> ")
        for obj in lst:
            if obj.hakbun == num:
                lst.remove(obj)
                print("\n학생 정보를 삭제하였습니다\n")
                break
        else:
            print("\n학생이 존재하지 않습니다\n")

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