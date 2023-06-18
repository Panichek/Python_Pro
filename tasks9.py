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


class Category:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)


class Record:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class Article:
    def __init__(self, title, text):
        self.title = title
        self.content = text


# Створення екземпляру товару
my_product = Product("Назва категорії", 500)
print(Product)

# Створення екземпляру категорії
my_category = Category("Назва категорії")
my_category.add_product(my_product)
print(Category)

# Створення екземпляру запису
my_records = Record("Title 1", "Content 1")
print(Record)

# Створення екземпляру статті
my_article = Article("Заголовок статті", "Вміст статті.")
print(Article)
