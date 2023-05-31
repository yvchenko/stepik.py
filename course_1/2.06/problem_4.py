# Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк. После
# последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).
#
# Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме
# элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент
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

for j in range(height):
    row = []
    for i in range(width):
        left = matrix[j][i - 1]
        if i + 1 == width:
            right = matrix[j][0]
        else:
            right = matrix[j][i + 1]
        up = matrix[j - 1][i]
        if j + 1 == height:
            down = matrix[0][i]
        else:
            down = matrix[j + 1][i]
        sum_all = left + right + up + down
        row.append(sum_all)
    new_matrix.append(row)

for j in range(height):
    for i in range(width):
        print(new_matrix[j][i], end=' ')
    print()
