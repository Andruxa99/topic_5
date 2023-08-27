string: str = str(input("Введите строку: "))

string_min: str = min(string)  # Минимальный символ
string_max: str = max(string)  # Максимальный символ

print("Минимальный символ: " + string_min,
      "Максимальный символ: " + string_max,
      sep="\n")
