import random
import codecs


def Filling_One_Dimensional_Array_Random_String_In_File(path_to_file: str, quantity: int):
    file_data = codecs.open(path_to_file, "r", "utf-8").readlines()[3]
    file_list = file_data.split()
    result_list = []
    result_list = [random.choice(file_list) for i in range(quantity)]
    print(result_list)
    return result_list
