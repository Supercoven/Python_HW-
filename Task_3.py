# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.

def dec_to_bin(num):
    list_dec = []

    while num > 0:
        list_dec.insert(0, num % 2) # складываем результат в начало списка через insert
        num //= 2

    print(" ".join(map(str, list_dec))) # переводим список в строку для вывода

print('Введите число для конвертации в двоичную систему: ')
dec_to_bin(int(input()))