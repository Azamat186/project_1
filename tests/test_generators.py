import pytest
from src.generators import *

@pytest.fixture(scope="module")
def sample_transactions():
    """Генерация фиксированных транзакций."""
    return [
        {"id": 1, "description": "Описание первой транзакции", "operationAmount": {"currency": {"code": "USD"}}},
        {"id": 2, "description": "Вторая транзакция", "operationAmount": {"currency": {"code": "EUR"}}},
        {"id": 3, "description": "Третья транзакция", "operationAmount": {"currency": {"code": "USD"}}}
    ]

@pytest.mark.parametrize(
    "currency_code, expected_ids",
    [
        (None, []),  # Проверка None в currency_code
        ("", []),  # Пустая строка
        ("usd", []),  # Регистрозависимость
    ],
    ids=["none_currency", "empty_currency", "lowercase_currency"]
)
def test_filter_by_currency_edge_cases(sample_transactions, currency_code, expected_ids):
    result = list(filter_by_currency(sample_transactions, currency_code))
    result_ids = [item["id"] for item in result]
    assert sorted(result_ids) == sorted(expected_ids)


def test_filter_by_currency_nested_missing_fields(sample_transactions):
    # Транзакция с неполной структурой operationAmount
    partial_tx = {"id": 4, "operationAmount": {}}
    transactions = sample_transactions + [partial_tx]

    result = list(filter_by_currency(transactions, "USD"))
    result_ids = [item["id"] for item in result]
    assert 4 not in result_ids  # Должна быть исключена

@pytest.mark.parametrize(
    "transactions, expected_output",
    [
        ([{"description": None}], [None]),
        ([{"desc": "Нет поля description"}], [None]),
        ([{}], [None]),
    ],
    ids=["none_description", "missing_field", "empty_dict"]
)
def test_transaction_descriptions(transactions, expected_output):
    descriptions = transaction_descriptions(transactions)
    actual_descriptions = list(descriptions)
    assert actual_descriptions == expected_output

# Параметризированные тесты для filter_by_currency
@pytest.mark.parametrize(
    "input_data, expected_ids",
    [
        (
            [{"id": 1, "operationAmount": {"currency": {"code": "USD"}}}],
            [1]
        ),
        (
            [],
            []
        ),
        (
            [{"id": 1, "operationAmount": {"currency": {"code": "RUB"}}}],
            []
        ),
        (
            [
                {"id": 1, "operationAmount": {"currency": {"code": "RUB"}}},
                {"id": 2, "operationAmount": {"currency": {"code": "USD"}}}
            ],
            [2]
        ),
        (
            [
                {"id": 1, "operationAmount": {"currency": {"code": "USD"}}},
                {"id": 2, "operationAmount": {"currency": {"code": "USD"}}}
            ],
            [1, 2]
        ),
        (
            [{"id": 1, "operationAmount": {}}],
            []
        )
    ],
    ids=[
        "single_match",
        "empty_input",
        "no_matches",
        "partial_match",
        "full_match",
        "missing_operation_amount"
    ]
)
def test_filter_by_currency(input_data, expected_ids):
    result = list(filter_by_currency(input_data, "USD"))
    result_ids = [item["id"] for item in result]
    assert sorted(result_ids) == sorted(expected_ids)

# Тест для transaction_descriptions
def test_transaction_descriptions_with_sample_transactions(sample_transactions):
    descriptions = transaction_descriptions(sample_transactions)
    actual_results = list(descriptions)
    assert all(isinstance(d, str) for d in actual_results)

# Дополнительные тесты для card_number_generator
@pytest.mark.parametrize(
    "start, stop, expected_first, expected_last",
    [
        (1, 5, "0000 0000 0000 0001", "0000 0000 0000 0005"),
        (1000, 1002, "0000 0000 0000 1000", "0000 0000 0000 1002"),
        (9999999999999995, 9999999999999999, "9999 9999 9999 9995", "9999 9999 9999 9999")
    ],
    ids=[
        "small_range",
        "medium_range",
        "large_range"
    ]
)
def test_card_number_generator(start, stop, expected_first, expected_last):
    gen = card_number_generator(start, stop)
    numbers = list(gen)
    first_number = numbers[0]
    last_number = numbers[-1]
    assert first_number == expected_first and last_number == expected_last

# Тест проверки исключения пустых транзакций
def test_empty_transactions():
    empty_txns = []
    filtered = list(filter_by_currency(empty_txns, "USD"))
    assert not filtered

# Проверка исключительных ситуаций в описании транзакций
def test_missing_description():
    txn_without_desc = [{"id": 1}]
    desc_gen = transaction_descriptions(txn_without_desc)
    next(desc_gen, None) is None

# Проверка валидных диапазонов в генераторе карт
def test_valid_card_ranges():
    # 1. start < 1
    with pytest.raises(ValueError):
        card_number_generator(-1, 10)  # Должно вызвать ошибку

    # 2. start > end
    with pytest.raises(ValueError):
        card_number_generator(10, 1)  # Должно вызвать ошибку

    # 3. start слишком длинный
    with pytest.raises(ValueError):
        card_number_generator(10000000000000000, 9999999999999999)  # 17 цифр

    # 4. end слишком большой
    with pytest.raises(ValueError):
        card_number_generator(9999999999999999, 10000000000000000)  # end > макс. значения
