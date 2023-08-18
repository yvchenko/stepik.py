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


with open('problem_1_dataset.txt') as dataset:
    compressed = dataset.readline().strip()

split = []
part = ''

length = len(compressed)
expanded = []

for i in range(length):
    part += str(compressed[i])
    if not compressed[(i + 1) % length].isdigit():
        split.append(part)
        part = ''

for part in split:
    letter = ''
    amount = ''
    for character in part:
        if not character.isdigit():
            letter = character
        else:
            amount += character
    expanded.append(letter * int(amount))

with open('problem_1_done.txt', 'w') as done:
    for element in expanded:
        done.write(element)
