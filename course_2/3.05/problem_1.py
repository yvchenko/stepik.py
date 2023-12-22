# В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
#
# Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический
# факт об этом числе.
#
# Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
# Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
#
# Пример запроса к интересному числу:
# http://numbersapi.com/31/math?json=true
#
# Пример запроса к скучному числу:
# http://numbersapi.com/999/math?json=true
import requests

with open("problem_1_dataset.txt") as f:
    numbers = f.read().strip().split("\n")

with open("problem_1_dataset_processed.txt", "w") as f:
    for number in numbers:
        trivia = requests.get(f"http://numbersapi.com/{number}/math?default=Boring").text
        if trivia == "Boring":
            f.write(trivia)
        else:
            f.write("Interesting")
        f.write("\n")