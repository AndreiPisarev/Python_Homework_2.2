"""
def detect_encording(name_file) - читаем файл побайтно, определяет кодировку файла и возвращает её

def detect_encording(name_file) - принимает кодировку, читает файл построчно удаляя смволы \n и разделяе строку на слова
возвращает список слов длинее 6 символов в файле

def top_10_popular(list_char_more_6) - принимает список из слов длинее 6 символов, находит число повторений каждого
слова, формирует вложенный список вида [[число повторений, слово], [число повторений, слово]].Убирает повтор. элекменты,
сортирует по числу повторений, выделяет топ 10, убирает кол-во повторений из списка, возвращает только список 10 слов
наиболее часто повторяющиеся в тексте файла

print_word(word, name_file) - принимает список топ 10 и имя обрабатываемого файла, формирует печать

main() - указывает список файлов для обработки, запускаем в цикле обработку каждого файла:
- определяем кодировку
- читаем файл определенной кодировкой
- назодим топ 10 слов
- выводим информацию
"""

import chardet


def detect_encording(name_file):
    with open(name_file, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        print("\nКодировка в {}: {}".format(name_file, result['encoding']))

        return result['encoding']


def read_file(name_file, encoding_file):
    with open(name_file, encoding=encoding_file) as news_file:
        list_char_more_6 = list()
        string_file = news_file.read().replace('\n', '')  # Подкинули задачку с \n  в начале строки :)
        list_string_file = string_file.lower().split(' ')
        list_char_more_6 = [i for i in list_string_file if len(i) > 6]  # Наконец научился так писать

        return list_char_more_6


def top_10_popular(list_char_more_6):
    list_word = list()
    list_word_unique = list()

    list_word = [[list_char_more_6.count(i), i] for i in list_char_more_6]  # Список из числа повтор. и слова
    # list_word_unique = [i for i in list_word if i not in list_word_unique]  # Такая конструкция не работает, не понял.

    for i in list_word:
        if i not in list_word_unique:
            list_word_unique.append(i)  # Убираем повторяющие элементы из списка

    list_word_unique.sort(reverse=True)  # Сортрируем, первыми занч. будут с наиб. числом повторений [повторн:слово]
    list_word_top_10 = list_word_unique[:10]  # С помощью среза выбираем ТОП 10

    list_word = list()
    for i in list_word_top_10:
        for i_i in i:
            if i[1] not in list_word:
                list_word.append(i[1])

    return list_word


def print_word(word, name_file):
    print('Топ 10 самых часто встречающихся в новостях {} слов длиннее 6 символов:'.format(name_file))
    for i in word:
        print(i)


def main():
    list_file = ['newsafr.txt', 'newscy.txt', 'newsfr.txt', 'newsit.txt']

    for name_file in list_file:
        encoding_file = detect_encording(name_file)
        list_char_more_6 = read_file(name_file, encoding_file)
        list_word = top_10_popular(list_char_more_6)
        print_word(list_word, name_file)


main()
