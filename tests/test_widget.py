from src.widget import mask_account_card


def test_mask_account_card(valid_cards, valid_accounts):
    for card_num in valid_cards:
        masked = mask_account_card(f"карта {card_num}")
        assert masked.startswith(card_num[:4])
        assert masked.endswith(card_num[-4:])
        assert "" in masked

    for acc_num in valid_accounts:
        masked = mask_account_card(f"счет {acc_num}")
        assert masked.startswith("")
        assert masked.endswith(acc_num[-4:])
