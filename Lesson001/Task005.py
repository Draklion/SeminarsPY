print("Задание 5. Программа, которая проверяет истиность утверждения !(X or Y or Z)=!X and !Y and !Z.")

for X in range(2):
    for Y in range(2):
        for Z in range(2):
            if not (X or Y or Z) == (not X and not Y and not Z):
                print(X, Y, Z)
