import RefFunctions

print("Задание 8. Программа, которая принимает на вход координаты двух точек и находит расстояние между ними в пространстве.")

print("Введите координаты первой точки: ")
first_point = RefFunctions.Filling_One_dimensional_Array(2)

print("Введите координаты второй точки: ")
second_point = RefFunctions.Filling_One_dimensional_Array(2)

print(((second_point[0] - first_point[0])**2 +
      (second_point[1] - first_point[1])**2)**0.5)
