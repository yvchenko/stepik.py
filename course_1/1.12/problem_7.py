# Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет,
# счастливый ли ему попался. Билет считается счастливым, если сумма первых трех цифр
# совпадает с суммой последних трех цифр номера билета.
#
# Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу, которая
# проверит равенство сумм и выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.
#
# На вход программе подаётся строка из шести цифр.
#
# Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.

ticket = int(input())

a = ticket // 100000
b = ticket // 10000 % 10
c = ticket // 1000 % 10
d = ticket // 100 % 10
e = ticket // 10 % 10
f = ticket % 10

if a + b + c == d + e + f:
    print("Счастливый")
else:
    print("Обычный")
