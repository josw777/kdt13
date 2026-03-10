files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
print(list(filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1, files)))

print("====")

files=input().split()
print(list(map(lambda x: f'{int(x.split(".")[0]):03d}.{x.split(".")[1]}' ,files)))