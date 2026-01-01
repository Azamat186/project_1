import pytest


@pytest.fixture
def transaction_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-07-01"},
        {"id": 2, "state": "CANCELED", "date": "2023-07-02"},
        {"id": 3, "state": "EXECUTED", "date": "2023-07-03"},
    ]


@pytest.fixture
def valid_cards():
    return ["1234567890123456", "9876543210987654"]


@pytest.fixture
def valid_accounts():
    return ["123456789012", "987654321098"]


@pytest.fixture
def invalid_cards():
    return ["123456789012345", "abc123"]


@pytest.fixture
def invalid_accounts():
    return ["12345678901", "xyz123"]
