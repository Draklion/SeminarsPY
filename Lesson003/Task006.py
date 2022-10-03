print("Задание 6. Программа, которая составляет список чисел Фибоначчи, в том числе для отрицательных индексов.")

number = int(input("Введите число: "))
if number <= 1:
    print("Вы ввели некорректное значение.")
else:
    firstNumberFibonacci = 0
    secondNumberFibonacci = 1
    Fibonacci_list = [0, 1]
    Fibonacci_reverse_list = []
    for i in range(2, number+1):
        Fibonacci_list.append(firstNumberFibonacci+secondNumberFibonacci)
        firstNumberFibonacci = secondNumberFibonacci
        secondNumberFibonacci = Fibonacci_list[i]
    for i in range(1, len(Fibonacci_list)):
        Fibonacci_reverse_list.append(
            Fibonacci_list[len(Fibonacci_list)-i]*(-1)**i)
    Fibonacci_reverse_list.extend(Fibonacci_list)
    print(Fibonacci_reverse_list)
