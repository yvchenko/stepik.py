# Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк. После
# последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).
#
# Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, y равен сумме
# элементов первой матрицы на позициях (i-1, y), (i+1, y), (i, y-1), (i, y+1). У крайних символов соседний элемент
# находится с противоположной стороны матрицы.
#
# В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

matrix = []
row_input = ''

while True:
    row_input = input()
    if row_input == 'end':
        break
    else:
        matrix.append([int(i) for i in row_input.split()])

width = len(matrix[0])
height = len(matrix)
new_matrix = []

for y in range(height):
    row = []
    for x in range(width):
        left = matrix[y][x - 1]
        if x + 1 == width:
            right = matrix[y][0]
        else:
            right = matrix[y][x + 1]
        up = matrix[y - 1][x]
        if y + 1 == height:
            down = matrix[0][x]
        else:
            down = matrix[y + 1][x]
        sum_all = left + right + up + down
        row.append(sum_all)
    new_matrix.append(row)

for y in range(height):
    for x in range(width):
        print(new_matrix[y][x], end=' ')
    print()
