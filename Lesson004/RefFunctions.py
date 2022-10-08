def Sort_Array_Max(source_array):
    max = int(source_array[0])
    for i in range(1, len(source_array)):
        if int(source_array[i]) > max:
            max = int(source_array[i])
    return max


def Sort_Array_Min(source_array):
    min = int(source_array[0])
    for i in range(1, len(source_array)):
        if int(source_array[i]) < min:
            min = int(source_array[i])
    return min
