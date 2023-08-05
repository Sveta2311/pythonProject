# Задача 2

# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.

# Задача 3

# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.


import logging
from datetime import datetime


logging.basicConfig(filename="oshibka.log", filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

def superLogger(func):
    def wrapper(*args, **kwargs):
        dict = {}
        dict["arguments"] = [*args]
        result = func(*args, **kwargs)
        dict["level"] = logger.level
        dict["result"] = result
        dict["function"] = func.__name__
        logger.info(dict)
        logger.info(datetime.now())
        return result

    return wrapper

@superLogger
def func2(*args):
    return 1

print(datetime.now())
print(func2(3, 4))
