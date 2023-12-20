# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
#
# Выведите одно число – количество вхождений строки t в строку s.

s, t = input(), input()


def count_string_occurrences(string, substring):
    occurrences = set()
    start = 0

    while start <= len(string):
        t_index = string.find(substring, start)
        occurrences.add(t_index)
        start += 1

    occurrences.remove(-1)
    return len(occurrences)


print(count_string_occurrences(s, t))
