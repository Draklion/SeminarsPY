import random
from RefFunctions import Filling_One_Dimensional_Array_Random_String_In_File as FODARSIF
print("Задание 1. Программа, которая удаляет из текста все слова, содержащие \"абв\".")
number = int(input("Введите число: "))
if number < 1:
    print("Введено некорректное значение.")
else:
    path_in_file = "text_words.txt"
    source_list = FODARSIF(path_in_file, number)
    result_list = []
    result_list = [source_list[i]
                   for i in range(len(source_list)) if source_list[i] != "абв"]
    if result_list == []:
        print("В списке только 1 элемент \"абв\"")
    else:
        print(result_list)
