# 1 На створення зміних
'''
Створити зміні
name
office
weight
height
(name - стрічка office число ціле weight число з комою height число з комою)
'''
name = str(input("Введіть Ім'я:"))
office = int(input("Введіть office:"))
weight = float(input("Введіть weight:"))
height = float(input("Введіть height:"))
print("Ім'я: "+name+"; " "Office: "+str(office)+"; " "Weight: "+str(weight)+"; " "Height: "+str(height))
# Інший спосіб виводу інформації
print(f"Iм'я: {name}; Office: {str(office)}; Weight: {str(weight)}; Height: {str(height)}.")

# 2 на введення даних і особливості виводу
'''
Коирстувач вводить значення в змінну text
Далі користувач відповідає на запитання 1 великими 2 малими
В залежності від вибору значення змінної text має вивестись або великими або малими літерами
'''
text = str(input("Введіть text:"))
num = (input("Вивести текст великими літерами = введіть 1, або вивести текст малими літерами = введіть 2:"))
if num == "1":
    print(text.upper())
if num == "2":
    print(text.lower())
else:
    print("Ви ввели інше число")

# додаткове завдання
"""
Привести до 2кової системи числення
числа
10
15
17
викласти файл з даними формату число - двійковий аналог
"""
number1 = int(10)
number2 = int(15)
number3 = int(17)
print(bin(number1)[2:] +"\n"+bin(number2)[2:]+"\n"+ bin(number3)[2:])
# Інший варіант
number1 = bin(10)
number2 = bin(15)
number3 = bin(17)
print(number1[2:] + "\n" + number2 [2:]+ "\n"+ number3[2:])