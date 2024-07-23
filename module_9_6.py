# module_9_6.py

# Домашнее задание по теме "Генераторы"

# Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
# при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
def all_variants(text):
    length = len(text)
    # print(f'Всего символов в text\nlength = len(text) = {length}')
    for sub_len in range(1, length + 1):  # Начинаем с длины подстроки 1 и увеличиваем до длины строки
        # print(f'Длина подстроки\nsub_len = {sub_len}')
        for start in range(length - sub_len + 1):
            # print(f'Начинаем с\nstart = {start}')
            # print(f'Заканчиваем перед\nstart + sub_len = {start + sub_len}')
            # print(f'Вывод подстроки от text[{start}] символа до text[{start + sub_len}] символа.')
            # print(f'text[start:start + sub_len] = text[{start}:{start} + {sub_len}] = {text[start:start + sub_len]}')
            yield text[start:start + sub_len]


# Пример работы функции
a = all_variants("abc")
for i in a:
    print(i)

# Вывод на консоль:
# a
# b
# c
# ab
# bc
# abc
