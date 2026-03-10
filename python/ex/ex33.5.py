def counter():
    i = 0
    def count():
        nonlocal i
        i += 1
        return i
    return count

c = counter()
for i in range(10):
    print(c(), end=' ')

print('\n====')

def countdown(n):
    a = n+1
    def count():
        nonlocal a
        a -= 1
        return a
    return count

n = int(input())
c = countdown(n)
for i in range(n):
    print(c(),end=' ')