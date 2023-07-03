'''
2 Створити Класи Автор і Підписник і функціонал підписки на автора для підписника
'''

class AutorMixin:
    def __init__(self, name):
        self.name = name
        self.subscriber = []

    def add_subscriber(self, item):
        self.subscriber.append(item)

    def del_subscriber(self, subscriber):
        self.subscriber.remove(subscriber)

    def send_item(self, item):
        print(f"{self.name} надіслав(ла) повідомлення: {item}")
        for subscriber in self.subscriber:
            subscriber.get_item(self, item)



class SubscriberMixin:
    def __init__(self, name):
        self.name = name
        self.item = []

    def get_item(self, autor, item):
        print(f"{self.name} отримав(ла) повідомлення від {autor.name}: {item}")

    def subscribe(self, item):
        item.subscriber.append(self)

    def describe(self, items):
        items.subscriber.remove(self)

    def show_item(self):
        print(self.item)


class Item(AutorMixin):
    pass


class Client(SubscriberMixin):
    pass


autor1 = AutorMixin("Автор 1")
autor2 = AutorMixin("Автор 2")

subscriber1 = SubscriberMixin("Підписник 1")
subscriber2 = SubscriberMixin("Підписник 2")
subscriber3 = SubscriberMixin("Підписник 3")

autor1.add_subscriber(subscriber1)
autor1.add_subscriber(subscriber2)
autor2.add_subscriber(subscriber2)
autor2.add_subscriber(subscriber3)

autor1.send_item("Привіт від Автора 1!")
autor2.send_item("Привіт від Автора 2!")

autor1.del_subscriber(subscriber2)

autor1.send_item("Ще одне повідомлення від Автора 1!")
autor2.send_item("Ще одне повідомлення від Автора 2!")

item1 = Item('')

client1 = Client('')

client1.subscribe(item1)

item1.send_item("Send item")

client1.show_item(item1)