# Выведите таблицу размером n×n, заполненную числами от 1 до n^2  по спирали, выходящей из левого верхнего угла
# и закрученной по часовой стрелке, как показано в примере (здесь n=5)

n = int(input())

matrix = [[0 for x in range(n)] for y in range(n)]

width = len(matrix[0])
height = len(matrix)

# add = 0
#
# l = 0
x = 0
y = 0

for number in range(n ** 2):
    number += 1
    if x < n:
        matrix[y][x] = number
        x += 1
    else:
        x -= 1
        if y + 1 < n:
            matrix[y][x] = number
            y += 1
        else:
            y -= 1
            if x < n:
                matrix[y][x] = number
                x -= 1


# for y in range(n):
#     for x in range(n):
#         add += 1
#         l = 0
#         m = n
#         ax = x
#         ay = y
#         if ax < m:
#             ax += 1
#         else:
#             ay += 1
#         if ay < n and ax < n:
#             matrix[ay][ax] += add

# for y in range(height):
#     for x in range(width):
#         add += 1
#         matrix[y][x] += add


for y in range(height):
    for x in range(width):
        print(matrix[y][x], end=' ')
    print()
