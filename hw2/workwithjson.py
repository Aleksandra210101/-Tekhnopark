"""
Разработала: Крылова Александра
Проект: решение квадратичного уравнения
"""


import json
import re
import collections
import zipfile
import os


def unzip(filepath, newfilepath):
    """Разархивирование файла"""
    zip_file = zipfile.bz2.BZ2File(filepath)
    data = zip_file.read()
    open(newfilepath, 'wb').write(data)


def words(filepath):
    """Функция, которая возвращает последовательность слов из body данного файла """
    with open(filepath, "r") as f_p:
        file = f_p.readline().lower()
        results = ''
        while file:
            f_j = json.loads(file)
            if f_j['body'] != 'deleted':
                results += f_j['body']
            file = f_p.readline().lower()
        results = re.findall(r'\w{4,}', results)
    return results


NAME = ['RC_2006-01', 'RC_2006-02', 'RC_2006-03', 'RC_2006-04', 'RC_2005-12']

os.mkdir('JsonFolder')
for i in NAME:
    unzip(i + '.bz2', 'JsonFolder/' + i + '.json')
WORDS = tuple()
for i in NAME:
    WORDS = WORDS + tuple(words('JsonFolder/' + i + '.json'))
TOP20WORDS = collections.Counter(WORDS).most_common(20)
with open('Top.json', 'w') as f:
    for i in TOP20WORDS:
        f.write(str(i))
