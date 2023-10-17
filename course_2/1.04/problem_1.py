# Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать
# поддержку создания пространств имен и добавление в них переменных.
#
# В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.
#
# Формат входных данных
# В первой строке дано число n (1 ≤ n ≤ 100) – число запросов.
# В каждой из следующих n строк дано по одному запросу.
# Запросы выполняются в порядке, в котором они даны во входных данных.
# Имена пространства имен и имена переменных представляют из себя строки длины не более 10,
# состоящие из строчных латинских букв.
#
# Формат выходных данных
# Для каждого запроса get выведите в отдельной строке его результат.

data = {'global': {'parent': None, 'variables': set()}}


def create(namespace, argument):
    data[namespace] = {'parent': argument, 'variables': set()}


def add(namespace, argument):
    data[namespace]['variables'].add(argument)


def get(namespace, argument):
    if argument in data[namespace]['variables']:
        return(namespace)
    else:
        if data[namespace]['parent'] == None:
            return None
        else:
            return(get(data[namespace]['parent'], argument))


for line in range(int(input())):
    command, namespace, argument = input().split()
    if command == 'create':
        create(namespace, argument)
    elif command == 'add':
        add(namespace, argument)
    else:
        print(get(namespace, argument))
