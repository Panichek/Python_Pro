# 1
'''
Створити функції action1 action2 action3
action1 має виводити при виконанні 1
action2 має виводити при виконанні 2
action3 має виводити при виконанні 3
'''
# 2
'''
Створити декоратор data isset і список data
Зробити можливим виконанні дій action1 action2 action3
тільки при наявності даних в списку data
'''
num = (input("Вибрати порожній список даних = введіть 0, вибрати непорожній список даних = введіть 1:"))
if num == "0":
    data = []
if num == "1":
    data = [1]


def data_isset(func):
    def wrapper():
        if data:  # Перевірка, чи є дані в списку
            func()
        else:
            print("Дані відсутні. Неможливо виконати дію.")

    return wrapper


@data_isset
def action1():
    print("1")


@data_isset
def action2():
    print("2")


@data_isset
def action3():
    print("3")


action1()
action2()
action3()
