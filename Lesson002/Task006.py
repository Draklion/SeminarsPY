print("Задание 6. Программа, которая заполняет список по формуле (1+1/n)**n и выводит сумму элементов.")

a = int(input("Введите число: "))
sum = 0
list_elements = []
for i in range(1, a+1):
    list_elements.append(round(((1+1/i)**i)))
print(f"Заполненный список: {list_elements}")
for i in range(len(list_elements)):
    sum = sum + list_elements[i]
print(f"Сумма элементов списка: {sum}")
