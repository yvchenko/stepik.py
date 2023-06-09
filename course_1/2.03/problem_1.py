# Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками. Для тренировок
# ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.
#
# Напишите программу, на вход которой даются четыре числа a, b, c d, каждое в своей строке. Программа
# должна вывести фрагмент таблицы умножения для всех чисел отрезка
# [a;b] на все числа отрезка [c;d].
#
# Числа a, b, c и d являются натуральными и не превосходят 10, a ≤ b, c ≤ d.
#
# Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции.
# Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков —
# заголовочные столбец и строка таблицы.

a, b, c, d = int(input()), int(input()), int(input()), int(input())

for column in range(c, d + 1):
    print('\t', column, end='')

print('')

for row in range(a, b + 1):
    print(row, end='\t')
    for column in range(c, d + 1):
        print(row * column, end='\t')
    print('')
