def filter_by_currency(transactions, currency_code):
    """
    Возвращает итератор,включающий только транзакции с указанным кодом валюты.

    :param transactions: Список словарей с транзакциями.
    :param currency_code: Код валюты ("USD", "EUR" и т.д.).
    :return: Итератор с соответствующими транзакциями.
    """
    return (tx for tx in transactions
            if tx
            .get('operationAmount', {})
            .get('currency', {})
            .get('code')
            == currency_code
            )


def transaction_descriptions(transactions):
    """
    Генератор, возвращающий описание каждой транзакции по порядку.

    :param transactions: Список словарей с транзакциями.
    :return: Итератор с описаниями транзакций.
    """
    return (tx.get('description') for tx in transactions)


def card_number_generator(start=1, end=9999999999999999):
    """
    Генератор банковских карточных номеров в формате XXXX XXXX XXXX XXXX.

    :param start: Начальная карта.
    :param end: Конечная карта.
    :return: Итератор с номерами карт.
    """
    if start < 1 or len(str(start)) > 16 or len(str(end)) > 16 or end > 9999999999999999 or start > end:
        raise ValueError(f"Некорректный диапазон карт: ({start}, {end})")

    format_str = "{:016d}"
    for i in range(start, end + 1):
        formatted_number = format_str.format(i)
        blocks = [formatted_number[j:j+4] for j in range(0, len(formatted_number), 4)]
        yield " ".join(blocks)
