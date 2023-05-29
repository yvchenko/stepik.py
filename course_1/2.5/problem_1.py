# Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.
#
# Используйте метод split строки.

numbers = [int(i) for i in input().split()]

sum_all = 0

for element in numbers:
    sum_all += element

print(sum_all)