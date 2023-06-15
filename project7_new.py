# Створити проєкт записник із можливістю збереження даних у файлі
# Дані зберігати у вигляді списку із словників (Використання pickle)
# Функціонал користувача Додати запис Прочитати всі записи очистити список записів
import pickle

def create_article():
    article_new = {"title": input("Введіть заголовок:"),
                   "text": input("Введіть текст:")}

    with open("article.txt", "rb") as f:
        articles = pickle.load(f)
    articles.append(article_new)

    with open("article.txt", "wb") as f:
        pickle.dump(articles, f)
    return article_new


def read_article():
    with open("article.txt", "rb") as f:
        print(pickle.loads(f.read()))


def clear_article():
    with open("article.txt", "wb") as f:
        print(pickle.dump([], f))


while True:
    choice = input(f"""1 додати запис
2 прочитати всі записи
3 очистити список записів 
4 вийти: """)
    if choice == "1":
        create_article()
    if choice == "2":
        read_article()
    if choice == "3":
        clear_article()
    if choice == "4":
        break
