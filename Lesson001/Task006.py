print("Задание 6. Программа, которая принимает на вход координаты точки (X и Y), причем X !=0 и Y !=0\
      и выдает номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).")

print("Введите координаты точки: ")

X = int(input())
Y = int(input())

if X != 0 and Y != 0:
    print("Точка находится в центре координат.")

if X > 0 and Y > 0:
    print("Точка находится в I четверти.")
elif X < 0 and Y > 0:
    print("Точка находится в II четверти.")
elif X < 0 and Y < 0:
    print("Точка находится в III четверти.")
elif X > 0 and Y < 0:
    print("Точка находится в IV четверти.")

if X > 0 and Y == 0:
    print("Точка лежит на положительной оси Х.")
elif X == 0 and Y > 0:
    print("Точка лежит на положительной оси Y.")
elif X < 0 and Y == 0:
    print("Точка лежит на отрицательной оси Х.")
elif X == 0 and Y < 0:
    print("Точка лежит на отрицательной оси Y.")
