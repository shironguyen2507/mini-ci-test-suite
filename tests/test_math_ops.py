import pytest

from app.math_ops import safe_div


def test_safe_div_ok():
    assert safe_div(6, 3) == 2


def test_safe_div_zero():
    with pytest.raises(ZeroDivisionError):
        safe_div(1, 0)
