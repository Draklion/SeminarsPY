import string


print("Задание 2. Программа, которая принимает на вход дробь и показать первую цифру дробной части числа.")

number = input("Введите число: ")

if number.find(".") == -1:
    print("Введено некорректное значение или целое число")
else:
    print(number[number.find(".") + 1])