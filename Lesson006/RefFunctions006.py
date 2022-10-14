from random import randint


def Сomparison(path_to_file):
    current_list = open(path_to_file).readlines()[
        randint(0, 1)].rstrip().split(", ")
    print(f"Исходный список: {current_list}")
    result_list = [current_list[i+1]
                   for i in range(0, len(current_list)-1, 2) if int(current_list[i]) < int(current_list[i+1])]
    if len(current_list) % 2 != 0:
        result_list.append(current_list[len(current_list)-1])
    else:
        result_list
    return result_list
