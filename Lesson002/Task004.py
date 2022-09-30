print("Задание 4. Программа, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.")

a = int(input("Введите первое число: "))
compos = 1
for i in range(1, a+1):
    compos = compos * i
    print(compos, end=" ")
