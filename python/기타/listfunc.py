lst = [10, 20, 30]
print(lst)
lst2 = lst
print(lst2)
lst[0] = 50
print(lst)
lst2 = lst
print(lst2)

a = [1,2,3,4]
a.append(5)
print(a)
a.append([6,7])
print(a)
b = [4,1,3,2]
print(b)
b.sort()
print(b)
b.reverse()
print(b)
print("===")

a = [1, 2, 3]
a.insert(1, 4)
print(a)
a.remove(1)
print(a)
print(a.pop())
print(a)
a = [1,2,2,2,3,3,4]
print(a.count(2))
a.extend([5,6,7])
print(a)
print("====")

a = [10, 10.5, "Python"]
print(a)
print(a[0])
print(a[-1])
print(a[-2])
print(a[2][0])
a[2] = "java"    #리스트 내의 객체 자체를 바꿈
print(a)
# a[2][0] = 'J'   #str은 값을 변경할 수 없음
# print(a)
print("====")

a = [1,2,3,4,5]
print(a)
b = a[:2]
print(b)
c = a[2:]
print(c)
d = a[-1:]
print(d)
e = a[-3:]
print(e)
print("====")

t1 = ()
print(type(t1))
t2 = (10,)
print(type(t2))
print(t2)
t3 = (1,2,3)
print(t3)
t4 = 1,2,3  #packing
print(t4)
x,y,z = t4 #unpacking
print(x,y,z)
t5 = (1,10.5,"Python")
print(t5)
print(t5[2])
print(t5[2][0:2])
#t5[2] = "Java"
print("====")

a = (1,2,3,[4,5])
a[3][0] = 10
print(a)






