# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

import random

print('Введите длину списка')
n = int(input())

# создаём список заданной пользователем длины, заполненный рандомом
def randomlist():
    r_list = []
    for i in range (n):
        num = random.randint(1,30)
        r_list.append(num)
    return r_list

new_list = randomlist()

# ищем элементы на нечётных позициях
def not_even(new_list):
    summ = 0
    for s in range(0, len(new_list), 2):
        summ += new_list[s]
    return summ

# вывод информации
print(new_list)
print(not_even(new_list))




