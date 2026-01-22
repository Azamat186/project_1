from unittest.mock import patch, MagicMock
from src.external_api import convert_to_rubles

@patch('requests.get')
def test_convert_usd_to_rubles(mock_get):
    """Тест конвертации долларов в рубли"""
    mock_response = MagicMock()
    mock_response.json.return_value = {'rates': {'RUB': 75}}  # Пример курса
    mock_response.status_code = 200  # Устанавливаем статус-код явно
    mock_get.return_value = mock_response
    result = convert_to_rubles({'amount': '100', 'currency': 'USD'})
    assert result == 7500.00

@patch('requests.get')
def test_convert_eur_to_rubles(mock_get):
    """Тест конвертации евро в рубли"""
    mock_response = MagicMock()
    mock_response.json.return_value = {'rates': {'RUB': 85}}  # Пример курса
    mock_response.status_code = 200  # Устанавливаем статус-код явно
    mock_get.return_value = mock_response
    result = convert_to_rubles({'amount': '50', 'currency': 'EUR'})
    assert result == 4250.00
