from src.code import add_ints
import pytest

@pytest.mark.parametrize("a,b,correct_sum",
    [(1, 1, 2),
    (2, 3, 5)]
    )

def test_add_ints(a: int, b: int, correct_sum: int):
    assert add_ints(a, b) == correct_sum