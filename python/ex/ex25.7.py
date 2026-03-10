maria = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
average =  sum(maria.values())/len(maria)
print(average)

print("=====")

keys = input().split()
values = map(int,input().split())
x=dict(zip(keys,values))
x.pop('delta')
x = {key: value for key, value in x.items() if value != 30}
print(x)