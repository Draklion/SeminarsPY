print("Задание 5. Программа, которая принимает на вход вещественное число и показывает сумму его цифр.")

a = input("Введите число: ")
sum = 0
for i in range(len(a)):
    if a[i] == "." or a[i] == ",":
        continue
    else:
        sum = sum + int(a[i])
print(f"Cумма цифр чисел: {sum}")
