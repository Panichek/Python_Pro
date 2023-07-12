'''
1 Створити дії action1 action2 action3
час виконання яких (10 20 і 40 секунд відповідно)
Свторити програму яка дозволить їх виконувати в фоновому режимі
на вибір користувача
'''
import threading
import time
from multiprocessing import Process


def action1():
    print("Дія action1")


def action2():
    print("Дія action2")


def action3():
    print("Дія action3")


def run_actions():
    for _ in range(2):
        threading.Timer(10, action1).start()
        time.sleep(10)
        threading.Timer(20, action2).start()
        time.sleep(10)
        threading.Timer(40, action3).start()
    time.sleep(60)

actions = {"1": action1,
           "2": action2,
           "3": action3}

choice = input("1 2 3:")
if __name__ == "__main__":
    if choice in actions:
        print("Програма починає виконання дій у фоновому режимі.")
        run_actions()
        p = Process(target=actions[choice])
        p.start()
    print("Виконано")