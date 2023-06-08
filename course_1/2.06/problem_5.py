# Выведите таблицу размером n×n, заполненную числами от 1 до n^2  по спирали, выходящей из левого верхнего угла
# и закрученной по часовой стрелке, как показано в примере (здесь n=5)

n = int(input())

matrix = [[0 for x in range(n)] for y in range(n)]

width = len(matrix[0])
height = len(matrix)

x = 0
y = 0

number = 0

lower_boundary = 0
upper_boundary = n - 1

while number < n ** 2:
    if number < n ** 2:
        while True:
            number += 1
            matrix[y][x] = number
            if x == upper_boundary:
                y += 1
                break
            x += 1
    if number < n ** 2:
        while True:
            number += 1
            matrix[y][x] = number
            if y == upper_boundary:
                x -= 1
                break
            y += 1
    if number < n ** 2:
        while True:
            number += 1
            matrix[y][x] = number
            if x == lower_boundary:
                y -= 1
                break
            x -= 1
    lower_boundary += 1
    upper_boundary -= 1
    if number < n ** 2:
        while True:
            number += 1
            matrix[y][x] = number
            if y == lower_boundary:
                x += 1
                break
            y -= 1

for y in range(height):
    for x in range(width):
        print(matrix[y][x], end='\t')
    print()
