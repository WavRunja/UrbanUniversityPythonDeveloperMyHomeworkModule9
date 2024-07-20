# module_9_2.py

# Домашнее задание по теме "Списковые, словарные сборки"

# Даны несколько списков, состоящих из строк
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# В переменную first_result запишите список созданный при помощи сборки состоящий из длин строк списка first_strings,
# при условии, что длина строк не менее 5 символов.
first_result = [len(s) for s in first_strings if len(s) >= 5]

# В переменную second_result запишите список созданный при помощи сборки состоящий из пар слов(кортежей)
# одинаковой длины. Каждое слово из списка first_strings должно сравниваться с каждым из second_strings. (два цикла)
second_result = [(first, second) for first in first_strings for second in second_strings if len(first) == len(second)]

# В переменную third_result запишите словарь созданный при помощи сборки, где парой ключ-значение будет
# строка-длина строки.
# Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings.
# Условие записи пары в словарь - чётная длина строки.
third_result = {string: len(string) for string in first_strings + second_strings if len(string) % 2 == 0}

# Пример выполнения кода
print(first_result)
# [10, 8, 8]
print(second_result)
# [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'),
# ('Variable', 'Computer')]
print(third_result)
# {'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}
