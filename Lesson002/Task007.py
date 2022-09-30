print(
    "Задание 7. Программа, которая принимает на вход 2 числа. Задает список из N элементов, заполненных числами из промежутка [-N, N].")

first_position = int(input("Введите первую позицию: "))
second_position = int(input("Введите вторую позицию: "))
count_elements = int(input("Введите количество элементов: "))
list_elements = []

for i in range(-count_elements, count_elements+1):
    list_elements.append(i)
print(f"Заполненный список: {list_elements}")
print(
    f"Произведение элементов {list_elements[first_position-1]} и {list_elements[second_position-1]}: {list_elements[first_position-1]*list_elements[second_position-1]}")
