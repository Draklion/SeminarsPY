import random
import codecs
import re


def Filling_One_Dimensional_Array_Random_String_In_File(path_to_file: str, quantity: int):
    file_data = codecs.open(path_to_file, "r", "utf-8").readlines()[3]
    file_list = file_data.split()
    result_list = []
    result_list = [random.choice(file_list) for i in range(quantity)]
    print(result_list)
    return result_list


def Archiver(path_to_file: str, quantity: int):
    first_string = open(path_to_file).readlines()
    count = 1
    current_string = str(first_string[quantity][0:len(first_string[quantity])])
    full_str = ""
    current_str = current_string[0]
    for i in range(1, len(current_string)):
        if current_str == current_string[i]:
            count += 1
        else:
            full_str = f"{full_str}{count}{current_str}"
            current_str = current_string[i]
            count = 1

    return full_str


def Unarchiver(path_to_file):
    result_list = ""
    for i in range(0, 2):
        current_list_num = re.split(' ', re.sub(
            "[^-0-9]", " ", open(path_to_file).readlines()[i]))
        current_list_str = re.split(' ', re.sub(
            "[^A-z]", " ", open(path_to_file).readlines()[i]))
        result_list_num = list(filter(None, current_list_num))
        result_list_str = list(filter(None, current_list_str))
        for i in range(len(result_list_num)):
            result_list = "".join(
                f"{result_list}{int(result_list_num[i]) * result_list_str[i]}")

    return result_list
