# module_9_5.py

# Домашнее задание по теме "Итераторы"

# Задача "Range - это просто".

# Создайте пользовательский класс исключения StepValueError, который наследуется от ValueError.
# Наследования достаточно, класс оставьте пустым при помощи оператора pass.
class StepValueError(ValueError):
    pass


# Создайте класс Iterator, который обладает следующими свойствами:
class Iterator:
    # Метод __init__(self, start, stop, step=1) - принимающий значения старта и конца итерации, а также шага.
    def __init__(self, start, stop, step=1):
        # В этом методе в первую очередь проверяется step на равенство 0.
        if step == 0:
            # Если равно, то выбрасывается исключение StepValueError('шаг не может быть равен 0')
            raise StepValueError('шаг не может быть равен 0')
        # Атрибуты объекта:
        # start - целое число с которого начинается итерация.
        self.start = start
        # stop - целое число на котором заканчивается итерация.
        self.stop = stop
        # step - шаг с которым совершается итерация.
        self.step = step
        # pointer - указывает на текущее число в итерации (изначально start)
        self.pointer = start

    # Метод __iter__ - метод сбрасывающий значение pointer на start и возвращающий сам объект итератора.
    def __iter__(self):
        # Метод сбрасывает значение pointer на start
        self.pointer = self.start
        # Метод возвращает сам объект итератора.
        return self

    # Метод __next__ - метод увеличивающий атрибут pointer на step.
    def __next__(self):
        # В зависимости от знака атрибута step итерация завершиться либо когда pointer станет больше stop,
        # либо меньше stop. Учтите это при описании метода.
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            # if (self.step > 0 and self.pointer > self.stop):
            #     print(f'Итерация остановлена: {self.pointer} > {self.stop}. Шаг итерации {self.step}.')
            # elif (self.step < 0 and self.pointer < self.stop):
            #     print(f'Итерация остановлена: {self.pointer} < {self.stop} Шаг итерации {self.step}')
            raise StopIteration
        current = self.pointer
        self.pointer += self.step
        return current


# Пример выполняемого кода:
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')  # Вывод на консоль: Шаг указан неверно

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')  # Вывод на консоль: -5 -4 -3 -2 -1 0 1
print()
for i in iter3:
    print(i, end=' ')  # Вывод на консоль: 6 8 10 12 14
print()
for i in iter4:
    print(i, end=' ')  # Вывод на консоль: 5 4 3 2 1
print()
for i in iter5:
    print(i, end=' ')  # Вывод на консоль отсутствует, так как итерация остановлена.
    # Число, с которого начинается итерация, равно 10. Оно больше числа, на котором заканчивается итерация - 1.
    # Шаг итерации равен 1.
print()
