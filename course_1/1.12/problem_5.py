# Напишите программу, которая получает на вход три целых числа,
# по одному числу в строке, и выводит на консоль в три строки сначала
# максимальное, потом минимальное, после чего оставшееся число.
#
# На ввод могут подаваться и повторяющиеся числа.

a, b, c = int(input()), int(input()), int(input())

if a >= b and a >= c:
    max_number = a
elif b >= a and b >= c:
    max_number = b
else:
    max_number = c

if a <= b and a <= c:
    min_number = a
elif b <= a and b <= c:
    min_number = b
else:
    min_number = c

if max_number != a and min_number != a:
    rest = a
elif max_number != b and min_number != b:
    rest = b
elif max_number != c and min_number != c:
    rest = c

print(max_number)
print(min_number)
print(rest)
