# На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление
# исходной строки обратно.
#
# Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования
# повторов, и производит обратную операцию, получая исходный текст.
#
# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
#
# В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
#
# Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется
# ссылка "download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными данными к
# себе на компьютер. Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл, который
# при этом у вас получится, надо отправить в качестве ответа на эту задачу.

import re

with open(file='problem_1_dataset.txt') as dataset:
    compressed = dataset.readline()

digits = '0123456789'

split = []
part = ''

length = len(compressed)

for i in range(length):
    part += str(compressed[i])
    if compressed[(i + 1) % length] not in digits:
        split.append(part)
        part = ''

with open('problem_1_done.txt', 'w') as done:
    for part in split:
        letter = ''
        amount = ''
        for character in part:
            if character not in digits:
                letter = character
            else:
                amount += character
        done.write(letter * int(amount))