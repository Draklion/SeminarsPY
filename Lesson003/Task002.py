from RefFunctions import Filling_One_Dimensional_Array_Random_String_In_File as F_O_D_A_R_S_I_F
print("Задание 2. Программа, которая определяет индекс второго вхождения строки в списке либо сообщит, что ее нет.")
path_fail = 'List.txt'
num = int(input("Введите количество элементов: "))
list_result = F_O_D_A_R_S_I_F(path_fail, num)[0]
comparison_string = F_O_D_A_R_S_I_F(path_fail, num)[1]
count = 0
index = 0
print(list_result)
print(comparison_string)

for i in range(len(list_result)):
    if comparison_string == list_result[i]:
        count += 1
    if count == 2:
        index = i

if index == 0:
    print(-1)
else:
    print(index)
