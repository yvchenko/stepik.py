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

ticket = input()

a, b, c, d, e, f = int(ticket[0]), int(ticket[1]), int(ticket[2]), int(ticket[3]), int(ticket[4]), int(ticket[5])

if a + b + c == d + e + f:
    print("Счастливый")
else:
    print("Обычный")