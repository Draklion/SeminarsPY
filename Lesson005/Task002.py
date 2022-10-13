from RefFunctions import Archiver
print("Задание 2. Программа,  реализует модуль сжатия и восстановления данных.")
path_to_file = "text_words.txt"
text_code_words = open("text_code_words.txt", "w")
for i in range(2):
    print(f"{Archiver(path_to_file, i)}")
    text_code_words.write("10wqserd qewr")
