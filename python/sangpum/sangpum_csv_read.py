import os, csv
if os.path.exists('sangpum_csv_data.csv'):
    fp = open("sangpum_csv_data.csv",'r',encoding='utf8',newline='')
    reader = list(csv.reader(fp))
    lst = []
    for line in reader:
        dct = {}
        dct['code'] = line[0]
        dct['irum'] = line[1]
        dct['su'] = int(line[2])
        dct['price'] = int(line[3])

        dct['kumack'] = dct['su'] * dct['price']
        lst.append(dct)
    fp.close()

    print("\n\t\t\t *** 제품관리 ***")
    print("=======================================")
    print("제품코드  제품명    수량    단가   판매금액")
    print("=======================================")
    hap = 0
    for dct in lst:
        hap += dct['kumack']
        print("%4s   %4s   %4d   %4d   %6d" % (dct['code'], dct['irum'], dct['su'], dct['price'], dct['kumack']))
    print("=======================================")
    print("\t\t\t\t 총 판매금액: %7d" % hap)

else:
    print('파일이 존재하지 않습니다!!!')