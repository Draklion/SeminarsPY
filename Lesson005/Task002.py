from time import sleep
from RefFunctions import Archiver, Unarchiver
print("Задание 2. Программа,  реализует модуль сжатия и восстановления данных.")
path_to_file_twt = "text_words.txt"
path_to_file_tcw = "text_code_words.txt"
text_code_words = open(path_to_file_tcw, "w")
for i in range(2):
    text_code_words.write(f"{Archiver(path_to_file_twt, i)}\n")
print()
print("Данные записаны в файл.")
print()
print("Данные разархивированы.")
print()
text_code_words.close()
Unarchiver(path_to_file_tcw)
