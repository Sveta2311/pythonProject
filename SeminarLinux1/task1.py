# Написать автотест на bash, который читает содержимое файла /etc/os-release
# (в нем хранится информация о версии системы)
# и выведет на экран “SUCCESS” если в нем содержатся версия 22.04.1,
# кодовое имя jammy и команда чтения файла выполнена без ошибок.
# В противном случае должно выводится “FAIL”.

import subprocess
comand = "cat /etc/os-release"

if __name__ == '__main__':
    result = subprocess.run(comand, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    print(result)