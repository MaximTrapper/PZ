def check_alternation(lst):
    for i in range(1, len(lst)):
        if (lst[i] > 0 and lst[i - 1] > 0) or (lst[i] < 0 and lst[i - 1] < 0):
            return i + 1  # Порядковый номер (индекс + 1)
    return 0

# Ввод списка
N = int(input("Введите размер списка: "))
lst = [int(input(f"Введите элемент {i + 1}: ")) for i in range(N)]

# Проверка чередования
result = check_alternation(lst)
print(f"Результат: {result}")