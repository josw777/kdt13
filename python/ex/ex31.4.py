def is_palindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    print(word[1:-1])
    return is_palindrome(word[1:-1])

print(is_palindrome('hello'))
print(is_palindrome('level'))

print("===")

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1)+fib(n-2)

n = int(input())
print(fib(n))