print("Задание 1. Программа, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a**2 == b or b**2 == a:
    print("Является.")
else:
    print("Не является.")
    print("Добавил изменения.")   
