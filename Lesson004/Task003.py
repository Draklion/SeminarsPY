print("Задание 3. Программа, которая составляет список простых множителей числа N.")
number = int(input("Введите число: "))
result_list = []
count = 2
for i in range(number):
    if (number % count == 0):
        number = number/count
        result_list.append(count)
    else:
        count += 1
print(f"Итоговый список: {result_list}")
