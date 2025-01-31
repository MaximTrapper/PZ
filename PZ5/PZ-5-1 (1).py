def draw_stars(m):
    for i in range(1, m + 1):
        print('*' * i)

# Ввод числа m
m = int(input("Введите количество строк (m): "))

# Вызов функции для построения изображения
draw_stars(m)