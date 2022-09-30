print("Задание 3. Программа, которая определяет количество вхожднений одной строки в другую.")

first_string = input("Введите первую строку: ")
second_string = input("Введите вторую строку: ")
count = 0
for i in range(len(first_string)-1):
    if (second_string[:len(second_string)] == first_string[i:i+len(second_string)]):
        count += 1
        i = i+len(second_string)
print(f"Количество вхождений: {count}")
