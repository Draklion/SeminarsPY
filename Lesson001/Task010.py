print("Задание 10. Программа, которая на вход принимает число N и выводит числа от -N до N.")
number = int(input("Введите число: "))
for i in range(-number, number+1):
    print(i, end=" ")
