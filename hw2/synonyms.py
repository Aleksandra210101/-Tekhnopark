"""
Разработала: Крылова Александра
Проект: решение квадратичного уравнения
"""


def add(word1, word2, dictionary):
    """Добавление в  dict  пару синонимов (word1, word2)"""
    if word1 not in dictionary:
        dictionary[word1] = []
        dictionary[word1].append(word2)
    if word2 not in dictionary[word1]:
        dictionary[word1].append(word2)
    if word2 not in dictionary:
        dictionary[word2] = []
        dictionary[word2].append(word1)
    if word1 not in dictionary[word2]:
        dictionary[word1].append(word2)


def count(word1, dictionary):
    """Узнать количество синонимов слова word"""
    if word1 in dictionary:
        print('Кол-во синонимов слова ' + word1.title() + ' : ' + str(len(dictionary[word1])))
    else:
        print(0)


def check(word1, word2, dictionary):
    """Проверяет, являются ли слова word1 и word2 синонимами"""
    if word1 in dictionary:
        if word2 in dictionary[word1]:
            print('Yes')
        else:
            print('No')
    else:
        print('No')


SYNONYMS = {}
NUMREQ = int(input('Введите кол-во запросов: '))
for i in range(NUMREQ):
    request = (input('Введите запрос: ')).lower().split()
    if request[0] == 'add':
        add(request[1], request[2], SYNONYMS)
    elif request[0] == 'count':
        count(request[1], SYNONYMS)
    elif request[0] == 'check':
        check(request[1], request[2], SYNONYMS)
    else:
        print('Вы точно ввели все верно?')
        i -= 1
