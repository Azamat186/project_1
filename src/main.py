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


def filter_english_name(names_list: list) -> list:
    """Фильтрация имен написанных на Английском"""
    new_name_list = list()
    for name_item in names_list:
        if not cyrillic(name_item):
            new_name_list.append(name_item)
    return new_names_list


def save_to_file(file_name: str, data: str) -> None:
    """Сохраняет данные в файл"""
    with open('data/' + file_name, 'w') as names_file:
        names_file.write(data)


if __name__ == '__main__':
    cleared_name = clear_names('../data/names.txt')

    filtered_names = filter_russian_name(cleared_name)
    save_to_file(
        'russian_names.txt',
        '\n'.join(filtered_names)
    )

filtered_names = filter_english_name(cleared_name)
    save_to_file(
        'english_names.txt',
        '\n'.join(filtered_names)
    )
