# Напишите программу, которая получает на вход три целых числа,
# по одному числу в строке, и выводит на консоль в три строки сначала
# максимальное, потом минимальное, после чего оставшееся число.
#
# На ввод могут подаваться и повторяющиеся числа.

a, b, c = int(input()), int(input()), int(input())

if a <= b:
    a, b = b, a
if a <= c:
    a, c = c, a
if a <= b:
    a, b = b, a

print(a)
print(b)
print(c)