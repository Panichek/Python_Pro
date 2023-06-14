#Створити систему товарів
'''
Функціонал
Створення товарів
Читання товарів
Читання окремого товару
Редагування товару
Видалення товару
'''
# Товар - словник (структура за власним баченням)
class GoodsSystem:
    def __init__(self):
        self.goods = {}

    def create_goods(self, name, price, quantity):
        goods = {
            'name': name,
            'price': price,
            'quantity': quantity
        }
        self.goods[name] = goods

    def read_all_goods(self):
        return list(self.goods.values())

    def read_single_good(self, name):
        return self.goods.get(name)

    def update_good(self, name, price=None, quantity=None):
        goods = self.goods.get(name)
        if goods:
            if price:
                goods['price'] = price
            if quantity:
                goods['quantity'] = quantity
            return True
        return False

    def delete_good(self, name):
        if name in self.goods:
            del self.goods[name]
            return True
        return False


# Приклад використання
goods_system = GoodsSystem()

# Створення товарів
goods_system.create_goods('Товар 1', 10, 5)
goods_system.create_goods('Товар 2', 20, 3)
goods_system.create_goods('Товар 3', 15, 8)

# Читання всіх товарів
all_goods = goods_system.read_all_goods()
print(all_goods)
# Вивід: [{'name': 'Товар 1', 'price': 10, 'quantity': 5}, {'name': 'Товар 2', 'price': 20, 'quantity': 3},
#         {'name': 'Товар 3', 'price': 15, 'quantity': 8}]

# Читання окремого товару
single_good = goods_system.read_single_good('Товар 2')
print(single_good)
# Вивід: {'name': 'Товар 2', 'price': 20, 'quantity': 3}

# Редагування товару
updated = goods_system.update_good('Товар 1', price=15, quantity=10)
print(updated)
# Вивід: True

# Перевірка оновлених даних
updated_good = goods_system.read_single_good('Товар 1')
print(updated_good)
# Вивід: {'name': 'Товар 1', 'price': 15, 'quantity': 10}

# Видалення товару
deleted = goods_system.delete_good('Товар 3')
print(deleted)
# Вивід: True

# Перевірка списку після видалення
all_goods = goods_system.read_all_goods()
print(all_goods)
# Вивід: [{'name': 'Товар 1', 'price': 15, 'quantity': 10}, {'name': 'Товар 2', 'price': 20, 'quantity': 3}]