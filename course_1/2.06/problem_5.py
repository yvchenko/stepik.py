# Выведите таблицу размером n×n, заполненную числами от 1 до n^2  по спирали, выходящей из левого верхнего угла
# и закрученной по часовой стрелке, как показано в примере (здесь n=5)

n = int(input())

matrix = [[0 for x in range(n)] for y in range(n)]

width = len(matrix[0])
height = len(matrix)

add = 0

x = 0
y = 0
number = 0

while True:
    number += 1
    matrix[y][x] = number
    if x == n - 1:
        y += 1
        break
    x += 1
while True:
    number += 1
    matrix[y][x] = number
    if y == n - 1:
        x -= 1
        break
    y += 1
while True:
    number += 1
    matrix[y][x] = number
    if x == 0:
        y -= 1
        break
    x -= 1
while True:
    number += 1
    matrix[y][x] = number
    if y == 1:
        x += 1
        break
    y -= 1




for y in range(height):
    for x in range(width):
        print(matrix[y][x], end='\t')
    print()
