# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

def randomlist():
    r_list = []
    for i in range (5):
        num = random.randint(1,30)
        r_list.append(num)
    return r_list

new_list = randomlist()
print(new_list)

# ищем значения по индексам и поворачиваем список
lastN = (new_list[4])
pre_lastN = (new_list[3])
rev_list = list(reversed(new_list))
# print(rev_list) #проверка что список перевернулся
firstN = (rev_list[4])
pre_firstN = (rev_list[3])

# я в итоге не понял зачем реверснул список, но зато научился это делать

MultiFL = (lastN * firstN) 
MultiPFPL = (pre_firstN * pre_lastN) 

print(MultiFL, MultiPFPL)