a = ['alpha','bravo','charlie','delta','echo','foxtrot','golf','hotel','india']
b = [i for i in a if len(i)==5]
print(b)

print("====")

num1, num2 = map(int,input().split())
lst = [2**i for i in range(num1,num2+1)]
del lst[1]
del lst[-2]
print(lst)