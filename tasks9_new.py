'''
Створити класи
Товари
Категорія
Запис
та стаття (поля та їх модиіфкатори на Ваше бачення)
'''


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return str(self.name)

    def __int__(self):
        return int(self.price)


class ProductCollection():

    def __init__(self):
        self.products = []

    def __str__(self):
        return str(self.products)

    def __int__(self):
        return str(self.products)

    def add_product(self, product):
        self.products.append(product)


class Category(ProductCollection):
    def __str__(self):
        return str(self.products)
    def __int__(self):
        return str(self.products)

class Record:
    def __init__(self, number_record):
        self.number_record = number_record

    def __int__(self):
        return int(self.number_record)


class Article:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\n"


# Створення екземпляру класу товару
my_product = Product("Назва категорії", 500)
print(str(my_product), int(my_product))

# Створення екземпляру класу категорії
my_category = Category()
my_category.add_product(my_product)
print(my_category)

# Створення екземпляру класу запису
my_records = Record(1)
print(int(my_records))

# Створення екземпляру класу статті
my_article = Article("Заголовок статті", "Вміст статті")
print(my_article)
