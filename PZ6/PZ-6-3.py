import math


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def find_min_sum_point(x_coords, y_coords):
    min_sum = float('inf')
    best_index = 0

    for i in range(len(x_coords)):
        total_distance = 0
        for j in range(len(x_coords)):
            if i != j:
                total_distance += calculate_distance(x_coords[i], y_coords[i], x_coords[j], y_coords[j])

        if total_distance < min_sum:
            min_sum = total_distance
            best_index = i

    return best_index, min_sum


# Ввод координат точек
N = int(input("Введите количество точек (N > 2): "))
x_coords = [float(input(f"Введите x для точки {i + 1}: ")) for i in range(N)]
y_coords = [float(input(f"Введите y для точки {i + 1}: ")) for i in range(N)]

# Поиск точки с минимальной суммой расстояний
index, min_distance = find_min_sum_point(x_coords, y_coords)

# Вывод результата
print(f"Точка с минимальной суммой расстояний: ({x_coords[index]}, {y_coords[index]})")
print(f"Сумма расстояний: {min_distance}")