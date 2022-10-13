from time import sleep
from RefFunctions import Archiver, Unarchiver
print("Задание 2. Программа,  реализует модуль сжатия и восстановления данных.")
path_to_file_twt = "text_words.txt"
path_to_file_tcw = "text_code_words.txt"
text_code_words = open(path_to_file_tcw, "w")
for i in range(2):
    text_code_words.write(f"{Archiver(path_to_file_twt, i)}\n")
sleep(2)
print("Данные записаны в файл.")
print()
sleep(1)
print("Данные разархивированы.")
text_code_words.close()
Unarchiver(path_to_file_tcw)
