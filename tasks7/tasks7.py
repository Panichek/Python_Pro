# 1 Записати у файл числа від 0 до 100
with open('numbers.txt', 'w') as file:
    for number in range(101):
        file.write(str(number) + '\n')

# 2 Прочитати текстовий файл назву якого має вказати користувач
file = open('numbers.txt', 'r')
print(file.read())
file.close()

# 3 Прочитати файл із зображення, Записати дані цього файлу під назвою 1.png
with open("file1.png", "rb") as f1, \
     open("1.png", "wb") as f2:
    f2.write(f1.read())
