# В Python каждая переменная и значение имеют свой тип данных, который представляет класс. Рассмотрим основные типы данных и методы работы с ними.
#
# 1. Числа
# Типы данных, связанные с числами: целые числа (int), числа с плавающей запятой (float) и комплексные числа (complex).
#
# Примеры:
#
# python
# Копировать код
a = 5
print(a, "имеет тип", type(a))  # <class 'int'>

b = 2.0
print(b, "имеет тип", type(b))  # <class 'float'>

c = 1 + 2j
print(c, "является ли комплексным числом?", isinstance(c, complex))  # True

# Особенности:
#
# Целые числа могут быть любой длины, ограничены только доступной памятью.
# Числа с плавающей запятой имеют ограниченную точность.
# Комплексные числа записываются в виде x + yj, где x — действительная часть, y — мнимая.
# Пример работы с числами:
#
# python
# Копировать код
a = 1234567890123456789
print(a)  # 1234567890123456789

b = 0.1234567890123456789
print(b)  # 0.12345678901234568

c = 1 + 2j
print(c)  # (1+2j)
#----------------------------------------------------------------------------------------------------------------------

# Особенности:
#
# Целые числа могут быть любой длины, ограничены только доступной памятью.
# Числа с плавающей запятой имеют ограниченную точность.
# Комплексные числа записываются в виде x + yj, где x — действительная часть, y — мнимая.
# Пример работы с числами:
#
# python
# Копировать код

a = 1234567890123456789
print(a)  # 1234567890123456789

b = 0.1234567890123456789
print(b)  # 0.12345678901234568

c = 1 + 2j
print(c)  # (1+2j)
#----------------------------------------------------------------------------------------------------------------------


