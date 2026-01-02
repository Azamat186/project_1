from typing import List, Dict
from datetime import datetime


def filter_by_state(transactions: List[Dict],
                    state: str = "EXECUTED") -> List[Dict]:
    """Фильтрует список операций по состоянию"""
    return [t for t in transactions if t.get("state") == state]


def sort_by_date(transactions: List[Dict], reverse: bool = False) \
        -> List[Dict]:
    """Сортирует операции по дате."""
    return sorted(
        transactions,
        key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'),
        reverse=reverse,
    )
