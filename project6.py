# Створити програму куля долі користувач задає питання програма випадково відповідає так ні мабудь
from random import choice

question = input(f"Задайте Ваше питання: ")


def response_random():
    responses = ["Так", "Ні", "Мабудь"]
    response = choice(responses)
    print(response)

response_random()