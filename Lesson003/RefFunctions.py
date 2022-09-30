import random


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
