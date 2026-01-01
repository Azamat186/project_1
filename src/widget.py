import re


def mask_account_card(data: str) -> str:
    """Маскирует карту или аккаунт в зависимости от типа"""
    match = re.match(r"^(?P<type>карта|счет)\s+(?P<number>\w+)$", data.strip())
    if not match:
        raise ValueError("Некорректный формат данных.")

    type_ = match.group("type")
    number = match.group("number")

    if type_ == "карта":
        first_digits = number[:4]
        middle_digits = number[4:-4]
        last_digits = number[-4:]
        return f"{first_digits} {middle_digits[:2]} **** {last_digits}"
    elif type_ == "счет":
        return f"{number[-4:]}"
