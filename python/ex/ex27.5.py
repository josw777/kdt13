# lines = ['anonymously\n','compatibility\n','dashboard\n','experience\n','photography\n','spotlight\n','warehouse\n']
# with open('words.txt','w') as file:
#     file.writelines(lines)

lines = ['anonymously','compatibility','dashboard','experience','photography','spotlight','warehouse']
with open('words.txt','w') as file:
    for i in lines:
        file.write(f'{i}\n')

with open('words.txt','r') as file:
    count = 0
    for i in file:
        if len(i.strip('\n')) <= 10:
            count+=1
    print(count)

    print("===")

with open('words.txt','w') as file:
    file.write('Fortunately, however, '
               'for the reputation of Asteroid B-612, a Turkish dictator made a law that his subjects, '
               'under pain of death, should change to European costume. So in 1920 the astronomer gave '
               'his demonstration all over again, dressed with impressive style and elegance. '
               'And this time everybody accepted his report.')

with open('words.txt','r') as file:
    s = file.read()
    a = s.split()
    for i in a:
        if 'c' in i.strip('.,'):
            print(i.strip('.,'))