# В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
# Во второй строке дано одно число days -- число дней.
#
# Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число
# дней, равное days.
#
# Примечание:
# Для решения этой задачи используйте стандартный модуль datetime.
# Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta для прибавления дней к дате.

import datetime

old_date = [int(number) for number in input().split()]
days = int(input())

new_date = datetime.date(*old_date) + datetime.timedelta(days=days)

print(new_date.year, new_date.month, new_date.day)
