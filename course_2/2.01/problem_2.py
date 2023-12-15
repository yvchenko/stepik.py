# Вам дано описание наследования классов исключений в следующем формате.
# <имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
# Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.
#
# Антон написал код, который выглядит следующим образом. Костя посмотрел на этот код и указал Антону на то,
# что некоторые исключения можно не ловить, так как ранее в коде будет пойман их предок. Но Антон не помнит
# какие исключения наследуются от каких. Помогите ему выйти из неловкого положения и напишите программу,
# которая будет определять обработку каких исключений можно удалить из кода.
#
# Важное примечание:
# В отличие от предыдущей задачи, типы исключений не созданы.
# Создавать классы исключений также не требуется
# Мы просим вас промоделировать этот процесс, и понять какие из исключений можно и не ловить, потому что
# мы уже ранее где-то поймали их предка.
#
# Формат входных данных
# В первой строке входных данных содержится целое число n - число классов исключений.
#
# В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется
# i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется
# сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.
#
# В следующей строке содержится число m - количество обрабатываемых исключений.
# Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
# Гарантируется, что никакое исключение не обрабатывается дважды.
#
# Формат выходных данных
# Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода, не изменив при этом
# поведение программы. Имена следует выводить в том же порядке, в котором они идут во входных данных.

exc_parents = {}
n = int(input())
exceptions = []


def is_parent(parent, child):
    if child == parent:
        return True

    for p in exc_parents.get(child):
        if is_parent(parent, p):
            return True

    return False


for line in range(n):
    command = input().split()
    if len(command) == 1:
        exc_parents[command[0]] = []
    else:
        exc_parents[command[0]] = command[2:]

m = int(input())

for line in range(m):
    command = input()
    for exception in exceptions:
        if is_parent(exception, command):
            print(command)
            break
    exceptions.append(command)
