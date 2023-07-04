'''
ПОВЕДІНКОВІ ПАТТЕРНИ
1 Створити нескінченну послідовність від – 1000 до 1000
Спочатку від -1000 виводить числа до 1000 як тільки доходить до 1000
починає повертати числа в зворотньому порядку
2 Створити об’єкт дії який при ініціалізації приймає 1 параметр text а при
виконанні виводить його
3 Сворити Класс User який може мати 3 статуси 1 standart 2 vip 3 super vip
В залежності від статусу користувача метод info буде виводити Ви vip ви
Звичайний користувач або Ви супер Vip користувач
'''
'''
# Ітератор
class MyData:
    def __init__(self,
                 start,
                 increment):
        self.start = start
        self.increment = increment

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == -1000:
            self.increment = 1
        elif self.start == 1000:
            self.increment = -1

        value = self.start
        self.start += self.increment
        return value


my_data = MyData(-1000, 1)

for number in my_data:
    print(number)
'''

'''
# Command
class MyAction:
    def __init__(self,
                 text):
        self.text = text

    def __call__(self):
        print(self.text)


action = MyAction("Text")

action()
'''

# State
class StandartStatus:
    def get_message(self, text):
        return "Ви звичайний користувач"


class VipStatus:
    def get_message(self, text):
        return "Ви VIP користувач"


class SuperVipStatus:
    def get_message(self, text):
        return "Ви супер VIP користувач"

class User:
    def __init__(self,state):
        self.state = state
    def info(self,text):
        return self.state.get_message(text)

user1 = User(StandartStatus())
print(user1.info(""))

user2 = User(VipStatus())
print(user2.info(""))

user3 = User(SuperVipStatus())
print(user3.info(""))