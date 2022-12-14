from functions import *
import math


# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32
tables = 0
class_count = is_natural('Введите количество классов: ')

for i in range(1, class_count + 1):
    students = is_natural(f'Введите количество учеников в {i} классе: ')
    temp = students // 2 + students % 2
    tables += temp

print(f'Нужно столов: {tables}')


