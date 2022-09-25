def Filling_One_dimensional_Array(count):
    Filled_Array = [int(input()) for i in range(count)]
    return Filled_Array


def Sort_Array(source_array):
    max = source_array[0]
    for i in range(1, len(source_array)):
        if source_array[i] > max:
            max = source_array[i]
    return max
