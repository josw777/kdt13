for i in range(5):
    for j in range(5):
        if j<i:
            print(end=" ")
        else:
            print("*",end="")
    print()

print("====")

x = int(input())
for i in range(1,x+1):
    for j in range(1,x+1):
        if j <= (x-i):
            print(end=' ')
        else:
            print('*',end='')
    for j in range(i-1):
        print("*",end='')
    print()

print("=====")

height = int(input())
for i in range(height):
    for j in reversed(range(height)):
        if j > i:
            print(' ', end='')
        else:
            print('*', end='')
    for j in range(height):
        if j < i:
            print('*', end='')
    print()