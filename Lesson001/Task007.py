print("Задание 7. Программа, которая по заданному номеру четверти, показывает диапозон возможных координат точек в этой четверти (X и Y).")

print("Введите номер четверти: ")

number = int(input())

if number == 1:
    print("X > 0, Y > 0.")
elif number == 2:
    print("X < 0, Y > 0.")
elif number == 3:
    print("X < 0, Y < 0.")
elif number == 4:
    print("X > 0, Y < 0.")
else:
    print("The quarter is entered incorrectly!")
