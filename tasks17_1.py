# Задачі на структури даних
'''
1
Дано словники
user = {"login":"admin","password":"123123"}
config = {"menu_style":"1","text_color":"green"}
Необхідно поєднати словники
2
створити файл записати в нього 10000 випадкових числе кожне з нової стрічки
прочитати 2 останні стрічки
3
Дано текст
text = "ujhefiuvheriubguivhcrwugmr89ygw9r78cfhwtyfhwr9ge3809fg98rfuyh34yghcu9yg802134ygy134h1394uyfgq398ycfg3cy7"
знайти 3 найчастіше зустріваані літери
4
Дано словник
data = {1:1,2:2,3:3,4:4}
Поставити ключ 1 до кінця
'''

from collections import ChainMap, deque, Counter, OrderedDict
import random

# 1
'''
user = {"login":"admin","password":"123123"}
config = {"menu_style":"1","text_color":"green"}
chain = ChainMap(user, config)
print(chain)
'''
#2
'''
with open("numbers.txt", "w") as file:
    for _ in range(10000):
        random_number = random.randint(1, 1000)
        file.write(str(random_number) + "\n")

with open('numbers.txt') as file:
    data = deque(file,maxlen=2)
print(data)
'''
#3
'''
text = "ujhefiuvheriubguivhcrwugmr89ygw9r78cfhwtyfhwr9ge3809fg98rfuyh34yghcu9yg802134ygy134h1394uyfgq398ycfg3cy7"
my_counter = Counter(text)
print(my_counter.most_common(3))
'''
#4
data = {1: 1, 2: 2, 3: 3, 4: 4}
ordered_data = OrderedDict(data)
ordered_data.move_to_end(1, last=True)
print(ordered_data)