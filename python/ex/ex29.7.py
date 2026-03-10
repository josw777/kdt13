x = 10
y = 3

def get_quotient_remainder(x,y):
    return x//y, x%y

quotient, remainder = get_quotient_remainder(x,y)
print('몫: {0}, 나머지: {1}'.format(quotient,remainder))

print("====")

x,y = map(int,input().split())
def calc(a,b):
    return a+b,a-b,a*b,a/b

a,s,m,d =calc(x,y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a,s,m,d))