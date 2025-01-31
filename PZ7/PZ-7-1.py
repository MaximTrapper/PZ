# Ввод данных
N1 = int(input("Введите N1: "))
N2 = int(input("Введите N2: "))
S1 = input("Введите строку S1: ")
S2 = input("Введите строку S2: ")

# Создание новой строки
new_string = S1[:N1] + S2[-N2:] if N2 > 0 else S1[:N1]

# Вывод результата
print("Результат:", new_string)