# a = [[[0 for col in range(3)] for row in range(4)] for depth in range(2)]
# print(a)
#
# print("=====")
#
# col, row = map(int, input().split())
# matrix = []
# for i in range(row):
#     matrix.append(list(input()))
#
# for i in range(row):
#     for j in range(col):
#         count = 0
#         if matrix[i][j] != '*':
#             if i != row-1:
#                 if '*' in matrix[i+1][j]:
#                     count += 1
#             if j != col-1:
#                 if '*' in matrix[i][j+1]:
#                     count += 1
#             if i != 0:
#                 if '*' in matrix[i-1][j]:
#                     count += 1
#             if j != 0:
#                 if '*' in matrix[i][j-1]:
#                     count += 1
#             if i != row - 1 and j != col - 1:
#                 if '*' in matrix[i + 1][j + 1]:
#                     count += 1
#             if i != row - 1 and j != 0:
#                 if '*' in matrix[i + 1][j - 1]:
#                     count += 1
#             if i != 0 and j != col - 1:
#                 if '*' in matrix[i - 1][j + 1]:
#                     count += 1
#             if i != 0 and j != 0:
#                 if '*' in matrix[i - 1][j - 1]:
#                     count += 1
#             print(count,end="")
#         else:
#             print(matrix[i][j],end='')
#     print()
#
#
# print("====")

col, row = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))

for i in range(row):
    for j in range(col):
        if matrix[i][j] != '*':
            matrix[i][j] = 0
            for y in range(i-1,i+2):
                for x in range(j-1,j+2):
                    if y<0 or x<0 or y>=row or x >= col:
                        continue
                    if matrix[y][x] == '*':
                        matrix[i][j] += 1
        print(matrix[i][j], end='')
    print()
