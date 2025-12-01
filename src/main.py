import re


def clear_names(file_name: str) -> list:
    """Функция для отчистки имен от лишних симолов"""
    new_names_list = list()
    with open('data/' + file_name) as names_file:
        names_list = names_file.read().split()
        for name_item in names_list:
            new_name = ''
            for symbol in name_item:
                if symbol.isalpha():
                    new_name += symbol
            if new_name.isalpha():
                new_names_list.append(new_name)
    return new_names_list


def is_cyrillic(name_item):
    """Проверка на вхождение кириллицы в строку"""
    return bool(re.search('[а-яА-Я]', name_item))


def filter_russian_name(names_list: list) -> list:
    """Фильтрация имен написанных на Русском"""
    new_name_list = list()
    for name_item in names_list:
        if cyrillic(name_item):
            new_name_list.append(name_item)
    return new_names_list


if __name__ == '__main__':
    cleared_name = clear_names('data/names.txt')


    print(filter_russian_name(cleared_name))
