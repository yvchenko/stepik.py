# Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
# Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
#
# Попробуем написать подобную систему.
#
# На вход программе первой строкой передаётся количество d известных нам слов, после чего на d строках
# указываются эти слова. Затем передаётся количество l строк текста для проверки, после чего  l строк текста.
#
# Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

d = int(input())

dictionary = []
errors = set()

for word in range(d):
    word = input().lower()
    dictionary.append(word)

l = int(input())

for row in range(l):
    row = input().lower().split()
    for word in row:
        if word not in dictionary:
            errors.add(word)

[print(error) for error in errors]
