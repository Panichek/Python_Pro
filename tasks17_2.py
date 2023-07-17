# Задача на логіювання    Підключити логер (будь яким зручним чином)
'''
Після Warning все виписувати в термінал
Все що рівнем нижче записувати до файлу log.log
додати по 30 записів кожно рівня
'''
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s'
)

logger = logging.getLogger() # Підключення логера

file_handler = logging.FileHandler('log.log')
file_handler.setLevel(logging.WARNING)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler) # Додавання обробника файлу до логера


console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)



for _ in range(30):
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')
