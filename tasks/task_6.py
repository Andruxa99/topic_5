line: str = input("Введите строку: ")

unique_chars: set = set(line)

# Преобразование множества в кортеж при помощи функций
print("Уникальные символы:", tuple(unique_chars))
print("Количество уникальных символов:", len(unique_chars))
