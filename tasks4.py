'''
Створити функції action1 action2 action3
action1 має виводити при виконанні 1
action2 має виводити при виконанні 2
action3 має виводити при виконанні 3
'''


# Варіант виведення в консоль
def action1():
    print("1")


def action2():
    print("2")


def action3():
    print("3")


action1()
action2()
action3()
print("___________________")


# Варіант виведення в змінну
def action1():
    return ('1')


def action2():
    return ('2')


def action3():
    return ('3')


a = action1()
b = action2()
c = action3()
print(a + '\n' + b + '\n' + c)
print("___________________")

# Ускладнений варіант
name = 3


def action1(arg='1'):
    print(arg)

    def action2(arg=2):
        print(arg)

    return action2()


def action3():
    print(name)
    return name


action1()
action3()
