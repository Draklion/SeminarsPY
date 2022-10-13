import random
import codecs


def Filling_One_Dimensional_Array_Random_String_In_File(path_to_file: str, quantity: int):
    file_data = codecs.open(path_to_file, "r", "utf-8").readlines()[3]
    file_list = file_data.split()
    result_list = []
    result_list = [random.choice(file_list) for i in range(quantity)]
    print(result_list)
    return result_list


def asdf(path_to_file: str, quantity: int):
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
