# module_9_7.py

# Домашнее задание по теме "Декораторы".

# Задание: Декораторы в Python.

# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом
# и "Составное" в противном случае.
def is_prime(func):
    # Не забудьте написать внутреннюю функцию wrapper в is_prime
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 1:
            # if result % 2 == 0:
            #     print("Составное")
            # odd = 3
            # while odd * odd <= result and result % odd != 0:
            #     odd += 2
            # if odd * odd > result:
            #     print("Простое")
            # else:
            #     print("Составное")

            # У любого составного числа есть собственный делитель, не превосходящий квадратного корня из числа.
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        else:
            print("Составное")
        return result
    # Функция is_prime должна возвращать wrapper
    return wrapper


@is_prime
# Функция, которая складывает 3 числа (sum_three)
def sum_three(first, second, third):
    return first + second + third


# Пример:
result = sum_three(2, 3, 6)
print(result)

# Результат консоли:
# Простое
# 11
