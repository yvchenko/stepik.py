# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
#
# Выведите одно число – количество вхождений строки t в строку s.

s, t = input(), input()


def find_string(s, t):
    start = 0
    while start <= len(s):
        t_index = s.find(t, start)
        yield t_index
        start += 1


def count_string_occurrences(s, t):
    occurrences = set(find_string(s, t))
    occurrences.remove(-1)
    return len(occurrences)


print(count_string_occurrences(s, t))
