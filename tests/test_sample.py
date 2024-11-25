"""Tests the square root function."""

from pytest import mark
from template.sample import square_root


@mark.parametrize(
    "number, root",
    [
        (4, 2),
        (9, 3),
        (16, 4),
    ],
)
def test_square_root(number, root):
    """Tests the square root function."""
    assert root == square_root(number)
