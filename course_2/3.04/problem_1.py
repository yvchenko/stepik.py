# Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе
# Чикаго с 2001 года по настоящее время.
#
# Одним из атрибутов преступления является его тип – Primary Type.
#
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
import csv
import datetime

statistics = {}

with open("Crimes.csv") as f:
    crimes = csv.reader(f)
    next(crimes)
    for row in crimes:
        date = datetime.datetime.strptime(row[2], "%m/%d/%Y %H:%M:%S %p")
        if date.year == 2015:
            if row[5] not in statistics:
                statistics[row[5]] = 1
            else:
                statistics[row[5]] += 1

crime_rating = {v: k for k, v in statistics.items()}

print(crime_rating[max(crime_rating)])
