# Створити систему товарів
'''
Функціонал
Створення товарів
Читання товарів
Читання окремого товару
Редагування товару
Видалення товару
'''
# Товар - словник (структура за власним баченням)
# Створення товарів
article = {
    "name": "Назва",
    "code": "Код",
    "price": "Ціна",
    "quantity": "Кількість",
    "article1": {"name": "Ноутбук", "code": 1, "price": 15000, "quantity": 3},
    "article2": {"name": "Монітор", "code": 2, "price": 5000, "quantity": 9},
    "article3": {"name": "Сиcтемний блок", "code": 3, "price": 16000, "quantity": 2}
}
print(article.values())
# Читання всіх товарів
counter = 1
key = f"article{counter}"
while key in article:
    item = article[key]
    print(f"Товар {counter}:")
    for item_key, item_value in item.items():
        print(f"{item_key}: {item_value}")
    print(f"_______________________________")
    counter += 1
    key = f"article{counter}"
# Читання окремого товару
number = input("Введіть код товару:")
code = number
key = f"article{code}"
while key in article:
    item = article[key]
    print(f"Товар {code}:")
    for item_key, item_value in item.items():
        print(f"{item_key}: {item_value}")
    print(f"Вибраний товар {code}:")
    break
# Редагування товару
number = input("Введіть код товару для редагування:")
code = number
key = f"article{code}"
if key in article:
    item = article[key]
    print(f"Поточні дані товару {code}:")
    for item_key, item_value in item.items():
        print(f"{item_key}: {item_value}")
    # Оновлення даних товару
    new_name = input("Введіть нову назву товару:")
    new_price = input("Введіть нову ціну товару:")
    article[key]['name'] = new_name
    article[key]['price'] = new_price
    print(f"Дані товару {code} були оновлені:")
    for item_key, item_value in item.items():
        print(f"{item_key}: {item_value}")
else:
    print(f"Товар з кодом {code} не знайдений.")
# Видалення товару
number = input("Введіть код товару для видалення:")
code = number
key = f"article{code}"
if key in article:
    item = article[key]
    print(f"Дані товару {code}, які будуть видалені:")
    for item_key, item_value in item.items():
        print(f"{item_key}: {item_value}")
    del article[key]
    print(f"Товар {code} був успішно видалений.")
else:
    print(f"Товар з кодом {code} не знайдений.")
# Pезультат редагування
print(article.values())