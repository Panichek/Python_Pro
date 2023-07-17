# Задача тесутвання Дано функцію
'''
def sum_elements(*args):
    pass

Функція має через args отримувати елементи і повертати результатом їх суму (при умові що там тільки числа)
Розробити код через TDD (прикріпити файл із кодом + написані для цього коду тести)
'''
class Sum_elements:
    def sum_elements(*args):
        # Перевірка, чи всі аргументи є числами
        if all(isinstance(arg, (int, float)) for arg in args):
            return sum(args)
        else:
            raise ValueError("All arguments must be numbers.")


    #print(sum_elements(1, 2.7, 5.3))
    def sum(self):
        pass

