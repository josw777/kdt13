file = open('hello.txt','wt')
s = file.write('Hello Python!!!')
file.close()

file = open('hello.txt','rt')
s = file.read()         # 문자열 반환, string타입
print(s)
file.close()            # readline(), readlines()

with open('hello.txt','rt') as file:
    s = file.read()
    print(s)

with open('hello.txt','w') as file:
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))

lines = ['안녕하세요.\n','파이썬\n','코딩 도장입니다.\n']
with open('hello.txt','w',encoding='utf8') as file:
    file.writelines(lines)

with open('hello.txt','r',encoding='utf8') as file:
    lines = file.readlines()
    print(lines)

with open('hello.txt','r',encoding='utf8') as file:
    line = None
    while line != '':
        line = file.readline()
        print(line.strip('\n'), end='')

with open('hello.txt','r',encoding='utf8') as file:
    for line in file:
        print(line.strip('\n'))