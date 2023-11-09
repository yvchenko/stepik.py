# Вам дано описание наследования классов в следующем формате.
# <имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
# Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.
#
# Вам необходимо отвечать на запросы, является ли один класс предком другого класса
#
# Важное примечание:
# Создавать классы не требуется.
# Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
# Формат входных данных
# В первой строке входных данных содержится целое число n - число классов.
#
# В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов
# наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что
# класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса
# более одного раза.
#
# В следующей строке содержится число q - количество запросов.
#
# В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
# Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.
#
# Формат выходных данных
# Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2,
# и "No", если не является.

classes = {}
n = int(input())


def is_parent(parent, child):
    ind = 0
    if child not in classes.keys():
        return False
    elif child == parent:
        return True
    else:
        if parent in classes[child]:
            return True
        elif not classes[child]:
            return False
        else:
            if len(classes[child]) == 1:
                return is_parent(parent, classes[child][ind])
            else:
                while ind + 1 < len(classes[child]):
                    if not is_parent(parent, classes[child][ind]):
                        ind += 1
                    return is_parent(parent, classes[child][ind])
                return False


for line in range(n):
    command = input()
    if ':' not in command:
        child, parents = command, []
    else:
        child, parents = command.split(':')
        child = child.strip()
        parents = parents.strip().split()
    if child not in classes.keys():
        classes[child] = parents
    for parent in parents:
        if parent not in classes[child]:
            classes[child].extend(parents)

q = int(input())

for line in range(q):
    command = input()
    parent, child = command.split()
    if not is_parent(parent, child):
        print('No')
    else:
        print('Yes')
