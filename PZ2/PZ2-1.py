# Ввод количества секунд с начала суток
N = int(input("Введите количество секунд с начала суток: "))

# Вычисление количества секунд с начала последней минуты
seconds_since_last_minute = N % 60

# Вывод результата
print(f"Количество секунд с начала последней минуты: {seconds_since_last_minute}")