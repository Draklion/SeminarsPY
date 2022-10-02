from RefFunctions import Filling_One_Dimensional_Array_Random as F_O_D_A_R
print("Задание 3. Программа, которая преобразовывает десятичное число в двоичное.")
number = int(input("Введите число: "))
number_list = F_O_D_A_R(number)
sum = 0
for i in range(0, len(number_list), 2):
    sum = sum + number_list[i]
print(f"Сумма нечетных элементов списка: {sum}")
