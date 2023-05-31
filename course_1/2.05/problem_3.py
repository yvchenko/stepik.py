# Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения,
# которые встречаются в нём более одного раза.
#
# Для решения задачи может пригодиться метод sort списка.
#
# Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.


numbers = sorted([int(i) for i in input().split()])

length = len(numbers)
new = []

for i in range(length - 1):
    if numbers[i] == numbers[i + 1]:
        if numbers[i] not in new:
            new.append(numbers[i])

print(*new)
