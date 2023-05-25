# Напишите простой калькулятор, который считывает с пользовательского ввода три строки:
# первое число, второе число и операцию, после чего применяет операцию к введённым числам
# ("первое число" "операция" "второе число") и выводит результат на экран.
#
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
#
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
#
# Обратите внимание, что на вход программе приходят вещественные числа.

number_1, number_2 = float(input()), float(input())
operator = input()

if (operator == "/" or operator == "mod" or operator == "div") and number_2 == 0.0:
    print("Деление на 0!")
elif operator == "+":
    print(number_1 + number_2)
elif operator == "-":
    print(number_1 - number_2)
elif operator == "/":
    print(number_1 / number_2)
elif operator == "*":
    print(number_1 * number_2)
elif operator == "mod":
    print(number_1 % number_2)
elif operator == "pow":
    print(number_1 ** number_2)
elif operator == "div":
    print(number_1 // number_2)