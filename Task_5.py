#** 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fibonacci(num: int):
    a = 1
    b = 1
    list_fibonacci = [0]

    for i in range(num):
        list_fibonacci.append(a)
        list_fibonacci.insert(0, a * (-1) ** i)
        a, b = b, b + a


    return list_fibonacci

print("Введите число: ")
print(fibonacci(int(input())))