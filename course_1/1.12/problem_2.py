# Напишите программу, принимающую на вход целое число, которая выводит True, если
# переданное значение попадает в интервал (−15,12]∪(14,17)∪[19,+∞) и False в
# противном случае (регистр символов имеет значение).
#
# Обратите внимание на разные скобки, используемые для обозначения интервалов. В задании используются
# полуоткрытые и открытые интервалы. Подробнее про это вы можете прочитать, например,
# на википедии (полуинтервал, промежуток).

number = int(input())

if -15 < number <= 12 or 14 < number < 17 or number >= 19:
    print("True")
else:
    print("False")