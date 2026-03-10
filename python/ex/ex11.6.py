year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
population = [10249679, 10195318, 10143645, 10103233,
              10022181, 9930616, 9857426, 9838892]
print(year[-3:])
print(population[-3:])

print("=======")

n = -32, 75, 97, -10, 9, 32, 4, -15, 0 ,76, 14, 2
print(n[1::2])

print("=======")

x = input().split()
del x[-5:]
print(tuple(x))

print("======")

a = input()
b = input()
print(a[1::2]+b[::2])