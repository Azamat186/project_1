from src.processings import filter_by_state, sort_by_date


def test_filter_by_state(transaction_data):
    executed_txns = filter_by_state(transaction_data)
    assert len(executed_txns) == 2
    assert all(tx["state"] == "EXECUTED" for tx in executed_txns)

    canceled_txn = filter_by_state(transaction_data, state="CANCELED")
    assert len(canceled_txn) == 1
    assert canceled_txn[0]["state"] == "CANCELED"


def test_sort_by_date(transaction_data):
    sorted_txns = sort_by_date(transaction_data)
    assert sorted_txns[0]["date"] == "2023-07-01"
    assert sorted_txns[-1]["date"] == "2023-07-03"

    reversed_sorted_txns = sort_by_date(transaction_data, reverse=True)
    assert reversed_sorted_txns[0]["date"] == "2023-07-03"
    assert reversed_sorted_txns[-1]["date"] == "2023-07-01"
