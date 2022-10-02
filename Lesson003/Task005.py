from RefFunctions import Filling_One_Dimensional_Array_Random as F_O_D_A_R
print("Задание 5. Программа, которая находит произведение пар чисел списка.")
number = int(input("Введите число: "))
number_list = F_O_D_A_R(number)
number_list_2 = []
compos = 1
for i in range(int(len(number_list)/2)):
    number_list_2.append(number_list[i] * number_list[len(number_list)-1 - i])
print(f"Произведение пар чисел списка: {number_list_2}")
