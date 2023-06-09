# Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк. После
# последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).
#
# Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, y равен сумме
# элементов первой матрицы на позициях (i-1, y), (i+1, y), (i, y-1), (i, y+1). У крайних символов соседний элемент
# находится с противоположной стороны матрицы.
#
# В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

matrix = []

row_input = input()
while row_input != 'end':
    matrix.append([int(i) for i in row_input.split()])
    row_input = input()

for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        vertical = matrix[y - 1][x] + matrix[(y + 1) % len(matrix)][x]
        horizontal = matrix[y][x - 1] + matrix[y][(x + 1) % len(matrix[y])]
        print(vertical + horizontal, end=' ')
    print()
