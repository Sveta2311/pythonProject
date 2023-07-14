# Задача 3

# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import csv
import json
import os
from pathlib import Path


def get_from_user(file: Path) -> None:
    json_file = {}
    if os.path.isfile(file):
        with open(file, 'r', encoding='utf-8') as js:
            if os.path.getsize(file) > 0:
                json_file = json.load(js)

    rows = []
    print(json_file)
    for id, values in json_file.items():
            rows.append({'id': id, 'name': values[0], 'level': values[1]})

    with open('out.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['id', 'name', 'level']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == '__main__':
    get_from_user(Path('./access_file.json'))
