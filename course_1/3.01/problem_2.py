# Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него
# все нечётные значения, а чётные нацело делит на два. Функция не должна ничего возвращать,
# требуется только изменение переданного списка.

def modify_list(l):
    l[:] = [element // 2 for element in l if element % 2 == 0]
