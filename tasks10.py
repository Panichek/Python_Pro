# Додати функціонал об'єкту який
# 1 при додавання до об'єкта буде повертати результатом 10
# 2 при відніманні від об'єкта буде повертати 100
# 3 при перетворені на стрічку буде повертати стрічку число
# 4 при переведенні до числа буде результатом 123
class MyData:
    def __add__(self, other):  # 1
        return 10

    def __sub__(self, other):  # 2
        return 100

    def __str__(self):  # 3
        return '100'

    def __int__(self):  # 4
        return 123

data = MyData()
print(data + 0)
print(data - 0)
print(str(data))
print(int(data))