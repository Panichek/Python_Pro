# Створити систему заміток
'''
Функціонал
Створення заміток
Читання заміток
Читання окремого заміток
Редагування заміток
Видалення заміток
'''
# Створення заміток
note = {"title": "Заголовок",
        "text": "Текст",
        "description": "Опис",
        "note1": {"title": "Заголовок №1",
                  "text": "Текст №1",
                  "description": "Опис №1"},
        "note2": {"title": "Заголовок №2",
                  "text": "Текст №2",
                  "description": "Опис №2"}
        }
# Читання заміток
for i in range(1, 3):
    note_title = note["note{}".format(i)]["title"]
    note_text = note["note{}".format(i)]["text"]
    note_description = note["note{}".format(i)]["description"]
    print(f"Замітка {i}:")
    print(f"Заголовок: ", note_title)
    print(f"Текст: ", note_text)
    print(f"Опис: ", note_description)
    print(f"--------")
# Читання окремого заміток
number = input("Введіть номер замітки:")
code = number
key = f"note{code}"
if key in note:
    note_title = note[key]["title"]
    note_text = note[key]["text"]
    note_description = note[key]["description"]
    print(f"Заголовок: ", note_title)
    print(f"Текст: ", note_text)
    print(f"Опис: ", note_description)
else:
    print(f"Замітка з номером {key} не знайдена.")
# Редагування заміток
number = input("Введіть номер замітки для редагування:")
code = number
key = f"note{code}"
if key in note:
    item = note[key]
    print(f"Поточні дані {code}:")
    for item_key, item_value in item.items():
        print(f"{item_key}: {item_value}")
    # Оновлення
    new_title = input("Введіть новий текст:")
    new_description = input("Введіть новий опис:")
    note[key]['text'] = new_title
    note[key]['description'] = new_description
    print(f"Дані замітки {code} були оновлені:")
    for item_key, item_value in item.items():
        print(f"{item_key}: {item_value}")
else:
    print(f"Замітка з номером {key} не знайдена.")
# Видалення заміток
number = input("Введіть номер замітки для видажлення:")
code = number
key = f"note{code}"
if key in note:
    del note[key]
    print(f"видалені дані {code}:")
    for item_key, item_value in item.items():
        print(f"{item_key}: {item_value}")
# Pезультат
print(note.values())