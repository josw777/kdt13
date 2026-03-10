path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
print(path)
x = path.split('\\')
filename = x[-1]
print(filename)

print("=====")

a = input().split()
count = 0
for i in a:
    if i.strip(',.') == 'the':
        count += 1
print(count)

print('=====')

a = list(map(int,input().split(';')))
a.sort(reverse=True)

for i in a:
    print(f"{i:9,d}")


