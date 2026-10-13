def mask_card(number: str) -> str:
    """Mask all but the last 4 digits of a card number."""
    digits = "".join(ch for ch in number if ch.isdigit())
    return "*" * max(len(digits) - 4, 0) + digits[-4:]
