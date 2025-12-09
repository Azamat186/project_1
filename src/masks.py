def get_mask_card_number(card_number: int) -> str:
    """
    Маска банковской карты в формате XXXX XX** **** XXXX.

    :param card_number: Номер карты (целое число)
    :return: Отформатированная строка с маской карты
    """
    if len(str(card_number)) != 16:
        raise ValueError("Номер карты должен состоять ровно из 16 цифр.")
    formatted_number = f"{card_number:016d}"
    masked_part = formatted_number[:6] + '**' + '****' + formatted_number[-4:]
    return ' '.join([masked_part[i:i + 4] for i in range(0, len(masked_part), 4)])


def get_mask_account(account_number: int) -> str:
    """
    Маска банковского счёта в формате **XXXX.

    :param account_number: Номер счёта (целое число)
    :return: Отформатированная строка с маской счёта
    """
    return f"**{account_number % 10000:04d}"
