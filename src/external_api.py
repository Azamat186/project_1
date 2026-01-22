import os
import requests
from typing import Dict, Optional
from dotenv import load_dotenv

load_dotenv()

def convert_to_rubles(transaction: Dict[str, any]) -> Optional[float]:
    """
 Возвращает сумму транзакции в рублях. Если валюта USD/EUR, отправляет запрос к API
 для конвертации валюты.
 :param transaction: Словарь с данными о транзакции
    :type transaction: dict
    :rtype: float | None
    """
    amount = transaction.get('amount')
    currency = transaction.get('currency')

    if not amount or not currency:
        return None

    if currency == 'RUB':
        return float(amount)

    # Получаем токен из переменных окружения
    api_key = os.getenv('EXCHANGE_RATES_DATA_API_KEY')

    # Определяем базовую валюту и целевую (рубль)
    base_currency = currency
    target_currency = 'RUB'

    # Отправляем запрос к API
    response = requests.get(
        f"https://api.apilayer.com/exchangerates_data/latest?base={base_currency}&symbols=RUB",
        headers={"apikey": api_key}
    )

    if response.status_code == 200:
        data = response.json()
        ruble_rate = data['rates']['RUB']
        converted_amount = float(amount) * ruble_rate
        return round(converted_amount, 2)
    else:
        print(f"Ошибка при обращении к API: {response.text}")
        return None
