from random import randint
from unittest import result


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


def Filling_One_Dimensional_List(count):
    filled_list = [i for i in range(20, count+1)]
    return filled_list


def Сalculations(current_list):
    result_list = [current_list[i]
                   for i in range(len(current_list)) if int(current_list[i]) % 20 == 0 or int(current_list[i]) % 21 == 0]
    return result_list


def Dictionary_Names(path_to_file):
    current_list = "".join(
        open(path_to_file, "r", encoding="utf-8").readlines()).split()
    current_list.sort()
    print(current_list)
    result_list = list(set([current_list[i][0]
                       for i in range(0, len(current_list))]))
    result_list.sort()
    result_dictionary = {}
    for i in current_list:
        if i[0] in result_dictionary:
            result_dictionary[i[0]] += [i]
        else:
            result_dictionary[i[0]] = [i]

    return result_dictionary
