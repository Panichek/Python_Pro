users = []


def create_note():
    note = {"title": input("Введіть заголовок:"),
            "text": input("Введіть текст:")}
    return note


def view_notes(notes):
    for number, note in enumerate(notes, 1):
        print(f"{number}) - {note['title']}")


def get_note_number(notes):
    view_notes(notes)
    note_number = input("Оберіть номер замітки:")
    if note_number.isdigit() and 0 < int(note_number) <= len(notes):
        note_number = int(note_number) - 1
        return note_number


def user_menu(user):
    while True:
        choice = input("""1 створити замітку
2 прочитати замітки
3 очистити замітки
4 читати одну замітку
5 оновити текст замітки
6 видалити замітку
9 вихід до основного меню:""")

        if choice == "1":
            note = create_note()
            user["notes"].append(note)

        if choice == "2":
            view_notes(user["notes"])

        if choice == "3":
            user["notes"] = []
            print("Замітки очищено")

        if choice == "4":
            number = get_note_number(user["notes"])
            if number != None:
                print(user["notes"][number])

        if choice == "5":
            number = get_note_number(user["notes"])
            if number != None:
                user["notes"][number].update(create_note())

        if choice == "6":
            number = get_note_number(user["notes"])
            if number != None:
                user["notes"].pop(number)

        if choice == "9":
            break


def registration():
    login = input("login:")
    password = input("password:")
    if login not in [user["login"] for user in users]:
        user = {"login": login,
                "password": password,
                "notes": []}
        users.append(user)


def check_user(login,
               password,
               user):
    if (login == user["login"]
            and password == user["password"]):
        return True
    else:
        return False


def login():
    login = input("login:")
    password = input("password:")
    for user in users:
        if check_user(login, password, user):
            print("Ви Увійшли !!!")
            user_menu(user)


while True:
    choice = input("1 registration 2 login 3 exit:")
    if choice == "1":
        registration()

    if choice == "2":
        login()

    if choice == "3":
        break