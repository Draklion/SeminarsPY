print("Задание 2. Программа,  реализует модуль сжатия и восстановления данных.")
first_string = open("text_words.txt").readlines()[:2]
count = 1
for i in range(len(first_string[0])):
    current_string = str(first_string[0][0:len(first_string[0])-1])
    print(current_string)
    current_str = current_string[0]
    for i in range(0, len(current_string)):
        if current_string[i] == current_str:
            count += 1
        else:
            current_str == current_string[i]
            count = 1
    print(count, current_str)
