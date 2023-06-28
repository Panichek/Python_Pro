# Виконати рефакторинг з переробкою коду
'''
class Article:
    title = ""
    description = ""
    text = ""

class PapperArticle:
    title = ""
    description = ""
    text = ""
    papper = ""

class SiteArticle:
    title = ""
    description = ""
    text = ""
    site = ""

class BlogArticle:
    title = ""
    description = ""
    text = ""
    blog = ""

class NewsArticle:
    title = ""
    description = ""
    text = ""
    news = ""

articles = []

choice = input("1 papper 2 site 3 blog 4 news:")
if choice == "1":
    article = PapperArticle()
elif choice == "2":
    article = SiteArticle()
elif choice == "3":
    article = BlogArticle()
elif choice == "4":
    article = NewsArticle()
else:
    article = None
if article:
    articles.append(article)
'''


class Article:
    def __init__(self,
                 title,
                 description,
                 text):
        self.title = title
        self.description = description
        self.text = text


class PapperArticle(Article):
    def __init__(self,
                 title,
                 description,
                 text,
                 papper):
        super().__init__(title, description, text)
        self.papper = papper


class SiteArticle(Article):
    def __init__(self,
                 title,
                 description,
                 text,
                 site):
        super().__init__(title, description, text)
        self.site = site


class BlogArticle(Article):
    def __init__(self,
                 title,
                 description,
                 text,
                 blog):
        super().__init__(title, description, text)
        self.blog = blog


class NewsArticle(Article):
    def __init__(self,
                 title,
                 description,
                 text,
                 news):
        super().__init__(title, description, text)
        self.news = news


def get_article(article_type):
    available_articles = {"1": PapperArticle,
                          "2": SiteArticle,
                          "3": BlogArticle,
                          "4": NewsArticle}
    return available_articles.get(article_type)


articles = []


def menu():
    choice = input("1 papper 2 site 3 blog 4 news:")
    article_class = get_article(choice)
    if article_class:
        article = article_class("", "", "", "")
        articles.append(article)


while True:
    menu()
    print(articles)
'''   
def menu():
    choice = input("1 papper 2 site 3 blog 4 news:")
    if choice == "1":
        article = PapperArticle("", "", "", "")
    elif choice == "2":
        article = SiteArticle("", "", "", "")
    elif choice == "3":
        article = BlogArticle("", "", "", "")
    elif choice == "4":
        article = NewsArticle("", "", "", "")
    else:
        article = None
    if article:
        articles.append(article)

menu()
'''
