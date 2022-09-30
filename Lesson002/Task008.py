import random
print("Задание 8. Программа, которая реализуйет алгоритм перемешивания списка.")

a = int(input("Введите количество элементов списка: "))

list_elements = []
list_elements_result = []
index = 0
for i in range(0, a):
    list_elements.append(i)
print(f"Исходный список: {list_elements}")

len = len(list_elements)

for i in range(len):
    index = random.randrange(len)
    list_elements_result.append(list_elements[index])
    list_elements.pop(index)
    len -= 1
print(f"Новый список: {list_elements_result}")
