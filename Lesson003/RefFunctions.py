from csv import list_dialects
import random
from typing import List


def Filling_One_Dimensional_Array(count):
    Filled_Array = [int(input()) for i in range(count)]
    return Filled_Array


def Sort_Array_Max(source_array):
    max = source_array[0]
    for i in range(1, len(source_array)):
        if source_array[i] > max:
            max = source_array[i]
    return max


def Sort_Array_Min(source_array):
    min = source_array[0]
    for i in range(1, len(source_array)):
        if source_array[i] < min:
            min = source_array[i]
    return min


def Filling_One_Dimensional_Array_Random(number_elements):
    random_array = []
    for i in range(0, number_elements):
        random_array.append(random.randrange(20))
    print(f"Исходный список: {random_array}")

    return random_array


def Filling_One_Dimensional_Array_Random_String_In_File(path_to_file: str, quantity: int):
    file_data = open(path_to_file)
    file_list = " ".join(file_data.readlines()).split(' ')
    file_data.close()
    result_list = []
    for i in range(quantity):
        result_list.append(random.choice(file_list))
    comparison_string = random.choice(file_list)

    return [result_list, comparison_string]


def Translating_Numbers(number, numberb=" "):
    if (number <= 0):
        print(f"Число в двоичной системе счисления: {numberb}")
        return numberb

    else:
        numberb = str(number % 2) + numberb
        Translating_Numbers(number // 2, numberb)
