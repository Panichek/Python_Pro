# НА ЦИКЛ FOR
'''
Дано список names
вивести коже ім'я почерзі
names = ['Name1','Name2','Name3','Name4']
'''
names = ['Name1', 'Name2', 'Name3', 'Name4']
for name in names:
    print(name)
# На створення послідовності
'''
Створити послідовності від 0 до 100 по 10
від 100 джо 10000 по 5
від 1 до 10 по 5
'''
sequence_1 = []
for i in range(0, 101, 10):
    sequence_1.append(i)
print(sequence_1)
sequence_2 = []
for i in range(100, 100001, 5):
    sequence_2.append(i)
print(sequence_2)
sequence_3 = []
for i in range(1, 11, 5):
    sequence_3.append(i)
print(sequence_3)
# На цикл while
'''
Користувач посчтійно відповідає на запитання q - вихід
Якщо користувач відповідає q програма закривається
'''
while True:
    question = input("Запитання? ('q' вихід): ")
    if question == 'q':
        break
