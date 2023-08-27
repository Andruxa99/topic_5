fruits: dict = dict(яблоко=50, банан=30, груша=40, апельсин=35)

# fruits = {
#     "яблоко": 50,
#     "банан": 30,
#     "груша": 40,
#     "апельсин": 35
# }

print("Список фруктов и их цены:", fruits, sep="\n", end="\n\n")
user_input = input("Выберите фрукт из списка: ")

price = fruits[user_input]
print("Цена " + user_input + " -", price)
