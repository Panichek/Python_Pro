# Список контактів
# прийняти дзвінок
# надіслати дзвінок
# переглянути журнал дзвінків
# Якщо контакт є буде виписувати його ім'я
# Якщо контакту немає юуде виписано номер

# КОНТАКТИ
# Записи про дзвінки
'''
Додати можливість при додані нових контактів переробити список записів про дзвінки додаючи імена до записів до дзвінків
додати функціонал очистки списку записів
'''


def data_exists(data):
    def decorator(action):
        def wrapper(*args, **kwargs):
            if data:
                action(*args, **kwargs)
            else:
                print("Некорректна операція")

        return wrapper

    return decorator


records = []
contacts = []


# Контакт - словник з ключами Ім'я телефоня
# Запис про дзвінок словник ключі - ім'я  телефон статус (прийнято або надіслано)
@data_exists(contacts)
def get_contact_name(number):
    for contact in contacts:
        if contact["number"] == number:
            return contact["name"]


def add_contact():
    contact = {"name": input("Введіть ім'я"),
               "number": input("Введіть номер телефону:")}
    contacts.append(contact)


def call(number):
    name = get_contact_name(number)
    if not name:
        name = number
    record = {"name": name,
              "number": number,
              "status": "call"}
    records.append(record)


def recieve(number):
    name = get_contact_name(number)
    if not name:
        name = number
    record = {"name": name,
              "number": number,
              "status": "recieve"}
    records.append(record)


@data_exists(records)
def show_calls():
    for record in records:
        print(f"""Зателефонував {record['name']}
З номером {record['number']}
Статуc дзвінка - {record['status']}""")


def clear_records():
    global records
    records = []


while True:
    choice = input(f"""1 додати контакт
2 зателефонувати
3 прийняти дзвінок
4 переглянути журнал
5 очистити список записів
9 вихід: """)
    if choice == "1":
        add_contact()
    if choice == "2":
        number = input("Введіть номер:")
        call(number)
    if choice == "3":
        number = input("Введіть номер:")
        recieve(call)
    if choice == "4":
        show_calls()
    if choice == "5":
        clear_records()
    if choice == "9":
        break
