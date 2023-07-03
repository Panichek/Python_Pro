# Виконати рефакторинг коду із виправленнями
'''
class Item:
    def __init__(self,
                 name=""):
        self.name = name
        self.price = 10


class Box:
    def __init__(self, items=[]):
        self.items = items


class DiscontBox:
    def __init__(self,
                 discont=0,
                 items=[]):
        self.items = items
        self.discont = discont


class Cart:
    def __init__(self, items):
        self.items = items

    @property
    def get_price(self):
        price = 0
        for item in self.items:
            if type(item) == Item:
                price += item.price

            if type(item) == Box:
                for item in item.items:
                    price += item.price

            if type(item) == DiscontBox:
                tmp_price = 0
                for item in item.items:
                    tmp_price += item.price
                    tmp_price -= item.discont
                    price += tmp_price

        return price

'''
class Item:
    price = 10

    def get_price(self):
        return self.price

    @property
    def price(self) -> int:
        return self._price


class Box:
    def __init__(self,items):
        self.items = items

    def get_price(self):
        price = 0
        for item in self.items:
            price += item.get_price()
        return price


class DiscontBox:
    def __init__(self, discont: int = 0, items: list = None):
        self._items = items or []
        self._discont = discont

    @property
    def items(self) -> list:
        return self._items

    @property
    def discont(self) -> int:
        return self._discont


class Cart:
    def __init__(self, items: list):
        self._items = items

    @property
    def items(self) -> list:
        return self._items

    @property
    def get_price(self) -> int:
        price = 10
        for item in self.items:
            price += item.get_price()
        return price