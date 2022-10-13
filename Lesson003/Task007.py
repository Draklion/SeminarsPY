from RefFunctions import Sort_Array_Max as SAMax, Sort_Array_Min as SAMin, Filling_One_Dimensional_Array_Random_Float as F_O_D_A_R_F, Sorting_Exception_Whole as S_E_W
print("Задание 7. Программа, которая находит разницу между максимальным и минимальным значением дробной части элементов.")
number = int(input("Введите число: "))
numbers_list = F_O_D_A_R_F(number)

print(f"Список с исключенной целой частью: {S_E_W(numbers_list)}")
max = SAMax(S_E_W(numbers_list))
print(f"Max: {max}")
min = SAMin(S_E_W(numbers_list))
print(f"Min: {min}")

print(
    f"Разница между максимальным и минимальным значением дробной части элементов: {round((max-min), 2)}")
