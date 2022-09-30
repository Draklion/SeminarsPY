import random
from RefFunctions import Filling_One_Dimensional_Array_Random as F_O_D_A_R

print("Задание 1. Программа, которая определяет присутствует ли в заданном списке число, полученное от пользователя.")

number_elements = int(input("Введите количество элементов списка: "))
verification_number = int(input("Введите проверочное число: "))
count = 0
list_elements = []

list_elements = F_O_D_A_R(number_elements)


for i in range(0, number_elements):
    if verification_number == list_elements[i]:
        count += 1
if count != 0:
    print(
        f"The number - {verification_number} is present in the list {count} times.")
else:
    print(f"The number - {verification_number} is not present in the list.")
