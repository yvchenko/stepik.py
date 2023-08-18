# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
#
# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
#
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/
#
# Загрузите содержимое последнего файла из набора, как ответ на это задание.
import requests

with open('problem_2_dataset.txt') as source:
    address = source.readline().strip()

domain = 'https://stepic.org/media/attachments/course67/3.6.3/'
file_content = requests.get(address).text

with open('problem_2_done.txt', 'w') as done:
    while "We" not in file_content:
        new_address = domain + file_content
        file_content = requests.get(new_address).text
    done.write(file_content + '\n')
