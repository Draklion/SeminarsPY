from email.mime import image
import re
import random
from RefFunctions import Sort_Array_Max as SAMax, Sort_Array_Min as SAMin
print("Задание 1. Программа, которая показывает большее и меньшее число.")
number = random.randint(0, 2)
print(f"Исходная строка: {open('Task001.txt').readlines()[number]}")
s1 = re.sub("[^-0-9]", " ", "".join(open('Task001.txt').readlines()[number]))
result = re.split(' ', s1)
print(f"Исходный массив: {result}")
result = list(filter(None, result))
print(f"Результирующий массив: {result}")
print(
    f"Максимальное значение: {SAMax(result)}, минимальное значение: {SAMin(result)}")
