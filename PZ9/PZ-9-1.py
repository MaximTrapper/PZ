# Исходная строка
data = '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15'

# Разделяем строку на части
parts = data.split()

# Извлекаем температуры (игнорируем первый элемент, так как это "2020год")
temperatures = list(map(int, parts[1:]))

# Список месяцев
months = [
    "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
    "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
]

# Создаем словарь
temperature_dict = {month: temp for month, temp in zip(months, temperatures)}

# Функция для вычисления средней температуры
def calculate_average(temps):
    return sum(temps) / len(temps)

# Функция для нахождения минимальной температуры
def find_minimum(temps):
    return min(temps)

# Вычисляем среднюю и минимальную температуры
average_temp = calculate_average(temperatures)
min_temp = find_minimum(temperatures)

# Выводим результаты
print("Словарь температур по месяцам:")
print(temperature_dict)
print(f"Средняя температура за год: {average_temp:.2f}°C")
print(f"Минимальная температура за год: {min_temp}°C")