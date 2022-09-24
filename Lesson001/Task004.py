print("Задание 4. Программа, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.")

day_week = int(input("Введите день недели: "))

if 1 <= day_week < 6:
    print("Workday.")
elif day_week == 6 or day_week == 7:
    print("Weekend.")
else:
    print("It's not a day of the week!")
