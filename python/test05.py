import test04

print(test04.div(10,2))

x=15
print(f'{x:>15d}')

a = set("apple")
print(a)

a = {1,2,3,4}
b = {3,4,5,6}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
a.add(10)
print(a)
a.remove(10)
print(a)


print("=======")
a = {1,2,3,4}
b = a
print(a)
print(b)
a.add(10)
print(a)
print(b)
b=a.copy()
print(a)
print(b)
a.add(5)
print(a)
print(b)
