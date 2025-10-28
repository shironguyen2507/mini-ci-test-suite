def safe_div(a, b):
    """Chia an toàn: b = 0 -> ném ZeroDivisionError."""
    if b == 0:
        raise ZeroDivisionError("b must not be zero")
    return a / b
