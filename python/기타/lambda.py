def plus_ten(x):
    return x+10
print(list(map(plus_ten,[1,2,3])))

print("====")

print(list(map(lambda x: x+10,[1,2,3])))

print("====")

circle_area = lambda radius, pi: pi * (radius ** 2)
print(circle_area(3,3.14))

print("====")

print((lambda radius, pi: pi * (radius ** 2))(3,3.14))

print("=====")

def circle_area(radius, print_format):
    area = 3.14 * (radius ** 2)
    print_format(area)

if __name__ == "__main__":
    a = lambda x: print("결과값:", round(x,1))
    circle_area(3, a)
    circle_area(3, lambda x: print("결과값:", round(x, 2)))
