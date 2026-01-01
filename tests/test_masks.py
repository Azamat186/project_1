import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(valid_cards, invalid_cards):
    for card_num in valid_cards:
        masked = get_mask_card_number(card_num)
        assert masked.startswith(card_num[:4])
        assert masked.endswith(card_num[-4:])
        assert "" in masked

    for bad_card in invalid_cards:
        with pytest.raises(ValueError):
            get_mask_card_number(bad_card)


def test_get_mask_account(valid_accounts, invalid_accounts):
    for acc_num in valid_accounts:
        masked = get_mask_account(acc_num)
        assert masked.startswith("")
        assert masked.endswith(acc_num[-4:])

    for bad_acc in invalid_accounts:
        with pytest.raises(ValueError):
            get_mask_account(bad_acc)
