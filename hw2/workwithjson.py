"""
Разработала: Крылова Александра
Проект: работа с .json файлами
"""


import json
import re
import collections
import zipfile
import os
import glob


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


os.mkdir('JsonFolder')
FILES = glob.glob('RC*.bz2')
for name_file in FILES:
    unzip(name_file, 'JsonFolder/' + name_file[:-4] + '.json')
WORDS = tuple()
for name_file in FILES:
    WORDS = WORDS + tuple(words('JsonFolder/' + name_file[:-4] + '.json'))
TOP20WORDS = collections.Counter(WORDS).most_common(20)
with open('Top.json', 'w') as f:
    for i in TOP20WORDS:
        f.write(str(i))
