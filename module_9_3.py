# module_9_3.py

# Домашнее задание по теме "Генераторные сборки"

# Дано 2 списка:
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк из списков
# first и second, если их длины не равны. Для перебора строк попарно из двух списков используйте функцию zip.
first_result = (len(is_first) - len(is_second) for is_first, is_second in zip(first, second)
                if len(is_first) != len(is_second))

# В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения строк
# в одинаковых позициях из списков first и second. Составьте эту сборку НЕ используя функцию zip.
# Используйте функции range и len.
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Пример выполнения кода
print(list(first_result))
print(list(second_result))
