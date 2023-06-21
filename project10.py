'''#
Створити систему входу і регістрації із Адміністратором Автором і підписником
Зберігання в середині одного списку бази даних (Реалізувати із збереженням в файлі
(реалізація файлової частини є у кода написаних на лекції))
'''
import pickle
import os

class PickleFileService:
    def __init__(self, filename):
        self.__filename = filename
        if not os.path.exists(filename):
            self.clear()

    def write(self, data):
        with open(self.__filename, "wb") as f:
            f.write(pickle.dumps(data))

    def read(self):
        with open(self.__filename, "rb") as f:
            return pickle.loads(f.read())

    def clear(self):
        with open(self.__filename, "wb") as f:
            f.write(pickle.dumps([]))


class Db:
    def __init__(self, filename):
        self.__fileservice = PickleFileService(filename)
        self.sync()

    def append(self, element):
        self.data.append(element)
        self.save()

    def pop(self, number):
        self.data.pop(number)
        self.save()

    def remove(self, element):
        self.data.remove(element)
        self.save()

    def clear(self):
        self.data.clear()
        self.save()

    def save(self):
        self.__fileservice.write(self.data)

    def sync(self):
        self.data = self.__fileservice.read()

    def __setitem__(self, key, value, ):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]

    def __str__(self):
        return f"{self.data}"

    def __len__(self):
        return len(self.data)


articles = Db("articles.txt")


class Author:
    def __init__(self, Db):
        self.autor = "autor"

    def __str__(self):
        return str(self.autor)


autor = Author(str(articles))


class Subscriber:
    def __init__(self, Db):
        self.subscriber = "subscriber"

    def __str__(self):
        return str(self.subscriber)


subscriber = Subscriber(str(articles))


class Admin:
    def __init__(self, Db):
        self.admin = "admin"

    def __str__(self):
        return str(self.admin)


admin = Admin(str(articles))


class User:
    def __init__(self, user_types, username, password):
        self.user_types = user_types.__str__()
        self.username = username
        self.password = password


class Users:
    def __init__(self, Db):
        self.users = []
        self.database = Db

    def register(self, user_types, username, password):
        new_user = User(user_types, username, password)
        self.users.append(new_user)
        self.database.append(new_user.user_types + ": (login: " + new_user.username + "; Password: " + new_user.password+")")


users = Users(articles)

while True:
    choice = input(f"""1 зареєструватись як автор
2 зареєструватись як subscriber    
3 зареєструватись як admin   
4 прочитати всі записи 
5 кількість записів
6 видалити записи
0 вийти: """)
    if choice == "1":
        user_type = autor
        name = input("Введіть Ім'я:")
        password = input("Введіть Пароль:")
        users.register(user_type, name, password)
    if choice == "2":
        user_type = subscriber
        name = input("Введіть Ім'я:")
        password = input("Введіть Пароль:")
        users.register(user_type, name, password)
    if choice == "3":
        user_type = admin
        name = input("Введіть Ім'я:")
        password = input("Введіть Пароль:")
        users.register(user_type, name, password)
    if choice == "4":
        print(articles.__str__())
    if choice == "5":
        print(articles.__len__())
    if choice == "6":
        print(articles.clear())
    if choice == "0":
        break
