import sys
sys.path.append('/Users/david/Desktop/python/')
from funcs.functions import *

# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

cranes_count = is_natural('Введите количество журавликов: ')
serj_petr = cranes_count / 6

if int(serj_petr) == serj_petr:
    print(f'Сережа сделал: {serj_petr}\nПетя сделал: {serj_petr}\nКатя сделала: {serj_petr * 4}')
else:
    print('Что-то пошло не так. Введенное количество журавликов не соответствует условию задачи.')