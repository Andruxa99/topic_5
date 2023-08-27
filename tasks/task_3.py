numbers: list = [12, 45, 0.34711, 67, 89, 34, 55.632781, 78.9395]

value: float | int = sum(numbers)  # Сумма всех элементов
average_value: float = round(value / len(numbers), 1)  # Среднее значение

print("Среднее значение:", average_value)
