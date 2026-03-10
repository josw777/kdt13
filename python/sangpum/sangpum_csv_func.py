# 제품코드, 제품명, 수량, 단가를 입력받아 금액을 계산하여 출력하는 프로그램
import csv, os

def menu_title():
    print("*** 제품관리 ***")
    print("1. 제품정보 입력")
    print("2. 제품정보 출력")
    print("3. 제품정보 조회")
    print("4. 제품정보 수정")
    print("5. 제품정보 삭제")
    print("6. 프로그램 종료")
    print()

def input_data():
    if os.path.exists('sangpum_csvfunc_data.csv'):
        fp = open("sangpum_csvfunc_data.csv", 'at', encoding='utf8', newline='')
        fieldnames = ["code", "irum", "su", "price", "kumack"]
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
    else:
        fp = open("sangpum_csvfunc_data.csv", 'at', encoding='utf8', newline='')
        fieldnames = ["code", "irum", "su", "price", "kumack"]
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()

    # fileexist = os.path.exists('sangpum_csvfunc_data.csv')
    # fp = open("sangpum_csvfunc_data.csv", 'at', encoding='utf8', newline='')
    # fieldnames = ["code", "irum", "su", "price", "kumack"]
    # writer = csv.DictWriter(fp, fieldnames=fieldnames)
    # if not fileexist:
    #     writer.writeheader()

    dct = {}
    dct['code'] = input("제품코드 입력 => ")
    dct['irum'] = input("제품명 입력 => ")
    dct['su'] = int(input("수량 입력 => "))
    dct['price'] = int(input("단가 입력 => "))
    dct['kumack'] = dct['su'] * dct['price']
    writer.writerow(dct)
    fp.close()
    print("\n제품정보 입력 성공!!\n")

def print_data():
    if os.path.exists('sangpum_csvfunc_data.csv'):
        fp = open("sangpum_csvfunc_data.csv", 'r', encoding='utf8', newline='')
        lst = list(csv.DictReader(fp))
        print("\n\t\t\t *** 제품관리 ***")
        print("=======================================")
        print("제품코드  제품명    수량    단가   판매금액")
        print("=======================================")
        hap = 0
        for data in lst:
            hap += int(data["kumack"])
            print("%4s   %4s   %4d   %4d   %6d" % (data["code"], data["irum"], int(data["su"]), int(data["price"]), int(data["kumack"])))
        print("=======================================")
        print("\t\t\t\t 총 판매금액: %7d\n" % hap)
        fp.close()
    else:
        print('\n출력할 제품 정보가 없음!!!\n')

def search_data():
    # 제품코드를 입력 받아 해당 제품 정보를 출력한다.
    if os.path.exists('sangpum_csvfunc_data.csv'):
        fp = open("sangpum_csvfunc_data.csv", 'r', encoding='utf8', newline='')
        lst = list(csv.DictReader(fp))
        sangpum = input("찾는 제품코드를 입력하세요 ==> ")
        for data in lst:
            if data["code"] == sangpum:
                print("\n=======================================")
                print("제품코드  제품명    수량    단가   판매금액")
                print("=======================================")
                print("%4s   %4s   %4d   %4d   %6d" % (data["code"], data["irum"], int(data["su"]), int(data["price"]), int(data["kumack"])))
                print("=======================================\n")
                break
        else:
            print("\n제품이 존재하지 않음\n")
        fp.close()
    else:
        print('\n출력할 제품 정보가 없음!!!\n')

def update_data():
    # 제품코드를 입력받아 일치하는 데이터를 찾아서 수량과 단가를 입력받아 금액을 수정 후 파일 전체를 재저장
    if os.path.exists('sangpum_csvfunc_data.csv'):
        fp = open("sangpum_csvfunc_data.csv", 'r', encoding='utf8', newline='')
        lst = list(csv.DictReader(fp))
        sangpum = input("업데이트할 제품의 제품코드를 입력하세요 ==> ")
        sangpumin = False
        for data in lst:
            if data["code"] == sangpum:
                data['su'] = int(input("수량 입력 => "))
                data['price'] = int(input("단가 입력 => "))
                data['kumack'] = data['su'] * data['price']
                sangpumin = True
                break
        else:
            print("\n제품이 존재하지 않음\n")
        fp.close()
        if sangpumin:
            fp = open("sangpum_csvfunc_data.csv", 'wt', encoding='utf8', newline='')
            fieldnames = ["code", "irum", "su", "price", "kumack"]
            writer = csv.DictWriter(fp, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lst)
            # for i in lst:
            #     writer.writerow(i)
            fp.close()
            print("\n제품정보 변경 성공!!\n")
    else:
        print('\n출력할 제품 정보가 없음!!!\n')

def delete_data():
    if os.path.exists('sangpum_csvfunc_data.csv'):
        fp = open("sangpum_csvfunc_data.csv", 'r', encoding='utf8', newline='')
        lst = list(csv.DictReader(fp))
        sangpum = input("삭제할 제품의 제품코드를 입력하세요 ==> ")
        sangpumin = False
        for data in lst:
            if data["code"] == sangpum:
                lst.remove(data)
                sangpumin = True
                break
        else:
            print("\n제품이 존재하지 않음\n")
        fp.close()
        if sangpumin:
            fp = open("sangpum_csvfunc_data.csv", 'wt', encoding='utf8', newline='')
            fieldnames = ["code", "irum", "su", "price", "kumack"]
            writer = csv.DictWriter(fp, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lst)
            # for i in lst:
            #     writer.writerow(i)
            fp.close()
            print("\n제품정보 삭제 성공!!\n")
    else:
        print('\n출력할 제품 정보가 없음!!!\n')

if __name__ == "__main__":
    while True:
        menu_title()
        menu = int(input("메뉴를 선택하세요(1~6) ==> "))
        if menu == 1:
            input_data()
        elif menu == 2:
            print_data()
        elif menu == 3:
            search_data()
        elif menu == 4:
            update_data()
        elif menu == 5:
            delete_data()
        elif menu == 6:
            print("\n프로그램 종료\n")
            break
        else:
            print("\n메뉴를 다시 입력하세요!!\n")