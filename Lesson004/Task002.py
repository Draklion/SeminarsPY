from decimal import Decimal
print("Задание 2. Программа, которая показывает большее и меньшее число.")
number = Decimal(input("Введите число: "))
accuracy = len(input("Введите требуемую точность 0.0001: "))

print(round(Decimal(number), accuracy-2))
