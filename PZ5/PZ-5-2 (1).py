def InvertDigits(K):
    # Преобразуем число в строку, разворачиваем и возвращаем как число
    return int(str(K)[::-1])

# Ввод пяти чисел
numbers = [int(input(f"Введите число {i + 1}: ")) for i in range(5)]

# Обращение цифр каждого числа
inverted_numbers = [InvertDigits(num) for num in numbers]

# Вывод результатов
print("Обращенные числа:")
for original, inverted in zip(numbers, inverted_numbers):
    print(f"Исходное: {original}, Обращенное: {inverted}")