'''
В систему користувач потрапляє кожні 0.1 часові одиниці
час виконання операції від 1 до 3 секунд
кількість клієнтів за час роботи 10000
визначити кількість комірок обслуговування аби
час обслуговування не перевищував 5 часових одиниць
'''
import random
import time
from datetime import datetime
from threading import Thread, Semaphore

time_comming = 0.1  # за умови 1 секунда = 1 часова одиниця
min_time_working = 1
max_time_working = 3
clients = 10000
sem = Semaphore(19)  # 19-20 комірок обслуговування
queue_time = 5


def action():
    start = datetime.now()
    with sem:
        print(f"користувач прийшов")
        random_time_working = random.randint(min_time_working, max_time_working)
        time.sleep(random_time_working)
        print(f"користувач вийшов")
    print(f"Час виконання - {datetime.now() - start} має бути до {queue_time} секунд ")


threads = []

for number in range(clients):
    time.sleep(time_comming)
    t = Thread(target=action)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print("Робота завершена.")
