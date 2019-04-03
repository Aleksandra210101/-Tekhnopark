"""
Разработала: Крылова Александра
Проект: синонимы
"""
def add( word1, word2, dictionary):
                """Добавление в  dict  пару синонимов (word1, word2)"""
                if word1 not in dictionary:
                    dictionary[word1] = set()
                dictionary[word1].add(word2)
                if word2 not in dictionary:
                    dictionary[word2] = set()
                dictionary[word2].add(word1)

def count(word1, dictionary):
                """Узнать количество синонимов слова word"""
                if word1 in dictionary:
                    return len(dictionary[word1])
                else:
                    return 0

def check(word1, word2, dictionary):
                """Проверяет, являются ли слова word1 и word2 синонимами"""
                if word1 in dictionary:
                    if word2 in dictionary[word1]:
                        return True
                    else:
                        return False
                else:
                    return False

if __name__ == '__main__':
        SYNONYMS_DICT = {}
        NUMREQ = int(input('Введите кол-во запросов: '))
        for i in range(NUMREQ):
            request = (input('Введите запрос: ')).lower().split()
            if request[0] == 'add':
                add(request[1], request[2], SYNONYMS_DICT)
            elif request[0] == 'count':
                count(request[1], SYNONYMS_DICT)
            elif request[0] == 'check':
                check(request[1], request[2], SYNONYMS_DICT)
            else:
                print('Вы точно ввели все верно?')
                i -= 1
