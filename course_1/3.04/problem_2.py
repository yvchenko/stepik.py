# Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно
# смотреть, как, например, на наиболее часто используемые.
#
# Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит
# самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько,
# вывести лексикографически первое (можно использовать оператор < для строк).
#
# В качестве ответа укажите вывод программы, а не саму программу.
#
# Слова, написанные в разных регистрах, считаются одинаковыми.

with open('problem_2_dataset.txt') as dataset:
    words = [i for i in dataset.read().lower().split()]

counted = {}
for word in words:
    if word not in counted:
        counted[word] = 1
    else:
        counted[word] += 1

with open('problem_2_done.txt', 'w') as done:
    amount = max([counted[key] for key in counted])
    word = min({key for key in counted if counted[key] == amount})
    done.write(str(word) + ' ' + str(amount))
